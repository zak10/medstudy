from ninja_simple_jwt.jwt.token_operations import decode_token, TokenTypes

from crm.models import Buyer
from tests.factories.request import RequestFactory
from tests.factories.user import MagicTokenFactory
from tests.utils import APITestCase
from users.models import MagicToken


class TestUsersAPI(APITestCase):
    def test_token_refresh_bad_token(self):
        response = self.client.post(
            "/api/auth/token/refresh/", {"refresh": ""}, format="json"
        )

        assert response.status_code == 401

    def test_token_refresh_succeeds(self):
        t = MagicTokenFactory()
        response = self.client.post(
            f"/api/auth/magic-token/{t.token}/login/",
            format="json",
        )

        refresh = response.json()["refresh"]

        response = self.client.post(
            "/api/auth/token/refresh/", {"refresh": refresh}, format="json"
        )
        data = response.json()

        assert response.status_code == 200
        access_token = decode_token(
            data["access"], token_type=TokenTypes.ACCESS, verify=True
        )

        assert access_token["user_id"] == str(t.user.id)
        assert access_token["is_staff"] == t.user.is_staff
        assert access_token["email"] == t.user.email
        assert access_token["name"] == t.user.name
        assert access_token["is_superuser"] == t.user.is_superuser

    def test_login_with_email_flow_create(self):
        assert MagicToken.objects.count() == 0
        response = self.client.post(
            "/api/auth/login-with-email/", {"email": "zach@usearena.com"}, format="json"
        )
        assert Buyer.objects.count() == 0
        assert response.status_code == 200
        assert response.json()["success"]

        token = MagicToken.objects.first()
        assert token is not None

        login_response = self.client.post(
            f"/api/auth/magic-token/{token.token}/login/", format="json"
        )

        assert login_response.status_code == 200
        assert "access" in login_response.json()
        assert "refresh" in login_response.json()
        assert Buyer.objects.count() == 1

    def test_login_with_email_flow_invalid_email(self):
        assert MagicToken.objects.count() == 0
        response = self.client.post(
            "/api/auth/login-with-email/", {"email": "zach"}, format="json"
        )
        assert Buyer.objects.count() == 0
        assert response.status_code == 400
        assert response.json()["error_code"] == "INVALID_EMAIL"

    def test_login_with_email_flow_personal_email(self):
        assert MagicToken.objects.count() == 0
        response = self.client.post(
            "/api/auth/login-with-email/", {"email": "zach@gmail.com"}, format="json"
        )
        assert Buyer.objects.count() == 0
        assert response.status_code == 400
        assert response.json()["error_code"] == "PERSONAL_EMAIL_DETECTED"

    def test_login_with_email_flow_claims_requests(self):
        r = RequestFactory(initial_email="zach@usearena.com", buyer=None)
        response = self.client.post(
            "/api/auth/login-with-email/", {"email": "zach@usearena.com"}, format="json"
        )
        assert Buyer.objects.count() == 0
        assert response.status_code == 200
        assert response.json()["success"]

        token = MagicToken.objects.first()
        assert token is not None

        login_response = self.client.post(
            f"/api/auth/magic-token/{token.token}/login/", format="json"
        )

        assert login_response.status_code == 200
        assert "access" in login_response.json()
        assert "refresh" in login_response.json()
        assert Buyer.objects.count() == 1
        r.refresh_from_db()
        assert r.buyer.user.email == "zach@usearena.com"
