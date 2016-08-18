from __future__ import unicode_literals

from django.apps import AppConfig


class App22Config(AppConfig):
    name = 'app2_2'
    verbose_name = 'App 2_2'  # TODO replace with ugettext_lazy()

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
