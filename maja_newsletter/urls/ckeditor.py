from django.conf.urls import url
from django.conf.urls import patterns
from maja_newsletter.views.ckeditor_utils import view_ckeditor_templates

urlpatterns = patterns('maja_newsletter.views.ckeditor_utils',
    url(r'^templates/$', view_ckeditor_templates, name='ckeditor_templates_list'),
)
