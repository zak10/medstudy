"""
WSGI config for nwo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nwo.settings")
sys.path.append(os.path.join(settings.BASE_DIR, "src"))

application = get_wsgi_application()
