# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-17 13:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20180517_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduledsession',
            name='SubjectID',
        ),
        migrations.DeleteModel(
            name='ScheduledSession',
        ),
    ]
