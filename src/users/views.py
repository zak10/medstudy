import uuid
from datetime import timedelta

from dj_rest_auth.registration.serializers import (
    SocialLoginSerializer,
)
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.db.models.functions import Lower
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.utils import timezone
from jwt import PyJWTError
from ninja.errors import AuthenticationError
from ninja_extra import (
    api_controller,
    http_post,
    http_get,
)
from ninja import Schema, ModelSchema
from django.core.exceptions import ValidationError
from ninja_extra.permissions import IsAuthenticated
from ninja_jwt.tokens import RefreshToken

from common.slack import NotificationClient, Notification, NotificationType
from common.validators.email import is_business_email
from crm.models import Buyer
from software_requests.models import Request
from users.auth import CustomJwtAuth
from ninja_simple_jwt.jwt.token_operations import (
    get_refresh_token_for_user,
    get_access_token_for_user,
    get_access_token_from_refresh_token,
)

from common.api.schemas import BadRequestSchema

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

from users.domains import LoginWithEmailRequestSchema
from users.models import User, MagicToken


class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = "__all__"


class RegisterSchema(Schema):
    email: str
    name: str
    password: str
    confirm_password: str


class LoginSchema(Schema):
    email: str
    password: str


class TokenPairSchema(Schema):
    access: str
    refresh: str


class RefreshTokenRequestSchema(Schema):
    refresh: str


class GoogleTokenSchema(Schema):
    access_token: str


class CreateUnverifiedUserSchema(Schema):
    email: str


class MagicTokenSchema(Schema):
    token: uuid.UUID
    password: str
    confirm_password: str


class LoginWithEmailResponseSchema(Schema):
    success: bool


@api_controller("/auth", tags=["auth"])
class AuthController:
    users = get_user_model()
    login_backend = "users.backends.EmailBackend"

    def __init__(self, notification_client: NotificationClient | None = None):
        self._notifications = notification_client or NotificationClient()

    @http_post(
        "/token/refresh/",
        auth=None,
        response={200: TokenPairSchema, 400: BadRequestSchema},
    )
    def refresh(self, payload: RefreshTokenRequestSchema):
        payload_data = payload.dict()
        try:
            access_token, _ = get_access_token_from_refresh_token(
                payload_data["refresh"]
            )
        except PyJWTError:
            raise AuthenticationError()

        return {"access": access_token, "refresh": payload.refresh}

    @http_get(
        "/me/",
        auth=CustomJwtAuth(),
        permissions=[IsAuthenticated()],
        response={200: UserSchema},
    )
    def me(self, request):
        return UserSchema.from_orm(request.user)

    @http_post(
        "/magic-token/{uuid:token}/login/",
        response={200: TokenPairSchema, 400: BadRequestSchema},
    )
    def login_via_token(self, request: HttpRequest, token: uuid.UUID):
        token = get_object_or_404(
            MagicToken.objects.filter(expires_at__gt=timezone.now(), used=False),
            token=token,
        )

        user = token.user

        # every time a user logs in, try to claim any requests they've made
        # with their email address
        buyer, _ = Buyer.objects.get_or_create(
            user=user, defaults=dict(company_name="Not set")
        )
        # claim requests for initial email
        Request.objects.filter(initial_email__iexact=user.email).update(
            buyer=buyer,
        )
        user.requires_activation = False
        user.save()
        token.used = True
        token.save()

        refresh_token, _ = get_refresh_token_for_user(user)
        access_token, _ = get_access_token_for_user(user)
        return {"refresh": refresh_token, "access": access_token}

    @http_post(
        "/login-with-email/",
        response={200: LoginWithEmailResponseSchema, 400: BadRequestSchema},
    )
    def login_with_email(
        self, request: HttpRequest, payload: LoginWithEmailRequestSchema
    ):
        user = (
            User.objects.annotate(lower_email=Lower("email"))
            .filter(lower_email=payload.email.lower())
            .first()
        )

        notification_type = NotificationType.EXISTING_USER_LOGIN
        if not user:
            try:
                validate_email(payload.email)
            except ValidationError:
                return 400, BadRequestSchema(
                    error_code="INVALID_EMAIL",
                    error_message="You must supply a valid email address.",
                )

            if not is_business_email(payload.email):
                return 400, BadRequestSchema(
                    error_code="PERSONAL_EMAIL_DETECTED",
                    error_message="You must use a business email.",
                )

            user = self.users.objects.create(
                email=payload.email,
                username=payload.email,  # Using email as the username
                name="",
                password=make_password(None),
                requires_activation=True,
            )
            notification_type = NotificationType.NEW_USER_LOGIN

        token = MagicToken.objects.create(
            user=user, expires_at=timezone.now() + timedelta(days=1)
        )

        result = self._notifications.send_notification(
            Notification(
                email_address=user.email,
                notification_type=notification_type,
                additional_context={"token": token.token, "redirect": payload.redirect},
            )
        )

        return {"success": result}


class CustomSerializer(SocialLoginSerializer):
    def to_representation(self, instance: RefreshToken):
        return dict(access=str(instance.access_token), refresh=str(instance))


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000"
    client_class = OAuth2Client

    def get_response_serializer(self):
        return CustomSerializer
