from django.template import Template, Context


def test_get_current_role():
    template = Template("{% load mysite %}{% get_current_role %}")
    rendered = template.render(Context({'request': None}))

    assert rendered == u'SA'
