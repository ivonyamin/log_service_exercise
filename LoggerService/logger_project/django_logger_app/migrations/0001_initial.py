# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('source', models.CharField(max_length=200)),
                ('log_level', models.IntegerField(choices=[(1, 'DEBUG'), (2, 'INFO'), (3, 'WARNING'), (4, 'ERROR')])),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LogReport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('source', models.CharField(max_length=200)),
                ('key', models.IntegerField(choices=[(1, 'LOG_LEVEL'), (2, 'MESSAGE_PREFIX')], default=1)),
                ('value', models.CharField(max_length=200)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
