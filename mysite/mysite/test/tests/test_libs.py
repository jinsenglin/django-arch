from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory

import pytest

from mysite import constants
from mysite.libs import common


def test_get_role_for_anonymouse_user():
    factory = RequestFactory()
    request = factory.get('/')

    user = AnonymousUser()
    request.user = user
    assert common.get_role(request) == ''


@pytest.mark.django_db(transaction=False)
def test_get_role_for_authenticated_user():
    factory = RequestFactory()
    request = factory.get('/')

    user = User.objects.create_user(username='ad02',
                                    password='p@ssw0rd',
                                    first_name='02',
                                    last_name=constants.ROLE_SUPER_ADMIN)
    request.user = user
    assert common.get_role(request) == user.last_name
