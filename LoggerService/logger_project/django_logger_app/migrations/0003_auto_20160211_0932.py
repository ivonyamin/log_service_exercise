# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 09:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_logger_app', '0002_auto_20160211_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='identifier',
            new_name='source',
        ),
        migrations.RenameField(
            model_name='logreport',
            old_name='identifier',
            new_name='source',
        ),
    ]
