from __future__ import absolute_import, unicode_literals
from Community_Connect.celery import app
from django.core.mail import EmailMessage
from celery import shared_task

@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@shared_task
def sendAllMails():
    email = EmailMessage('unique dummy subject', 'dummy message', to=['rahulmandal1995@gmail.com'])
    email.send()
        


