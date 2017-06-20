# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 14:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import photos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_upload', models.DateTimeField(default=django.utils.timezone.now)),
                ('pause_upload', models.DateTimeField(default=photos.models.pause)),
                ('status', models.CharField(choices=[('ir', 'In Review'), ('ap', 'Approved'), ('tr', 'Trash')], default='ir', max_length=2)),
                ('date_approved', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('date_deleted', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=photos.models.PhotoUpload.path_and_rename, validators=[photos.models.PhotoUpload.file_size])),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
