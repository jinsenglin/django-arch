from django.apps import apps


def dashboards(request):
    dashboards = []
    for config in apps.get_app_configs():
        if hasattr(config, 'menu'):
            if 'panel' in config.menu:
                # a panel app
                if any(d['name'] == config.menu['dashboard'] for d in dashboards):
                    # parent dashboard already exists TODO
                    pass
                else:
                    dashboards.append({'name': config.menu['dashboard'],
                                       'panels': [{'name': config.name}]})
            else:
                # a dashboard app
                if any(d['name'] == config.menu['dashboard'] for d in dashboards):
                    # dashboard already exists
                    pass
                else:
                    dashboards.append({'name': config.name, 'panels': []})

    menu = {'menu': dashboards}
    return menu
