from __future__ import absolute_import
from celery import shared_task

from django.utils import timezone
from django_logger_app.models import Log, LogReport
import datetime


@shared_task()
def create_report():
    report_date = timezone.now()
    report_logs_start_date = report_date - datetime.timedelta(hours=1)
    sources_list = Log.objects.values_list('source', flat=True).distinct()
    for source in sources_list:
        for level in Log.LOG_LEVELS:
            log_report = LogReport()
            log_report.date = report_date
            log_report.source = str(source)
            log_report.key = LogReport.LOG_LEVEL
            log_report.value = str(level[1])
            log_report.count = Log.objects.all().filter(date__range=(report_logs_start_date, report_date),
                                                        source=source,
                                                        log_level=level[0]).count()
            log_report.save()
