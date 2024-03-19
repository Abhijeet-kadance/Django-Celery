from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from django_celery_project import settings

# import logging

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    print("Inside Send Mail function....")
    for user in users:
        mail_subject = 'Hi! Celery Testing'
        message = "If you are liking my Content. Do subscribe my channel.." 
        print(user.email)
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email='abhijeett@cdac.in',
            recipient_list=[to_email],
            fail_silently=True,
            )  
    return "Done"

# logger = logging.getLogger(__name__)

# @shared_task(bind=True)
# def send_mail_func(self):
#     users = get_user_model().objects.all()
#     logger.info("Inside Send Mail function....")
#     for user in users:
#         mail_subject = 'Hi! Celery Testing'
#         message = "If you are liking my Content. Do subscribe my channel.." 
#         logger.info(user.email)
#         to_email = user.email
#         send_mail(
#             subject=mail_subject,
#             message=message,
#             from_email='abhijeet.kadance.96@gmail.com',
#             recipient_list=[to_email],
#             fail_silently=True,
#         )  
#     return "Done"