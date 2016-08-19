from django.apps import apps
from django.core.cache import cache

from mysite import constants


def sitemap(request):
    """Return sitemap"""

    myrole = constants.ROLE_AUDIT_USER  # TODO : replace with request..some.attr
    mylang = request.LANGUAGE_CODE

    # print debug information
    print myrole
    print mylang

    def mkcachekey(myrole, mylang):
        """Return cache key according to role and language code"""

        return ':'.join([mylang, myrole, 'sitemap'])

    def hasperm(myrole, scope):
        """Return True if the user role falls in the given scope"""

        return any(role == myrole for role in scope)

    def mksitemap(myrole):
        """Return sitemap according to role"""

        # triage apps
        dashboard_dict = {}
        panel_list = []
        for config in apps.get_app_configs():
            if hasattr(config, 'menu') and hasperm(myrole,
                                                   config.menu['scope']):
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

    # return sitemap from cache if exists, otherwise make one and cache it
    cachekey = mkcachekey(myrole, mylang)
    sitemap = cache.get(cachekey)
    if sitemap:
        return sitemap
    else:
        sitemap = mksitemap(myrole)
        cache.set(cachekey, sitemap)
        return sitemap
