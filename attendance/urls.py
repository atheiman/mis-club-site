from django.conf.urls import patterns, url

from .views import index, register, signin

urlpatterns = patterns('',
    # /
    url(r'^$', index, name='index'),

    # /register
    url(r'^register\/?$', register, name='register'),

    # /signin/<meeting_id>
    url(r'^signin/(?P<meeting_id>\d+)', signin, name='signin'),
)
