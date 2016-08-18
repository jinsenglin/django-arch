from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class App2Config(AppConfig):
    name = 'app2'
    verbose_name = _('App 2')

    # add a new class attribute
    menu = {'dashboard': name,
            'name': verbose_name,
            'order': '2'}

    # override ready method
    def ready(self):
        super(App2Config, self).ready()
        # TODO update class variable 'menu' to add permission information
