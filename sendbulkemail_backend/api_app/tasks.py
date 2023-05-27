from celery import shared_task 
from django.conf import settings
from django.core.mail import send_mass_mail
from .models import *
from time import sleep

@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task(subject,message):
    sleep(10)
    email = UserEmail.objects.all()
    my_email = []
    for i in email:
        my_email.append(i.email)

    sendmail =  [(subject, message, f"<{settings.EMAIL_HOST_USER}>",[email]) for email in my_email]
    send_mass_mail(sendmail)

    return None
