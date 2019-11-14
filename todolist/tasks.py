from __future__ import absolute_import

from celery import shared_task

from todolist.services import Notifier


@shared_task # Use this decorator to make this a asynchronous function
def adding_task(cat_id):
    Notifier.auto_task(cat_id)