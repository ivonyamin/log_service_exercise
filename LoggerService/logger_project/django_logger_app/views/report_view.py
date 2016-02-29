from datetime import datetime
import pytz

from django.utils import timezone
from rest_framework.decorators import api_view
from django_logger_app.models import LogReport, LogReportSerializer
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET'])
def log_report(request):
    request_source = request.GET.get('source')
    request_start_date = request.GET.get('start_date')
    request_end_date = request.GET.get('end_date')
    request_log_level = request.GET.get('log_level')
    request_limit = request.GET.get('limit')

    return get_log_report(request_source, request_start_date, request_end_date, request_log_level, request_limit)


def get_log_report(request_source, request_start_date, request_end_date, request_log_level, request_limit):
    kwargs = {}
    if request_source:
        kwargs['source'] = str(request_source)

    if request_start_date:
        request_start_date = datetime.fromtimestamp(long(request_start_date), tz=pytz.utc)
        if request_start_date < timezone.now():
            kwargs['date__gte'] = request_start_date
        else:
            return handle_error(status.HTTP_400_BAD_REQUEST, 2, "start_date param cannot be greater then current date")

    if request_end_date:
        request_end_date = datetime.fromtimestamp(long(request_end_date), tz=pytz.utc)
        if not request_start_date or request_start_date < request_end_date:
            kwargs['date__lte'] = request_end_date
        else:
            return handle_error(status.HTTP_400_BAD_REQUEST, 3,
                                "start_date param cannot be greater then end_date param")

    if request_log_level:
        kwargs['value'] = request_log_level

    if request_limit:
        log_reports = LogReport.objects.filter(**kwargs)[:int(request_limit)]
    else:
        if kwargs:
            log_reports = LogReport.objects.filter(**kwargs)
        else:
            log_reports = LogReport.objects.all()

    if not log_reports:
        return handle_error(status.HTTP_404_NOT_FOUND, status.HTTP_404_NOT_FOUND,
                            "log reports not found")

    result = LogReportSerializer(log_reports, many=True)
    return Response(result.data, status=status.HTTP_200_OK)


def handle_error(response_status, code, description):
    response_dict = {"code": code,
                     "desc": description}

    return Response(response_dict, response_status)
