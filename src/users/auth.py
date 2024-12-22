import os
from io import StringIO

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from jwt import PyJWTError, DecodeError
from ninja.errors import AuthenticationError
from ninja.security import HttpBearer
from ninja_simple_jwt.jwt.token_operations import decode_token, TokenTypes
from ninja_simple_jwt.settings import ninja_simple_jwt_settings
from typing import IO, Any, Optional

from django.core.files.storage import Storage

from users.models import User


class CustomJwtAuth(HttpBearer):
    def __init__(self, optional: bool = False):
        self.optional = optional
        super().__init__()

    def __call__(self, request: HttpRequest) -> Optional[Any]:
        headers = request.headers
        auth_value = headers.get(self.header)
        if not auth_value:
            return AnonymousUser() if self.optional else None
        parts = auth_value.split(" ")

        if parts[0].lower() != self.openapi_scheme:
            return None
        token = " ".join(parts[1:])
        return self.authenticate(request, token)

    def authenticate(self, request: HttpRequest, token: str) -> Any | None:
        token = self.decode_authorization(request.headers["Authorization"])

        try:
            access_token = decode_token(
                token, token_type=TokenTypes.ACCESS, verify=True
            )
        except PyJWTError as e:
            # regardless of optional, if you passed in a token and its expired
            # or invalid (unsigned) we should return a 401
            raise AuthenticationError(e)

        request.user = User.objects.get(pk=access_token["user_id"])

        return True

    @staticmethod
    def set_token_claims_to_user(
        user: AbstractBaseUser | AnonymousUser, token: dict
    ) -> None:
        for (
            claim,
            user_attribute,
        ) in ninja_simple_jwt_settings.TOKEN_CLAIM_USER_ATTRIBUTE_MAP.items():
            if isinstance(user_attribute, str):
                setattr(user, user_attribute, token.get(claim))
            else:
                setattr(user, claim, token.get(claim))

    def decode_authorization(self, value: str) -> str:
        parts = value.split(" ")
        if len(parts) != 2 or parts[0].lower() != "bearer":
            raise DecodeError("Invalid Authorization header")

        token = parts[1]
        return token


class OptionalCustomJwtAuth(CustomJwtAuth):
    optional: bool = True


class EnvVarStorage(Storage):
    def _save(self, name: str, content: IO) -> str:
        raise NotImplementedError

    def exists(self, name: str) -> bool:
        """Always overwrite old keys with same filename."""
        return False

    def _open(self, name: str, mode: str = "rb") -> IO:
        if name == "jwt-signing.pem":
            name = "JWT_PRIVATE_KEY"
        elif name == "jwt-signing.pub":
            name = "JWT_PUBLIC_KEY"
        return StringIO(os.getenv(name))  # pylint: disable=unspecified-encoding


env_var_storage = EnvVarStorage()
