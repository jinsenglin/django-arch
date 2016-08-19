from django import template


register = template.Library()


@register.simple_tag(takes_context=True, name='get_current_role')
def current_role(context):
    # TODO : replace with real role
    return 'SA'
