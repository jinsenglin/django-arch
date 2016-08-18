from django.apps import apps


def sitemap(request):
    dashboard_list = []

    # triage apps
    dashboard_dict = {}
    panel_list = []
    for config in apps.get_app_configs():
        if hasattr(config, 'menu'):
            if 'panel' in config.menu:
                panel_list.append(config.menu)
            else:
                config.menu['panels'] = []
                dashboard_dict[config.menu['dashboard']] = config.menu

    # triage panels
    for panel in panel_list:
        dashboard_dict[panel['dashboard']]['panels'].append(panel)

    # convert dashboards from dict to list
    for dashboard in dashboard_dict:
        dashboard_list.append(dashboard_dict[dashboard])

    sitemap = {'sitemap': dashboard_list}
    return sitemap
