from tests.factories.request import (
    ProposalFactory,
    BuyerProposalResponseFactory,
)
from tests.factories.user import UserFactory
from tests.utils import APITestCase
from software_requests.constants import (
    BuyerProposalResponseStatus,
    ProposalStatus,
)


class TestProposalResponsesAPI(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.proposal = ProposalFactory(request__buyer__user=self.user)
        self.authenticate(self.user)

    def test_create_response_bad_request(self):
        response = self.client.post(
            "/api/responses/",
            {
                "description": "Test proposal",
            },
            format="json",
        )
        assert response.status_code == 422

    def test_create_response_succeeds(self):
        response = self.client.post(
            "/api/responses/",
            {
                "proposal_id": self.proposal.id,
                "status": BuyerProposalResponseStatus.REJECTED,
                "reason": "It costs too much",
                "reason_choices": ["Affordability", "Implementation", "Other issues"],
            },
            format="json",
        )
        assert response.status_code == 200

    def test_create_response_must_be_owner(self):
        proposal = ProposalFactory(request__buyer__user=UserFactory())  # anyone else
        response = self.client.post(
            "/api/responses/",
            {
                "proposal_id": proposal.id,
                "status": BuyerProposalResponseStatus.REJECTED,
                "reason": "It costs too much",
                "reason_choices": ["Affordability", "Implementation", "Other issues"],
            },
            format="json",
        )
        assert response.status_code == 404

    def test_create_response_already_responded(self):
        BuyerProposalResponseFactory(proposal=self.proposal)
        response = self.client.post(
            "/api/responses/",
            {
                "proposal_id": self.proposal.id,
                "status": BuyerProposalResponseStatus.REJECTED,
                "reason": "It costs too much",
                "reason_choices": ["Affordability", "Implementation", "Other issues"],
            },
            format="json",
        )
        assert response.status_code == 400
        assert response.json()["error_code"] == "PROPOSAL_ALREADY_RESPONDED"

    def test_create_response_succeeds_and_marks_other_proposals_as_rejected(self):
        proposal_two = ProposalFactory(
            request=self.proposal.request, status=ProposalStatus.SUBMITTED
        )
        response = self.client.post(
            "/api/responses/",
            {
                "proposal_id": self.proposal.id,
                "status": BuyerProposalResponseStatus.ACCEPTED,
                "reason": "It costs too much",
                "reason_choices": ["Affordability", "Implementation", "Other issues"],
            },
            format="json",
        )
        proposal_two.refresh_from_db()
        assert response.status_code == 200
        assert proposal_two.status == ProposalStatus.REJECTED
        assert proposal_two.proposal_response.reason == "Went with another vendor"
