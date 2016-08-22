from django import template

from ..libs import common


register = template.Library()


@register.simple_tag(takes_context=True, name='get_current_role')
def current_role(context):
    request = context['request']
    return common.get_role(request)
