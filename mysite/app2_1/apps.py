from __future__ import unicode_literals

from django.apps import AppConfig


class App21Config(AppConfig):
    name = 'app2_1'
    verbose_name = 'App 2_1'  # TODO replace with ugettext_lazy()

    # add a new class attribute
    menu = {'dashboard': 'app2',
            'panel': name,
            'name': verbose_name,
            'order': '2'}

    # override ready method
    def ready(self):
        super(App21Config, self).ready()
        # TODO update class variable 'menu' to add permission information
