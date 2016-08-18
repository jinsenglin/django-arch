from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from mysite import constants


class App22Config(AppConfig):
    name = 'app2_2'
    verbose_name = _('App 2_2')

    # add a new class attribute
    menu = {'dashboard': 'app2',
            'panel': name,
            'name': verbose_name,
            'order': 10,
            'path': name,
            'scope': [constants.ROLE_SUPER_ADMIN,
                      constants.ROLE_SYSTEM_ADMIN]}

    # override ready method
    def ready(self):
        super(App22Config, self).ready()
        # update class variable 'menu' here if according to other model
