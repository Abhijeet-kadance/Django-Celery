from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
def test(request):
    # test_func.delay()
    return HttpResponse("Done")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=12, minute=31)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"1", task='send_mail_app.tasks.send_mail_func')
    return HttpResponse("Done")