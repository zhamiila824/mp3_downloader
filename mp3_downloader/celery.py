from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mp3_downloader.settings')
app = Celery('mp3_downloader')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
