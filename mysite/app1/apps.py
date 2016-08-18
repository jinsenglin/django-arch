from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from mysite import constants


class App1Config(AppConfig):
    name = 'app1'
    verbose_name = _('App 1')

    # add a new class attribute
    menu = {'dashboard': name,
            'name': verbose_name,
            'order': 10,
            'path': name,
            'scope': [constants.ROLE_SUPER_ADMIN,
                      constants.ROLE_SYSTEM_ADMIN,
                      constants.ROLE_PROJECT_ADMIN,
                      constants.ROLE_PROJECT_USER,
                      constants.ROLE_AUDIT_USER]}

    # override ready method
    def ready(self):
        super(App1Config, self).ready()
        # update class variable 'menu' here if according to other model
