import factory

from crm.models import Buyer, Seller
from tests.factories.user import UserFactory
from tests.factories.vendor import VendorFactory


class BuyerFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    company_name = factory.Faker("company")

    class Meta:
        model = Buyer


class SellerFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    vendor = factory.SubFactory(VendorFactory)

    class Meta:
        model = Seller
