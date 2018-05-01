from __future__ import absolute_import, unicode_literals
from Community_Connect.celery import app
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.conf import settings
from mails.models import UserExtended


@app.task
def send(subject, message):
	import pdb
	pdb.set_trace()
	for user in User.objects.filter(is_superuser=0):
                finalMessage = render_to_string('mails/CreateMail.html', {
                    'message': message,
                    'username': user.username,
                    'unsubscribe': UserExtended.objects.get(user=user).userKey,
                    "community": settings.COMMUNITY,
                    
                })
                try:
                    email = EmailMessage(
                        subject, finalMessage, to=[user.email])
                    email.send()
                except:
                    # This needs to be changed, instead of raise we want to use logging.
                    raise('Check Email Setup, something might be wrong')
            