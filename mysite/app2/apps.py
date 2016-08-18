from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from mysite import constants


class App2Config(AppConfig):
    name = 'app2'
    verbose_name = _('App 2')

    # add a new class attribute
    menu = {'dashboard': name,
            'name': verbose_name,
            'order': 20,
            'scope': [constants.ROLE_SUPER_ADMIN,
                      constants.ROLE_SYSTEM_ADMIN,
                      constants.ROLE_PROJECT_ADMIN,
                      constants.ROLE_PROJECT_USER]}

    # override ready method
    def ready(self):
        super(App2Config, self).ready()
        # update class variable 'menu' here if according to other model
