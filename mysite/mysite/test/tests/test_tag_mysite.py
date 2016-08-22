from django.contrib.auth.models import AnonymousUser, User
from django.template import Template, Context
from django.test import RequestFactory

import pytest

from mysite import constants


def test_get_current_role_for_anonymouse_user():
    user = AnonymousUser()
    factory = RequestFactory()
    request = factory.get('/')
    request.user = user
    context = Context({'request': request})

    template = Template("{% load mysite %}{% get_current_role %}")
    rendered = template.render(context)

    assert rendered == u''


@pytest.mark.django_db(transaction=False)
def test_get_current_role_for_authenticated_user():
    user = User.objects.create_user(username='ad02',
                                    password='p@ssw0rd',
                                    first_name='02',
                                    last_name=constants.ROLE_SUPER_ADMIN)
    factory = RequestFactory()
    request = factory.get('/')
    request.user = user
    context = Context({'request': request})

    template = Template("{% load mysite %}{% get_current_role %}")
    rendered = template.render(context)

    assert rendered == user.last_name
