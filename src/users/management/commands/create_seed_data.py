import os
import random
from decimal import Decimal

import requests
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

from crm.models import Buyer
from scraping.g2 import parse_search_page, parse_search_page_two
from software_requests.constants import ProposalStatus
from software_requests.models import Request
from tests.factories.crm_data import SellerFactory, BuyerFactory
from tests.factories.request import (
    RequestFactory,
    RequirementFactory,
    VendorRequestMatchFactory,
    ProposalFactory,
    ReferralFactory,
    ImplementationStepFactory,
    KeyAdvantageFactory,
)
from tests.factories.vendor import (
    VendorFactory,
    BestForItemFactory,
    IntegrationFactory,
    EmbeddedContentFactory,
    ComplianceCertificationFactory,
    ProConFactory,
)
from users.models import User
from vendors.constants import (
    VendorImplementationRangeType,
    PricingCadence,
    PricingPer,
)
from vendors.models import (
    Vendor,
    ImplementationRange,
    PricingRange,
    Category,
    Integration,
)
from vendors.services import VendorImporter


class Command(BaseCommand):
    # Idempotently create sites for localhost and staging and add
    # the google socialapp
    def handle(self, *args, **options):
        self._create_google_oauth_app()
        self._create_users()
        self._import_vendors()
        # self._create_vendors()
        # self._create_vendors_from_data()
        self._create_random_requests()
        self._create_random_proposals()

    def _create_google_oauth_app(self):
        Site.objects.get_or_create(domain="http://localhost", name="localhost")
        Site.objects.get_or_create(domain="https://zk.fly.dev", name="staging")
        app, _ = SocialApp.objects.get_or_create(
            provider="google",
            client_id=settings.GOOGLE_OAUTH_CLIENT_ID,
            secret=settings.GOOGLE_OAUTH_SECRET,
        )

        app.sites.set(Site.objects.all())

    def _import_vendors(self):
        service = VendorImporter()
        service.import_vendors("data/vendors.csv")

    def _create_random_requests(self):
        category = Category.objects.get(name="Data Enrichment")
        zach = Buyer.objects.filter(user__email="zach@usearena.com").first()
        if not zach:
            zach = BuyerFactory(user=User.objects.get(email="zach@usearena.com"))
        for i in range(1, 10):
            requirements = RequirementFactory.create_batch(size=random.randint(6, 10))
            request = RequestFactory(
                buyer=zach,
                category=category,
                requirements=requirements,
                matched_vendors=list(
                    Vendor.objects.order_by("?")[: random.randint(2, 4)]
                ),
                specified_vendors=list(
                    Vendor.objects.order_by("?")[: random.randint(4, 11)]
                ),
            )
            for j in range(1, random.randint(4, 11)):
                VendorRequestMatchFactory(
                    request=request,
                    vendor=Vendor.objects.order_by("?").first(),
                    matched_requirements=random.choices(
                        requirements,
                        k=random.randint(len(requirements) - 2, len(requirements)),
                    ),
                )

    def _create_random_proposals(self):
        requests = Request.objects.all()

        def get_proposal_status(i: int):
            if i % 4 == 0:
                return ProposalStatus.IN_PROGRESS
            elif i % 3 == 0:
                return ProposalStatus.REJECTED
            else:
                return ProposalStatus.SUBMITTED

        for request in requests:
            for i in range(1, 8):
                seller = SellerFactory(vendor=Vendor.objects.order_by("?").first())
                p = ProposalFactory(
                    request=request,
                    submitter=seller,
                    materials=EmbeddedContentFactory.create_batch(
                        size=random.randint(1, 5)
                    ),
                    status=get_proposal_status(i),
                    referrals=ReferralFactory.create_batch(size=random.randint(1, 5)),
                    implementation_steps=ImplementationStepFactory.create_batch(
                        size=random.randint(3, 6)
                    ),
                )
                KeyAdvantageFactory.create_batch(size=random.randint(3, 5), proposal=p)

    def _create_users(self):
        for email in [
            "zach@usearena.com",
            "austin@usearena.com",
            "michael@usearena.com",
        ]:
            if not User.objects.filter(email=email).exists():
                User.objects.create_superuser(
                    email=email,
                    username=email,
                    password=email,
                )
