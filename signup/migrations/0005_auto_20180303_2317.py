# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20180303_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='channels_subscribed',
            field=models.CharField(choices=[('pd', 'PyDelhi'), ('pl', 'PyLadies'), ('lc', 'LinuxChix')], max_length=2),
        ),
    ]
