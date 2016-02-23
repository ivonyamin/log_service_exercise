from django.test import TestCase

# Create your tests here.
from django_logger_app.models import LogReport, Log


class LogTestCase(TestCase):
    def test_get_log_level_code(self):
        code = Log.get_log_level_code('DEBUG')
        self.assertEqual(code, Log.DEBUG)

    def test_get_invalid_log_level_code(self):
        code = Log.get_log_level_code('DEBUG1')
        self.assertEqual(code, None)

    def test_get_none_log_level_code(self):
        code = Log.get_log_level_code(None)
        self.assertEqual(code, None)


