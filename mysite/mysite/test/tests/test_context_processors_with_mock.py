from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
from django.apps import AppConfig

import pytest
from mock import patch

from mysite import context_processors
from mysite import constants


class X(AppConfig):
    name = 'app1'
    verbose_name = 'App 1'
    menu = {'dashboard': name,
            'name': verbose_name,
            'order': 10,
            'path': name,
            'scope': [constants.ROLE_SUPER_ADMIN,
                      constants.ROLE_SYSTEM_ADMIN,
                      constants.ROLE_PROJECT_ADMIN,
                      constants.ROLE_PROJECT_USER,
                      constants.ROLE_AUDIT_USER]}


@patch('mysite.context_processors.apps.get_app_configs', return_value=[X])
def test_sitemap_for_anonymous_user(configs):
    user = AnonymousUser()
    factory = RequestFactory()
    request = factory.get('/')
    request.user = user
    request.LANGUAGE_CODE = 'en'

    # test the first hit
    sitemap = context_processors.sitemap(request)
    assert 'sitemap' in sitemap
    assert len(sitemap['sitemap']) == 0

    # test the cached
    sitemap = context_processors.sitemap(request)
    assert 'sitemap' in sitemap
    assert len(sitemap['sitemap']) == 0


@patch('mysite.context_processors.apps.get_app_configs', return_value=[X])
@pytest.mark.django_db(transaction=False)
def test_sitemap_for_authenticated_user(configs):
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
    assert len(sitemap['sitemap']) == 1

    # test the cached
    sitemap = context_processors.sitemap(request)
    assert 'sitemap' in sitemap
    assert len(sitemap['sitemap']) == 1
