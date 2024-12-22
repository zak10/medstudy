import random

import factory

from tests.factories.user import UserFactory
from utils.constants import FileUploadType
from utils.models import FileUpload


class FileUploadFactory(factory.django.DjangoModelFactory):
    file = factory.django.FileField(file_name="test.txt", data=b"Test Content")
    upload_type = factory.LazyFunction(
        lambda: random.choice([m[0] for m in FileUploadType.choices])
    )
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = FileUpload
