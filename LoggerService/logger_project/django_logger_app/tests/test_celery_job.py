from django.test import TestCase
from django_logger_app.models import Log, LogReport, LogReportSerializer
from django_logger_app import celery_jobs


class LogReportsManagerTestCase(TestCase):
    fixtures = ["test_celery_job.json", ]

    def test_shit(self):
        celery_jobs.create_report();
        log_reports = LogReport.objects.all()
        self.assertEquals(log_reports.__len__(), Log.LOG_LEVELS.__len__())
        debug_report = (log_reports.filter(key=LogReport.LOG_LEVEL, value='DEBUG'))
        self.assertEquals(debug_report.get().count, 2)
        self.assertTrue(Log.objects.all().__len__() == 6)
