# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_logger_app', '0005_auto_20160215_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='logreport',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]