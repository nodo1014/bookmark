import os
import sys

path = "/home/jamukha/bookmark"

if path not in sys.path:
    sys.path.append(path)

from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = StaticFilesHandler(get_wsgi_application())
