from django.core.files.uploadedfile import SimpleUploadedFile

from tests.factories.crm_data import BuyerFactory
from tests.factories.request import RequestFactory, RequirementFactory
from tests.factories.user import UserFactory
from tests.factories.vendor import VendorFactory, CategoryFactory
from tests.utils import APITestCase
import uuid


class TestSoftwareRequestsAPI(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.vendor = VendorFactory()
        self.requirement = RequirementFactory()
        self.category = CategoryFactory(name="Data Enrichment")

    def test_get_without_authorization(self):
        request = RequestFactory(
            buyer=None,
        )
        response = self.client.get(f"/api/software-requests/{request.id}/")

        assert response.status_code == 200

    def test_create_request_without_file(self):
        """Test creating a new software request"""
        response = self.client.post(
            "/api/software-requests/",
            {
                "description": "Test proposal",
            },
            format="multipart",
        )

        assert response.status_code == 200
        data = response.json()
        assert data["description"] == "Test proposal"
        assert data["category"]["name"] == self.category.name

    def test_create_request_with_file(self):
        uploaded_file = SimpleUploadedFile("test_file.txt", b"file contents")
        response = self.client.post(
            "/api/software-requests/",
            {"description": "Test proposal", "file": uploaded_file},
            format="multipart",
        )

        assert response.status_code == 200
        data = response.json()
        assert data["description"] == "Test proposal"
        assert data["category"]["name"] == self.category.name

    def test_get_request(self):
        """Test retrieving a specific software request"""
        request = RequestFactory(
            description="Test proposal",
            matched_vendors=[self.vendor],
            specified_vendors=[self.vendor],
            requirements=[self.requirement],
            buyer=None,
        )

        response = self.client.get(f"/api/software-requests/{request.id}/")

        assert response.status_code == 200
        data = response.json()
        assert data["description"] == "Test proposal"
        assert len(data["matched_vendors"]) == 1
        assert len(data["specified_vendors"]) == 1
        assert len(data["requirements"]) == 1

        assert data["matched_vendors"][0]["id"] == str(self.vendor.id)
        assert data["specified_vendors"][0]["id"] == str(self.vendor.id)
        assert data["requirements"][0]["id"] == str(self.requirement.id)

    def test_get_request_404_when_buyer_set(self):
        """Test retrieving a specific software request"""
        request = RequestFactory(description="Test proposal", buyer=BuyerFactory())

        response = self.client.get(f"/api/software-requests/{request.id}/")

        assert response.status_code == 404

    def test_finalize_request(self):
        """Test updating a software request"""
        request = RequestFactory(
            description="Test proposal",
            category=CategoryFactory(name="Cat1"),
            open_to_other_vendors=True,
            buyer=None,
        )

        response = self.client.patch(
            f"/api/software-requests/{request.id}/",
            {"open_to_other_vendors": False, "email": "zach@usearena.com"},
            format="json",
        )
        assert response.status_code == 200
        data = response.json()
        assert data["open_to_other_vendors"] is False

    def test_finalize_request_fails_invalid_email(self):
        """Test updating a software request"""
        request = RequestFactory(
            description="Test proposal",
            category=CategoryFactory(name="Cat1"),
            open_to_other_vendors=True,
            buyer=None,
        )

        response = self.client.patch(
            f"/api/software-requests/{request.id}/",
            {"open_to_other_vendors": False, "email": "zach"},
            format="json",
        )
        assert response.status_code == 400
        data = response.json()
        assert data["error_code"] == "INVALID_EMAIL"

    def test_finalize_request_fails_using_personal_email(self):
        """Test updating a software request"""
        request = RequestFactory(
            description="Test proposal",
            category=CategoryFactory(name="Cat1"),
            open_to_other_vendors=True,
            buyer=None,
        )

        response = self.client.patch(
            f"/api/software-requests/{request.id}/",
            {"open_to_other_vendors": False, "email": "zach@gmail.com"},
            format="json",
        )
        assert response.status_code == 400
        data = response.json()
        assert data["error_code"] == "PERSONAL_EMAIL_DETECTED"

    def test_add_requirement(self):
        """Test adding a requirement to a software request"""
        request = RequestFactory(
            description="Test proposal",
            category=CategoryFactory(),
            buyer=None,
        )

        response = self.client.post(
            f"/api/software-requests/{request.id}/requirements/",
            {"requirement_type": "Integration", "requirement_value": ["AWS"]},
            format="json",
        )

        assert response.status_code == 200
        data = response.json()
        assert len(data["requirements"]) == 1
        assert data["requirements"][0]["requirement_type"] == "Integration"
        assert len(data["requirements"][0]["requirement_value"]) == 1
        assert "AWS" in data["requirements"][0]["requirement_value"]

    def test_remove_requirement(self):
        """Test removing a requirement from a software request"""
        request = RequestFactory(
            description="Test proposal",
            category=CategoryFactory(),
            requirements=[
                RequirementFactory(
                    requirement_type="Integration", requirement_value=["AWS"]
                )
            ],
            buyer=None,
        )

        response = self.client.delete(
            f"/api/software-requests/{request.id}/requirements/{request.requirements.first().id}/"
        )

        assert response.status_code == 200
        data = response.json()
        assert len(data["requirements"]) == 0

    def test_add_vendor_to_arena(self):
        """Test adding a vendor to the request's arena"""
        request = RequestFactory(
            description="Test proposal",
            category=CategoryFactory(),
            buyer=None,
        )

        response = self.client.post(
            f"/api/software-requests/{request.id}/vendors/{self.vendor.id}/"
        )

        assert response.status_code == 200
        data = response.json()
        assert len(data["matched_vendors"]) == 1
        assert data["matched_vendors"][0]["id"] == str(self.vendor.id)

    def test_remove_vendor_from_arena(self):
        """Test removing a vendor from the request's arena"""
        request = RequestFactory(
            description="Test proposal",
            category=CategoryFactory(),
            matched_vendors=[self.vendor],
            buyer=None,
        )

        response = self.client.delete(
            f"/api/software-requests/{request.id}/vendors/{self.vendor.id}/"
        )

        assert response.status_code == 200
        data = response.json()
        assert len(data["matched_vendors"]) == 0

    def test_list_requests_for_user(self):
        """Test listing all requests for a user"""
        buyer = BuyerFactory(user=self.user)
        RequestFactory(
            description="Test proposal 1",
            category=CategoryFactory(),
            buyer=buyer,
        )
        RequestFactory(
            description="Test proposal 2",
            category=CategoryFactory(),
            buyer=buyer,
        )
        self.authenticate(self.user)
        response = self.client.get("/api/software-requests/")

        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2

    def test_list_additional_vendors(self):
        """Test listing additional vendors for a request"""
        category = CategoryFactory(name="CRM")
        v = VendorFactory(categories=[category])
        request = RequestFactory(
            description="Test proposal",
            category=category,
            buyer=None,
        )

        response = self.client.get(
            f"/api/software-requests/{request.id}/vendors/",
            {"page_size": 10, "page_number": 1},
        )

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["id"] == str(v.id)

    def test_invalid_request_id(self):
        """Test accessing a request with an invalid ID"""
        invalid_id = uuid.uuid4()
        response = self.client.get(f"/api/software-requests/{invalid_id}/")
        assert response.status_code == 404
