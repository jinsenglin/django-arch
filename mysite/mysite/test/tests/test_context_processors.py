from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory

import pytest

from mysite import context_processors


def test_sitemap_for_anonymous_user():
    user = AnonymousUser()
    factory = RequestFactory()
    request = factory.get('/')
    request.user = user
    request.LANGUAGE_CODE = 'en'

    # test the first hit
    sitemap = context_processors.sitemap(request)
    assert 'sitemap' in sitemap

    # test the cached
    sitemap = context_processors.sitemap(request)
    assert 'sitemap' in sitemap


@pytest.mark.django_db(transaction=False)
def test_sitemap_for_authenticated_user():
    user = User.objects.create(username='ad02',
                               password='p@ssw0rd',
                               first_name='02',
                               last_name='AD')
    factory = RequestFactory()
    request = factory.get('/')
    request.user = user
    request.LANGUAGE_CODE = 'en'

    # test the first hit
    sitemap = context_processors.sitemap(request)
    assert 'sitemap' in sitemap

    # test the cached
    sitemap = context_processors.sitemap(request)
    assert 'sitemap' in sitemap
