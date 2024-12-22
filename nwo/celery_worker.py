import os
import sys

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nwo.settings")
from django.conf import settings

sys.path.append(os.path.join(settings.BASE_DIR, "src"))
app = Celery("nwo")
app.config_from_object("django.conf:settings", namespace="CELERY")
from django.apps import apps

app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
