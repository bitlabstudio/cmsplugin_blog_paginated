from django.conf.urls.defaults import *

from cmsplugin_blog.urls import urlpatterns as cmsplugin_urlpatterns

from cmsplugin_blog_paginated.views import BlogArchiveIndexView


urlpatterns = patterns('',
    (r'^$', BlogArchiveIndexView.as_view(), {}, 'blog_archive_index'),
)

urlpatterns += cmsplugin_urlpatterns
