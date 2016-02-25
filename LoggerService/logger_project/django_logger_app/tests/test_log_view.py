from django.test import TestCase
from rest_framework import status

from django_logger_app.models import Log, LogReport
from django_logger_app.views import log_view


class LogViewTestCase(TestCase):
    def test_createLog_successfully(self):
        response = log_view.create_log('Ivon', 'DEBUG', 'test_create_log')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        log = response.data.serializer.instance
        self.assertEquals(log.log_level, Log.get_log_level_code('DEBUG'))
        self.assertEquals(log.source, 'Ivon')
        self.assertEquals(log.message, 'test_create_log')
        self.assertIsNotNone(log.date)
        self.assertIsNotNone(log.id)

        log_record = Log.objects.get(pk=log.id)
        self.assertTrue(log_record == log)

    def test_createLog_invalid_log_level(self):
        response = log_view.create_log('Ivon1', 'DEBUG1', 'test_create_log')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        log_record = Log.objects.filter(source='Ivon1')
        self.assertTrue(log_record.__len__() == 0)

    def test_createLog_none_source(self):
        response = log_view.create_log(None, 'DEBUG', 'test_create_log')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        log_record = Log.objects.filter(source=None)
        self.assertTrue(log_record.__len__() == 0)

    def test_createLog_none_message(self):
        response = log_view.create_log('Ivon', 'DEBUG', None)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        log_record = Log.objects.filter(source=None)
        self.assertTrue(log_record.__len__() == 0)
