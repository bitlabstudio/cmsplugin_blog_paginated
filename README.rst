Important
=========

This app has been discontinued and is no longer maintained.

cmsplugin_blog_pagination
=========================

Adds pagination to the index view of your blog.

This app is an add-on to the fantastic `cmsplugin_blog <https://github.com/fivethreeo/cmsplugin-blog/>`_
application. 

Prerequisites
=============

  * Django
  * django-cms
  * cmsplugin_blog

Installation
============

pip install -e git+git://github.com/bitmazk/cmsplugin_blog_paginated.git#egg=cmsplugin_blog_paginated

Configuration
=============

Add BLOG_PAGINATE_BY to your settings.py. Default is 10.

Use the Blog Paginated Apphook instead of the normal Blog Apphook in the
administration.

Usage
======

Your ``archive_index.html`` will now be served by a ArchiveIndexView. Therefore 
you have access to a context variable named ``page_obj``, as documented
`here <https://docs.djangoproject.com/en/dev/ref/class-based-views/#django.views.generic.list.MultipleObjectMixin>`_.

A simple paginator could look like this::

  <div>
    <span>
      {% if page_obj.has_previous %}
        <a href="?page={{ page_obj.previous_page_number }}">previous</a>
      {% endif %}

      <span>
        {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}
      </span>

      {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">next</a>
      {% endif %}
    </span>
  </div>

License
=======

`The Unlicense <http://unlicense.org/>`_
