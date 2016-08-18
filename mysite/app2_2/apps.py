from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class App22Config(AppConfig):
    name = 'app2_2'
    verbose_name = _('App 2_2')

    # add a new class attribute
    menu = {'dashboard': 'app2',
            'panel': name,
            'name': verbose_name,
            'order': '1',
            'path': name}

    # override ready method
    def ready(self):
        super(App22Config, self).ready()
        # TODO update class variable 'menu' to add permission information
