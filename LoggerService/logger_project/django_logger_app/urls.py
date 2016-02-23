from django.conf.urls import url

import views.log_view
import views.report_view

urlpatterns = [
    url(r'^$', views.log_view.log, name='log'),
    url(r'^(?P<log_id>.*)/$', views.log_view.log_details, name='log_details'),
]
