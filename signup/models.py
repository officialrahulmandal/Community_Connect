# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# model for acquiring user_details
class user_details(models.Model):
    TYPE_CHOICES = (('pd', 'PyDelhi'),('pl', 'PyLadies'),('lc', 'LinuxChix'),)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100,null=True)
    channels_subscribed=models.CharField(max_length=2, choices=TYPE_CHOICES)
    administrator=models.ForeignKey('auth.User', on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

# model for send_mails
class send_mails(models.Model):
    subject=models.CharField(max_length=100)
    body=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    sender=models.CharField(max_length=100)
    open_counter=models.CharField(max_length=100)

# model for email_drafts
class email_drafts(models.Model):
    subject=models.CharField(max_length=100)
    body=models.CharField(max_length=100)
    variable=models.CharField(max_length=100)
    timer=models.CharField(max_length=100)
