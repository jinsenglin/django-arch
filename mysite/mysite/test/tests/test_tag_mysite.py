from django.contrib.auth.models import AnonymousUser
from django.template import Template, Context
from django.test import RequestFactory


def test_get_current_role():
    user = AnonymousUser()
    factory = RequestFactory()
    request = factory.get('/')
    request.user = user
    context = Context({'request': request})

    template = Template("{% load mysite %}{% get_current_role %}")
    rendered = template.render(context)

    assert rendered == u''
