from django.http import HttpRequest
from ninja import UploadedFile, File
from ninja_extra import api_controller, http_post

from common.api.schemas import BadRequestSchema

from utils.constants import FileUploadType
from utils.domains.file import FileUploadSchema
from utils.services.files import FileService


@api_controller("/files", tags=["software-requests"])
class FilesController:
    service = FileService()

    @http_post("/", response={200: FileUploadSchema, 400: BadRequestSchema})
    def upload_file(
        self,
        request: HttpRequest,
        upload_type: FileUploadType,
        file: UploadedFile = File(...),
    ):
        return self.service.upload_file(
            file=file, upload_type=upload_type, user=request.user
        )
