# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 17:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20180606_1320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availability',
            old_name='Availability',
            new_name='UserId',
        ),
    ]