from django.contrib import admin

from .models import Log

from .models import LogReport

admin.site.register(Log)
admin.site.register(LogReport)
