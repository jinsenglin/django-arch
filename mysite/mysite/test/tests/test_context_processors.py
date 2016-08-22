from django.test import RequestFactory


from mysite import context_processors


def test_sitemap():
    factory = RequestFactory()
    request = factory.get('/')
    request.LANGUAGE_CODE = 'en'

    sitemap = context_processors.sitemap(request)

    assert 'sitemap' in sitemap
