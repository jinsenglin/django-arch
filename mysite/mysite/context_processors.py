from django.apps import apps


def sitemap(request):
    def hasperm(app):
        """Filter app according to scope"""

        # TODO
        return True

    # debug
    print request.LANGUAGE_CODE
    print request.user.is_authenticated

    # triage apps
    dashboard_dict = {}
    panel_list = []
    for config in apps.get_app_configs():
        if hasattr(config, 'menu') and hasperm(config.menu['scope']):
            if 'panel' in config.menu:
                panel_list.append(config.menu)
            else:
                config.menu['panels'] = []
                dashboard_dict[config.menu['dashboard']] = config.menu

    # triage panels
    for panel in panel_list:
        dashboard_dict[panel['dashboard']]['panels'].append(panel)

    # convert dashboards from dict to list
    dashboard_list = []
    for dashboard in dashboard_dict:
        dashboard_list.append(dashboard_dict[dashboard])

    # sort panels
    for dashboard in dashboard_list:
        dashboard['panels'] = sorted(dashboard['panels'],
                                     key=lambda k: k['order'])

    # sort dashboards
    dashboard_list = sorted(dashboard_list, key=lambda k: k['order'])

    sitemap = {'sitemap': dashboard_list}
    return sitemap
