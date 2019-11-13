from __future__ import absolute_import

from celery import shared_task

from todolist.models import Category, Task


@shared_task  # Use this decorator to make this a asynchronous function
def send_notification(task_id):
    # send_mail(task_id)
    pass


@shared_task
def adding_task(cat_id):
    Task.objects.create(description="auto generated", start_date="2019-11-13 23:23", category_id=cat_id)