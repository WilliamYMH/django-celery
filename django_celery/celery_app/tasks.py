from celery import shared_task 

from django.core.mail import send_mail

from time import sleep

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_task():
    sleep(2)
    send_mail('Heyy Celery task worked!',
    'This is proof the task worked!',
    '--------------------------------',
    ['williamyesid.10@gmail.com', 'williamyesidmh@ufps.edu.co'])

    return None
