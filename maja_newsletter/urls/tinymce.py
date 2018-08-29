from django.conf.urls import url
from maja_newsletter.views.tinymce_utils import view_tinymce_templates

urlpatterns = [
    url(r'^templates/$', 'view_tinymce_templates', name='tinymce_templates_list'),
]
