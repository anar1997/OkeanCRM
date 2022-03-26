from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
import account


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')


app.config_from_object('django.conf:settings')


app.autodiscover_tasks()

app.conf.beat_schedule = {
    "maas_goruntuleme_create_task": {
        "task": "maas_goruntuleme_create_task",
        "schedule": crontab(0,0,'*', day_of_month="1"),
    },
    "maas_goruntuleme_create_task_15": {
        "task": "maas_goruntuleme_create_task_15",
        "schedule": crontab(0,0,'*', day_of_month="15"),
    }
}