from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory

import pytest

from mysite import constants
from mysite.libs import common


@pytest.mark.django_db(transaction=False)
def test_get_role():
    factory = RequestFactory()
    request = factory.get('/')

    user1 = AnonymousUser()
    request.user = user1
    assert common.get_role(request) == ''

    user2 = User.objects.create_user(username='ad02',
                                     password='p@ssw0rd',
                                     first_name='02',
                                     last_name=constants.ROLE_SUPER_ADMIN)
    request.user = user2
    assert common.get_role(request) == user2.last_name
