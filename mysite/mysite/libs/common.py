def get_role(request):
    """Return role from given request"""

    if request.user.is_authenticated:
        return request.user.last_name
    else:
        return ''
