from django.db.models import QuerySet
from ninja_extra import ModelControllerBase


class ModelViewSet(ModelControllerBase):
    queryset: QuerySet
