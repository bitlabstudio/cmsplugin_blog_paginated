from django.conf import settings
from django.views.generic import ArchiveIndexView

from cmsplugin_blog.models import Entry


class BlogArchiveIndexView(ArchiveIndexView):
    model = Entry
    queryset = Entry.objects.filter(is_published=True)
    date_field = 'pub_date'

    def get_paginate_by(self, queryset):
        if hasattr(settings, 'BLOG_PAGINATE_BY'):
            return settings.BLOG_PAGINATE_BY
        else:
            return 10

