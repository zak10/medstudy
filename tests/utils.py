from ninja_simple_jwt.jwt.token_operations import get_access_token_for_user
from rest_framework.test import APITestCase as BaseTestCase

from users.models import User


class APITestCase(BaseTestCase):
    def authenticate(self, user: User) -> None:
        token, _ = get_access_token_for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def unauthenticate(self):
        self.client.credentials()
