from ninja_extra import NinjaExtraAPI

from common.api.renderers import CustomJsonRenderer
from software_requests.views.proposal_responses import ProposalResponsesController
from software_requests.views.proposals import ProposalsController
from software_requests.views.requests import SoftwareRequestController
from staff.views.categories import StaffCategoryController
from staff.views.proposals import StaffProposalController
from staff.views.requests import StaffRequestController
from staff.views.vendors import StaffVendorsController
from staff.views.sellers import StaffSellersController
from users.auth import CustomJwtAuth
from users.views import AuthController
from vendors.views import VendorController

api = NinjaExtraAPI(csrf=False, renderer=CustomJsonRenderer(), auth=CustomJwtAuth(optional=True))

# begin register controllers #
api.register_controllers(
    AuthController,
    ProposalsController,
    ProposalResponsesController,
    SoftwareRequestController,
    VendorController,
    StaffVendorsController,
    StaffVendorsController,
    StaffCategoryController,
    StaffSellersController,
    StaffProposalController,
    StaffRequestController,
)
# end register controllers #
