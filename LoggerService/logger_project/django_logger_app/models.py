from __future__ import unicode_literals

import uuid
from django.utils import timezone
from datetime import datetime

from django.db import models
from rest_framework import serializers


class Log(models.Model):
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
    LOG_LEVELS = ((DEBUG, 'DEBUG'), (INFO, 'INFO'), (WARN, 'WARNING'), (ERROR, 'ERROR'),)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(blank=False, null=False, default=timezone.now)
    source = models.CharField(max_length=200, blank=False, null=False)
    log_level = models.IntegerField(choices=LOG_LEVELS,blank=False, null=False)
    message = models.TextField(blank=False, null=False)

    @staticmethod
    def get_log_level_code(val):
        for level in Log.LOG_LEVELS:
                if str(level[1]) == val:
                    return level[0]
        return None


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log


class LogReport(models.Model):
    LOG_LEVEL = 1
    MESSAGE_PREFIX = 2
    AVAILABLE_KEYS = ((LOG_LEVEL, 'LOG_LEVEL'), (MESSAGE_PREFIX, 'MESSAGE_PREFIX'),)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(blank=False, null=False, default=timezone.now)
    source = models.CharField(max_length=200, blank=False, null=False)
    key = models.IntegerField(choices=AVAILABLE_KEYS, default=LOG_LEVEL, blank=False, null=False)
    value = models.CharField(max_length=200, blank=False, null=False)
    count = models.IntegerField(blank=False, null=False, default=0)


class LogReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogReport
