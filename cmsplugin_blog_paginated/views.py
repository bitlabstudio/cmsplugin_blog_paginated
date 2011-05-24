from django.conf import settings
from django.views.generic import ArchiveIndexView

from cmsplugin_blog.models import Entry


class BlogArchiveIndexView(ArchiveIndexView):
    model = Entry
    date_field = 'pub_date'

    def get_paginate_by(self, queryset):
        return settings.BLOG_PAGINATE_BY

