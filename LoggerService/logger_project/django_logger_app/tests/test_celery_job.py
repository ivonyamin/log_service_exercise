from django.test import TestCase
from django_logger_app.models import Log
from django_logger_app import celery_jobs


class LogReportsManagerTestCase(TestCase):
    fixtures = ["test_celery_job.json", ]

    def test_shit(self):
        celery_jobs.create_report();
        self.assertT
        self.assertTrue(Log.objects.all().__len__() == 6)
