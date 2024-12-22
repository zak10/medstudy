from typing import Optional

from django.contrib.auth.backends import ModelBackend
from django.http.request import HttpRequest

from .models import User


class EmailBackend(ModelBackend):
    def authenticate(self, request: HttpRequest, username: Optional[str] = None, password: Optional[str] = None, **kwargs) -> Optional[User]:  # type: ignore
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        else:
            if not password:
                return None
            if user.check_password(password):
                return user
        return None
