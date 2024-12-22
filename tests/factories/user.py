import uuid
from datetime import datetime, timedelta

import factory

from users.models import User, MagicToken


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")

    class Meta:
        model = User


class MagicTokenFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory, requires_activation=True)
    token = factory.LazyFunction(lambda: uuid.uuid4())
    expires_at = factory.LazyFunction(lambda: datetime.now() + timedelta(days=30))

    class Meta:
        model = MagicToken
