"""Urls for the maja_newsletter Mailing List"""
from django.conf.urls import url

from maja_newsletter.forms import MailingListSubscriptionForm
from maja_newsletter.forms import AllMailingListSubscriptionForm
from maja_newsletter.views.mailing_list import view_mailinglist_unsubscribe, view_mailinglist_subscribe

urlpatterns = [
                       url(r'^unsubscribe/(?P<slug>[-\w]+)/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           view_mailinglist_unsubscribe,
                           name='newsletter_mailinglist_unsubscribe'),
                       url(r'^subscribe/(?P<mailing_list_id>\d+)/',
                           view_mailinglist_subscribe,
                           {'form_class': MailingListSubscriptionForm},
                           name='newsletter_mailinglist_subscribe'),
                       url(r'^subscribe/',
                           view_mailinglist_subscribe,
                           {'form_class': AllMailingListSubscriptionForm},
                           name='newsletter_mailinglist_subscribe_all'),
                       ]
