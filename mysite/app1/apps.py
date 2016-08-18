from __future__ import unicode_literals

from django.apps import AppConfig


class App1Config(AppConfig):
    name = 'app1'
    verbose_name = 'App 1'  # TODO replace with ugettext_lazy()

    # add a new class attribute
    menu = {'dashboard': name,
            'name': verbose_name,
            'order': '1',
            'path': name}

    # override ready method
    def ready(self):
        super(App1Config, self).ready()
        # TODO update class variable 'menu' to add permission information
