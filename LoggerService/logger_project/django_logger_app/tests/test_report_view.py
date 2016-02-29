from datetime import datetime, timedelta, date
from calendar import timegm


from django.test import TestCase
from rest_framework import status
from django.utils import timezone
from django_logger_app.views.report_view import get_log_report


class ReportViewTestCase(TestCase):
    fixtures = ["test_report_view.json", ]

    def test_get_log_report_no_params(self):
        report_response = get_log_report(None, None, None, None, None)
        self.verifyResponseSuccess(report_response, 11)

    def test_get_log_report_limit_param(self):
        report_response = get_log_report(None, None, None, None, 5)
        self.verifyResponseSuccess(report_response, 5)

    def test_get_log_report_start_date_param(self):
        yesterday_date = (timezone.now() - timedelta(days=1))
        report_response = get_log_report(None, timegm(yesterday_date.timetuple()), None, None, None)
        self.verifyResponseSuccess(report_response, 4)

    def test_get_log_report_end_date_param(self):
        yesterday_date = (timezone.now() - timedelta(days=1))
        report_response = get_log_report(None, None, timegm(yesterday_date.timetuple()), None, None)
        self.verifyResponseSuccess(report_response, 7)

    def verifyResponseSuccess(self, report_response, expected_count):
        self.assertTrue(report_response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(report_response.data)
        report = report_response.data
        self.assertEquals(report.__len__(), expected_count)





