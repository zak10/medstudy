import datetime
import random
from decimal import Decimal
import factory

from software_requests.constants import ProConType
from vendors.constants import (
    VendorImplementationRangeType,
    PricingCadence,
    PricingPer,
    EmbeddedContentType,
    RelativePricingType,
)
from vendors.models import (
    Vendor,
    Category,
    BestForItem,
    EmbeddedContent,
    Integration,
    ImplementationRange,
    PricingRange,
    ProCon,
    ComplianceCertification,
)


class ImplementationRangeFactory(factory.django.DjangoModelFactory):
    lower_bound = factory.LazyFunction(lambda: random.randint(1, 2))
    upper_bound = factory.LazyFunction(lambda: random.randint(3, 5))
    range_type = factory.LazyFunction(
        lambda: random.choice(
            [item[0] for item in VendorImplementationRangeType.choices]
        )
    )

    class Meta:
        model = ImplementationRange


class PricingRangeFactory(factory.django.DjangoModelFactory):
    lower_bound = factory.LazyFunction(
        lambda: random.choice([Decimal("10"), Decimal("20"), Decimal("50")])
    )
    upper_bound = factory.LazyFunction(
        lambda: random.choice([Decimal("100"), Decimal("200"), Decimal("500")])
    )
    cadence = factory.LazyFunction(
        lambda: random.choice([item[0] for item in PricingCadence.choices])
    )
    per = factory.LazyFunction(
        lambda: random.choice([item[0] for item in PricingPer.choices])
    )

    class Meta:
        model = PricingRange


class VendorFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("company")
    description = factory.Faker("sentence", nb_words=200)
    relative_pricing = factory.LazyFunction(
        lambda: random.choice([p[0] for p in RelativePricingType.choices])
    )
    website = factory.Faker("url")
    rating = factory.LazyFunction(
        lambda: (random.randint(0, 100) / Decimal("10")).quantize(Decimal("0.1"))
    )
    num_reviews = factory.LazyFunction(lambda: random.randint(100, 10000))
    image = factory.LazyFunction(lambda: f"{random.randint(1, 10)}.png")

    implementation_range = factory.SubFactory(ImplementationRangeFactory)
    pricing_range = factory.SubFactory(PricingRangeFactory)
    best_for = factory.Faker("sentence", nb_words=100)

    @factory.post_generation
    def best_for_items(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for b in extracted:
                self.best_for_items.add(b)

    @factory.post_generation
    def embedded_contents(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for e in extracted:
                self.embedded_contents.add(e)

    @factory.post_generation
    def integrations(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for i in extracted:
                self.integrations.add(i)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for category in extracted:
                self.categories.add(category)

    class Meta:
        model = Vendor


class ProConFactory(factory.django.DjangoModelFactory):
    vendor = factory.SubFactory(VendorFactory)
    type = factory.LazyFunction(
        lambda: random.choice([p[0] for p in ProConType.choices])
    )
    value = factory.Faker("sentence", nb_words=8)

    class Meta:
        model = ProCon


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("sentence", nb_words=2)

    class Meta:
        model = Category


class BestForItemFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("sentence", nb_words=4)

    class Meta:
        model = BestForItem


class ComplianceCertificationFactory(factory.django.DjangoModelFactory):
    vendor = factory.SubFactory(VendorFactory)
    type = factory.LazyFunction(lambda: random.choice(["GDPR", "SOC II"]))
    latest_certification_date = factory.LazyFunction(
        lambda: datetime.date.today() - datetime.timedelta(days=100)
    )

    class Meta:
        model = ComplianceCertification


class EmbeddedContentFactory(factory.django.DjangoModelFactory):
    type = factory.LazyFunction(
        lambda: random.choice([e[0] for e in EmbeddedContentType.choices])
    )
    link = factory.Faker("url")
    title = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("sentence", nb_words=50)
    date = factory.LazyFunction(
        lambda: datetime.date.today() - datetime.timedelta(days=100)
    )

    class Meta:
        model = EmbeddedContent


class IntegrationFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("company")
    description = factory.Faker("sentence", nb_words=20)

    class Meta:
        model = Integration
