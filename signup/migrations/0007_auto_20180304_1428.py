# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0006_auto_20180303_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
