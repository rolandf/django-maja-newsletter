"""Urls for the maja_newsletter Newsletter"""
from django.conf.urls import url
from maja_newsletter.views.newsletter import view_newsletter_preview, view_newsletter_contact

urlpatterns = [
                       url(r'^preview/(?P<slug>[-\w]+)/$',
                           view_newsletter_preview,
                           name='newsletter_newsletter_preview'),
                       url(r'^(?P<slug>[-\w]+)/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           view_newsletter_contact,
                           name='newsletter_newsletter_contact'),
                       ]
