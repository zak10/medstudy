from django.db.models import TextChoices


class FileUploadType(TextChoices):
    RFP = "RFP"
    PROPOSAL = "PROPOSAL"
    LOGO = "LOGO"
