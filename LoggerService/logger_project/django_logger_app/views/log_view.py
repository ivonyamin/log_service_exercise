from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from django_logger_app.models import Log, LogSerializer, LogReport, LogReportSerializer
from rest_framework import status
from rest_framework.response import Response
import json
import datetime
from django.utils import timezone

@api_view(['GET', 'POST'])
def log(request):
    if request.method == 'GET':
        return log_list(request)
    else:
        json_body = json.loads(request.body)
        log_source = str(json_body.get('source'))
        log_message = str(json_body.get('message'))
        log_level = str(json_body.get('log_level'))
        return create_log(log_level, log_source, log_message)


def log_list(request):
    request_source = str(request.GET.get('source'))
    request_start_date = request.GET.get('start_date')
    request_end_date = request.GET.get('end_date')
    request_log_level = str(request.GET.get('log_level'))
    request_limit = request.GET.get('limit')

    kwargs = {}
    if request_source:
         kwargs['source'] = request_source

    if request_start_date:
        request_start_date = datetime.datetime.utcfromtimestamp(long(request_start_date))
        if request_start_date < timezone.now():
            kwargs['date__gte'] = request_start_date
        else:
            return handle_error(status.HTTP_400_BAD_REQUEST, 2, "start_date param cannot be greater then current date")

    if request_end_date:
        request_end_date = datetime.datetime.utcfromtimestamp(long(request_end_date))
        if request_start_date < request_end_date:
            kwargs['date__lte'] = request_end_date
        else:
            return handle_error(status.HTTP_400_BAD_REQUEST, 3,
                                "start_date param cannot be greater then end_date param")

    if request_log_level:
        kwargs['log_level'] = Log.get_log_level_code(str(request_log_level))

    if request_limit:
        logs_list = Log.objects.filter(**kwargs)[:int(request_limit)]
    else:
        logs_list = Log.objects.filter(**kwargs)

    if not logs_list:
        return handle_error(status.HTTP_404_NOT_FOUND, status.HTTP_404_NOT_FOUND,
                            "logs with source = %s not found" % request_source)

    result = LogSerializer(logs_list, many=True)
    return Response(result.data, status=status.HTTP_200_OK)


def create_log(log_source, log_level, log_message):

    if not log_source:
        return handle_error(status.HTTP_400_BAD_REQUEST, 1, "source can't be null or empty")

    if not log_message:
        return handle_error(status.HTTP_400_BAD_REQUEST, 1, "message can't be null or empty")

    log_obj = Log(source=log_source, log_level=Log.get_log_level_code(log_level), message=log_message)

    if log_obj.log_level is None:
        return handle_error(status.HTTP_400_BAD_REQUEST, 1, "invalid log level")

    log_obj.save()
    result = LogSerializer(log_obj, many=False)
    return Response(result.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def log_details(request, log_id):

    result = LogSerializer(get_object_or_404(Log, id=log_id), many=False)
    return Response(result.data, status=status.HTTP_200_OK)


def handle_error(response_status, code, description):
    response_dict = {"code": code,
                     "desc": description}

    return Response(response_dict, response_status)
