from __future__ import absolute_import

from celery import shared_task

@shared_task  # Use this decorator to make this a asynchronous function
def send_notification(task_id):
    # send_mail(task_id)
    pass


@shared_task
def adding_task(x, y):
    return x + y