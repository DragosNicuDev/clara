# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_remove_photoupload_date_apropved'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoupload',
            name='date_approved',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]