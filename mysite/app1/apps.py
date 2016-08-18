from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class App1Config(AppConfig):
    name = 'app1'
    verbose_name = _('App 1')

    # add a new class attribute
    menu = {'dashboard': name,
            'name': verbose_name,
            'order': '1',
            'path': name}

    # override ready method
    def ready(self):
        super(App1Config, self).ready()
        # TODO update class variable 'menu' to add permission information
