from django.db import models
from model_utils.models import TimeStampedModel

from utils.constants import FileUploadType


def uuid_generator():
    from uuid_extensions import uuid7

    return uuid7()


class BaseModel(TimeStampedModel):
    id = models.UUIDField(
        default=uuid_generator, primary_key=True, null=False, blank=False
    )

    class Meta:
        abstract = True


class FileUpload(BaseModel):
    file = models.FileField(upload_to="user_uploads/")
    upload_type = models.TextField(
        choices=FileUploadType.choices, default=FileUploadType.RFP
    )
    user = models.ForeignKey(
        "users.User", related_name="uploads", on_delete=models.CASCADE, null=True
    )
