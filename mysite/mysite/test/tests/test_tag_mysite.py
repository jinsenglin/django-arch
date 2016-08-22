from django.template import Template, Context
from django.test import RequestFactory


def test_get_current_role():
    factory = RequestFactory()
    request = factory.get('/')
    context = Context({'request': request})

    template = Template("{% load mysite %}{% get_current_role %}")
    rendered = template.render(context)

    # TODO : replace with real role, e.g., request.user.role

    assert rendered == u'SA'
