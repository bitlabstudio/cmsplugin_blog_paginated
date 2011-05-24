from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class BlogPaginationApphook(CMSApp):
    name = _('Blog Paginated Apphook')
    urls = ['cmsplugin_blog_paginated.urls']

apphook_pool.register(BlogPaginationApphook)
