from django.conf.urls import patterns, url

from .views import register, signin

urlpatterns = patterns('',
    # /register
    url(r'^register\/?$', register, name='register'),

    # /signin/<meeting_id>
    url(r'^signin/(?P<meeting_id>\d+)', signin, name='signin'),
)
