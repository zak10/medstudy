from datetime import timedelta
from typing import Tuple

from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.db.models.functions import Lower
from django.utils import timezone

from common.slack import NotificationType, NotificationClient, Notification
from common.validators.email import is_business_email
from users.exceptions import PersonalEmailUsedException
from users.models import User, MagicToken


class UserService:
    def get_or_create_user(self, unsanitized_email: str) -> Tuple[User, bool]:
        user = (
            User.objects.annotate(lower_email=Lower("email"))
            .filter(lower_email=unsanitized_email.lower())
            .first()
        )
        created = False

        if not user:
            validate_email(unsanitized_email)
            if not is_business_email(unsanitized_email):
                raise PersonalEmailUsedException()

            user = User.objects.create(
                email=unsanitized_email,
                username=unsanitized_email,
                name="",
                password=make_password(None),
                requires_activation=True,
            )
            created = True

        return user, created

    def send_token(
        self, user: User, notification_type: NotificationType, redirect: str = "/app"
    ):
        token = MagicToken.objects.create(
            user=user, expires_at=timezone.now() + timedelta(days=1)
        )

        return NotificationClient().send_notification(
            Notification(
                email_address=user.email,
                notification_type=notification_type,
                additional_context={"token": token.token, "redirect": redirect},
            )
        )
