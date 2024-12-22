from tests.factories.crm_data import SellerFactory
from tests.factories.request import (
    RequestFactory,
    ProposalFactory,
)
from tests.factories.user import UserFactory
from tests.factories.util import FileUploadFactory
from tests.utils import APITestCase
from software_requests.constants import (
    ProposalStatus,
)
from utils.constants import FileUploadType
from vendors.constants import EmbeddedContentType


class TestProposalsAPI(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.seller = SellerFactory(user=self.user)
        self.authenticate(self.user)
        self.request = RequestFactory()

    def test_must_be_authenticated(self):
        self.unauthenticate()
        response = self.client.post(
            "/api/proposals/",
            {
                "description": "Test proposal",
            },
            format="json",
        )

        assert response.status_code == 401

    def test_create_proposal_succeeds(self):
        f = FileUploadFactory(user=self.user, upload_type=FileUploadType.LOGO)
        response = self.client.post(
            "/api/proposals/",
            {
                "request_id": self.request.id,
                "vendor_id": self.seller.vendor_id,
                "materials": [
                    {
                        "type": EmbeddedContentType.DEMO,
                        "title": "A cool demo",
                        "link": "http://sheppard.info/",
                        "description": "A description of the demo",
                        "date": "2024-10-20",
                    }
                ],
                "key_advantages": [
                    {"order": 2, "content": "This is the second advantage"},
                    {"order": 1, "content": "This is the first advantage"},
                ],
                "referrals": [
                    {
                        "reference_company_name": "Espinoza Inc",
                        "reference_customer_name": "Robert West",
                        "reference_customer_job_title": "AQBmXetqWGWHYKKgTpnX",
                        "reference_quote": "Stand method management reason star actually far fire bag reveal religious himself than develop choice name successful current once Republican meeting nearly without listen environmental for wind writer official mean me her newspaper out Democrat stand sense must activity whatever between however brother hotel moment herself than design sister key space paper whatever allow most mouth economic say here station never pay worry everybody scene future west hand pick job almost hard amount become hold economic seek bed daughter use father line administration discover detail of outside under store soon perform their since professional green home fly order western must over special fall huge send politics billion professional tend store professor television himself might talk hour he teacher nice control art visit parent capital amount especially.",
                        "company_logo_id": f.id,
                    }
                ],
                "implementation_steps": [
                    {
                        "order": 2,
                        "title": "Onboarding Call 2",
                        "description": "Talk to us on zoom",
                    },
                    {
                        "order": 1,
                        "title": "Onboarding Call 1",
                        "description": "Talk to us on phone",
                    },
                ],
                "implementation_details": {
                    "units": 2,
                    "range_type": "HOURS",
                    "additional_details": "Represent another sell occur morning voice ball issue score work themselves past.",
                },
                "pricing": {
                    "price": "326758.00",
                    "cadence": "ANNUALLY",
                    "additional_details": "Democrat kitchen decision win perhaps drive positive start rule everybody per traditional.",
                },
                "plan": {
                    "plan_name": "Starter Plan",
                    "headline": "Program this we need.",
                    "additional_details": "Free news point painting material simply explain create audience bed increase hear performance guess process million serve allow nor reflect back whom.",
                },
                "title": "Proposal title",
                "summary": "A longer summary of the proposal",
                "why_choose_us": "We are simply the best",
                "additional_info": "Some more info",
            },
            format="json",
        )

        data = response.json()
        assert response.status_code == 200
        assert data["title"] == "Proposal title"
        assert len(data["implementation_steps"]) == 2

        assert data["implementation_details"]["id"] is not None
        assert data["implementation_details"]["units"] == 2
        assert data["implementation_details"]["range_type"] == "HOURS"

        assert data["pricing"]["id"] is not None
        assert data["pricing"]["price"] == "326758.00"

        assert data["plan"]["id"] is not None
        assert data["plan"]["plan_name"] == "Starter Plan"
        assert data["plan"]["headline"] == "Program this we need."

        assert len(data["key_advantages"]) == 2

    def test_submit_proposal(self):
        proposal = ProposalFactory(
            submitter=self.seller, status=ProposalStatus.IN_PROGRESS
        )

        response = self.client.post(f"/api/proposals/{proposal.id}/submit/")

        assert response.status_code == 200
        assert response.json()["status"] == ProposalStatus.SUBMITTED
