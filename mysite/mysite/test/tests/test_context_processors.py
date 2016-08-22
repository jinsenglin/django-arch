from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory


from mysite import context_processors


def test_sitemap():
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
