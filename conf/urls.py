from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^attendance/', include('attendance.urls', namespace='attendance')),
    url(r'^admin/', include(admin.site.urls)),
)
