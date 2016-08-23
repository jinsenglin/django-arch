from django.core.urlresolvers import resolve


def test_root():
    result = resolve('/')
    assert result.view_name == 'index'
