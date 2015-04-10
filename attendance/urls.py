from django.conf.urls import patterns, url

from .views import register, signin, index, report

urlpatterns = patterns('',
    # /
    url(r'^$', index, name='index'),

    # /register/
    url(r'^register/$', register, name='register'),

    # /signin/<meeting_id>/
    url(r'^signin/(?P<meeting_id>\d+)/$', signin, name='signin'),

    # /report/meeting/ OR /report/member/
    url(r'^report/(?P<report_type>(meeting|member))/$', report, name='report'),

)
