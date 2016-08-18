from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class App21Config(AppConfig):
    name = 'app2_1'
    verbose_name = _('App 2_1')

    # add a new class attribute
    menu = {'dashboard': 'app2',
            'panel': name,
            'name': verbose_name,
            'order': '2',
            'path': name,
            'scope': 'anonymous'}

    # override ready method
    def ready(self):
        super(App21Config, self).ready()
        # TODO update class variable 'menu' to add permission information
