# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-14 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_auto_20180614_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject_user',
            name='Subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.Subject'),
        ),
        migrations.AlterField(
            model_name='subject_user',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.User'),
        ),
    ]
