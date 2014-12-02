from django.conf.urls import patterns, url

from .views import index, meeting_list, signin

urlpatterns = patterns('',
    # /
    url(r'^$', index, name='index'),

    # /meetings
    url(r'^meetings\/?$', meeting_list, name='meeting_list'),

    # /signin/<meeting_id>
    url(r'signin/(?P<meeting_id>\d+)', signin, name='signin'),
)
