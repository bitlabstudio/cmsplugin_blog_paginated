from django.views.generic import ArchiveIndexView

from cmsplugin_blog.models import Entry


class BlogArchiveIndexView(ArchiveIndexView):
    paginate_by = 2
    model = Entry
    date_field = 'pub_date'
