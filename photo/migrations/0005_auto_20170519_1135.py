# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20170518_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoupload',
            name='date_deleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='photoupload',
            name='date_approved',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
