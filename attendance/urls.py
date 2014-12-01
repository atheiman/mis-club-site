from django.conf.urls import patterns, url

from attendance import views

urlpatterns = patterns('',
    # /
    url(
        r'^$',
        views.index,
        name='index',
    ),

    # # /obj_id/
    # url(
    #     r'^(?P<obj_id>[0-9]+)\/?$',
    #     views.obj_id,
    #     name='obj_id',
    # ),

    # # /category_slug/
    # url(
    #     r'^(?P<category_slug>[a-z0-9_-]+)\/?$',
    #     views.obj_id,
    #     name='obj_id',
    # ),
)
