from tests.factories.user import UserFactory
from tests.factories.vendor import VendorFactory, CategoryFactory
from tests.utils import APITestCase
from vendors.constants import VendorCategory


class TestVendorsAPI(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.authenticate(self.user)

    def test_list_no_vendors(self):
        resp = self.client.get(
            "/api/vendors/",
        )

        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 0

    def test_list_no_params(self):
        c = CategoryFactory()
        v = VendorFactory(categories=[c])
        resp = self.client.get(
            "/api/vendors/",
        )

        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 1

        assert data[0]["name"] == v.name
        assert data[0]["categories"][0]["id"] == str(c.id)
        assert data[0]["website"] == v.website

    def test_list_with_category(self):
        erp = CategoryFactory(name="ERP")
        crm = CategoryFactory(name="CRM")
        v1 = VendorFactory(categories=[erp])
        v2 = VendorFactory(categories=[crm])
        resp = self.client.get("/api/vendors/", data={"category": VendorCategory.ERP})

        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 1

        assert data[0]["name"] == v1.name
        assert data[0]["categories"][0]["id"] == str(erp.id)
        assert data[0]["website"] == v1.website

        v2.categories.add(erp)
        resp = self.client.get("/api/vendors/", data={"category": VendorCategory.ERP})

        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 2

    def test_list_with_pagination(self):
        # in alphabetical order, alice should be on first page, bob on second
        erp = CategoryFactory(name="ERP")
        v1 = VendorFactory(categories=[erp], name="alice")
        v2 = VendorFactory(categories=[erp], name="bob")
        resp = self.client.get(
            "/api/vendors/",
            data={"category": VendorCategory.ERP, "page_size": 1, "page_num": 1},
        )

        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 1

        assert data[0]["name"] == v1.name
        assert data[0]["categories"][0]["id"] == str(erp.id)
        assert data[0]["website"] == v1.website

        resp = self.client.get(
            "/api/vendors/",
            data={"category": VendorCategory.ERP, "page_size": 1, "page_num": 2},
        )

        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 1

        assert data[0]["name"] == v2.name
        assert data[0]["categories"][0]["id"] == str(erp.id)
        assert data[0]["website"] == v2.website
