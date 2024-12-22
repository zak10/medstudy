import uuid

from django.core.files import File
from django.core.files.base import ContentFile

from users.models import User
from utils.constants import FileUploadType
from utils.models import FileUpload


class FileService:
    def upload_file(
        self, file: File, upload_type: FileUploadType, user: User | None
    ) -> FileUpload:
        # todo: validations based on type
        # todo: rate limiting
        upload = FileUpload(
            upload_type=upload_type,
        )
        if user and not user.is_anonymous:
            upload.user = user
        upload.file.save(
            str(uuid.uuid4()) + "/" + file.name, content=ContentFile(file.read())
        )
        upload.save()

        return upload

    def link_rfp_upload(self, request_id: uuid.UUID, user: User):
        pass
