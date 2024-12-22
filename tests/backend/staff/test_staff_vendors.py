from tests.factories.user import UserFactory
from tests.utils import APITestCase


class TestStaffVendorsAPI(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory(is_superuser=True, is_staff=True)
        self.authenticate(self.user)

    def test_create_vendor(self):
        pass
