from django.test import TestCase
from django_logger_app.models import Log, LogReport
from django_logger_app import celery_jobs


class CeleryJobsTestCase(TestCase):
    fixtures = ["test_celery_job.json", ]

    def test_createReport(self):
        celery_jobs.create_report();
        log_reports = LogReport.objects.all()
        self.assertEquals(log_reports.__len__(), Log.LOG_LEVELS.__len__())
        debug_report = (log_reports.filter(key=LogReport.LOG_LEVEL, value='DEBUG'))
        info_report = (log_reports.filter(key=LogReport.LOG_LEVEL, value='INFO'))
        error_report = (log_reports.filter(key=LogReport.LOG_LEVEL, value='ERROR'))
        no_reports_unknown_source = log_reports.filter(source='UNKNOWN')
        self.assertEquals(no_reports_unknown_source.count(), 0);
        self.assertEquals(debug_report.get().count, 1)
        self.assertEquals(info_report.get().count, 2)
        self.assertEquals(error_report.get().count, 0)
        self.assertTrue(Log.objects.all().__len__() == 6)
