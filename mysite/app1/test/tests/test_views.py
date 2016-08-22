# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import Client
from django.test import override_settings

import pytest


def test_index():
    client = Client()
    response = client.get('/app1/')

    assert response.status_code == 200


@override_settings(LANGUAGE_CODE='en')
@pytest.mark.django_db(transaction=False)
def test_index_for_authenticated_en_user():
    User.objects.create_user(username='ad02',
                             password='p@ssw0rd',
                             first_name='02',
                             last_name='AD')

    client = Client()
    authenticated = client.login(username='ad02', password='p@ssw0rd')

    assert authenticated

    response = client.get('/app1/')

    assert u'Application 1' in response.content.decode('utf8')
