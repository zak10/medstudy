from ninja import ModelSchema

from utils.models import FileUpload


class FileUploadSchema(ModelSchema):
    class Meta:
        model = FileUpload
        fields = "__all__"
