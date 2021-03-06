"""Tokens system for maja_newsletter"""
from django.conf import settings
from django.http import Http404
from django.utils.http import int_to_base36, base36_to_int

from maja_newsletter.models import Contact


class ContactTokenGenerator(object):
    """ContactTokengenerator for the newsletter
    based on the PasswordResetTokenGenerator bundled
    in django.contrib.auth"""

    def make_token(self, contact):
        """Method for generating the token"""
        from hashlib import sha1

        token = sha1(settings.SECRET_KEY + str(contact.id) +
                     contact.email).hexdigest()[::2]
        return token

    def check_token(self, contact, token):
        """Check if the token is correct for this user"""
        return token == self.make_token(contact)


def tokenize(contact):
    """Return the uid in base 36 of a contact, and a token"""
    token_generator = ContactTokenGenerator()
    return int_to_base36(contact.id), token_generator.make_token(contact)


def untokenize(uidb36, token):
    """Retrieve a contact by uidb36 and token"""
    try:
        contact_id = base36_to_int(uidb36)
        contact = Contact.objects.get(pk=contact_id)
    except:
        raise Http404

    token_generator = ContactTokenGenerator()
    if token_generator.check_token(contact, token):
        return contact
    raise Http404
