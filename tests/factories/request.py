import random

import factory
from decimal import Decimal

from software_requests.constants import (
    ProposalStatus,
    MaterialType,
    BuyerProposalResponseStatus,
)
from software_requests.models import (
    Request,
    Requirement,
    Proposal,
    ProposalMaterial,
    Referral,
    ImplementationStep,
    VendorRequestMatch,
    ProposalImplementationDetails,
    ProposalPlanDetails,
    ProposalPricing,
    BuyerProposalResponse,
    KeyAdvantage,
)
from tests.factories.crm_data import BuyerFactory, SellerFactory
from tests.factories.util import FileUploadFactory
from tests.factories.vendor import CategoryFactory, VendorFactory
from vendors.constants import VendorImplementationRangeType, PricingCadence


class RequirementFactory(factory.django.DjangoModelFactory):
    requirement_type = factory.Faker("pystr")
    requirement_value = factory.LazyAttribute(lambda o: o.fallback_values.split(" "))

    class Params:
        fallback_values = factory.Faker("sentence", nb_words=4)

    class Meta:
        model = Requirement


class RequestFactory(factory.django.DjangoModelFactory):
    description = factory.Faker("sentence", nb_words=100)
    attachment = factory.SubFactory(FileUploadFactory)
    category = factory.SubFactory(CategoryFactory)
    requirements = factory.RelatedFactoryList(RequirementFactory, size=5)
    buyer = factory.SubFactory(BuyerFactory)

    @factory.post_generation
    def matched_vendors(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for v in extracted:
                self.matched_vendors.add(v)

    @factory.post_generation
    def specified_vendors(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for v in extracted:
                self.specified_vendors.add(v)

    @factory.post_generation
    def requirements(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for r in extracted:
                self.requirements.add(r)

    class Meta:
        model = Request


class VendorRequestMatchFactory(factory.django.DjangoModelFactory):
    request = factory.SubFactory(RequestFactory)
    vendor = factory.SubFactory(VendorFactory)
    reason = factory.Faker("sentence", nb_words=50)

    @factory.post_generation
    def matched_requirements(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for r in extracted:
                self.matched_requirements.add(r)

    class Meta:
        model = VendorRequestMatch


class ProposalFactory(factory.django.DjangoModelFactory):
    request = factory.SubFactory(RequestFactory)
    title = factory.Faker("sentence", nb_words=12)
    status = factory.LazyFunction(lambda: random.choice(ProposalStatus.values))
    submitter = factory.SubFactory(SellerFactory)

    # Descriptive Fields
    summary = factory.Faker("sentence", nb_words=100)
    why_choose_us = factory.Faker("sentence", nb_words=100)
    additional_info = factory.Faker("sentence", nb_words=30)
    implementation_details = factory.RelatedFactory(
        "tests.factories.request.ProposalImplementationDetailsFactory",
        factory_related_name="proposal",
    )
    pricing = factory.RelatedFactory(
        "tests.factories.request.ProposalPricingFactory",
        factory_related_name="proposal",
    )
    plan = factory.RelatedFactory(
        "tests.factories.request.ProposalPlanDetailsFactory",
        factory_related_name="proposal",
    )

    # Relationships
    vendor = factory.SelfAttribute("submitter.vendor")

    @factory.post_generation
    def materials(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for r in extracted:
                self.materials.add(r)

    @factory.post_generation
    def referrals(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for r in extracted:
                self.referrals.add(r)

    @factory.post_generation
    def implementation_steps(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for r in extracted:
                self.implementation_steps.add(r)

    class Meta:
        model = Proposal


class ProposalMaterialFactory(factory.django.DjangoModelFactory):
    material_name = factory.Faker("pystr")
    material_type = factory.LazyFunction(
        lambda: random.choice([m[0] for m in MaterialType.choices])
    )
    material_link = factory.Faker("url")

    class Meta:
        model = ProposalMaterial


class ReferralFactory(factory.django.DjangoModelFactory):
    reference_company_name = factory.Faker("company")
    reference_customer_name = factory.Faker("name")
    reference_customer_job_title = factory.Faker("pystr")
    reference_quote = factory.Faker("sentence", nb_words=100)
    company_logo = factory.SubFactory(FileUploadFactory)

    class Meta:
        model = Referral


class ImplementationStepFactory(factory.django.DjangoModelFactory):
    order = factory.Sequence(lambda n: abs(n) + 1)
    title = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("sentence", nb_words=50)

    class Meta:
        model = ImplementationStep


class ProposalImplementationDetailsFactory(factory.django.DjangoModelFactory):
    proposal = factory.SubFactory(ProposalFactory, implementation_details=None)
    units = factory.LazyFunction(lambda: random.randint(1, 5))
    range_type = factory.LazyFunction(
        lambda: random.choice([i[0] for i in VendorImplementationRangeType.choices])
    )
    additional_details = factory.Faker("sentence", nb_words=20)

    class Meta:
        model = ProposalImplementationDetails


class ProposalPricingFactory(factory.django.DjangoModelFactory):
    proposal = factory.SubFactory(ProposalFactory, pricing=None)
    price = factory.LazyFunction(lambda: Decimal(random.randint(100, 500000)))
    cadence = factory.LazyFunction(
        lambda: random.choice([i[0] for i in PricingCadence.choices])
    )
    additional_details = factory.Faker("sentence", nb_words=20)

    class Meta:
        model = ProposalPricing


class ProposalPlanDetailsFactory(factory.django.DjangoModelFactory):
    proposal = factory.SubFactory(ProposalFactory, plan=None)
    plan_name = factory.LazyFunction(
        lambda: random.choice(
            ["Pro Plan", "Enterprise Plan", "Power Plan", "Starter Plan", "Custom Plan"]
        )
    )
    headline = factory.Faker("sentence", nb_words=5)
    additional_details = factory.Faker("sentence", nb_words=20)

    class Meta:
        model = ProposalPlanDetails


class BuyerProposalResponseFactory(factory.django.DjangoModelFactory):
    proposal = factory.SubFactory(ProposalFactory)
    status = factory.LazyFunction(
        lambda: random.choice([m[0] for m in BuyerProposalResponseStatus.choices])
    )
    reason = factory.Faker("sentence", nb_words=12)
    reason_choices = ["Affordability", "Implementation timeline"]

    class Meta:
        model = BuyerProposalResponse


class KeyAdvantageFactory(factory.django.DjangoModelFactory):
    proposal = factory.SubFactory(ProposalFactory)
    order = factory.Sequence(lambda i: i)
    content = factory.Faker("sentence", nb_words=20)

    class Meta:
        model = KeyAdvantage
