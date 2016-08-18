from __future__ import unicode_literals

from django.apps import AppConfig


class App2Config(AppConfig):
    name = 'app2'
    verbose_name = 'App 2'  # TODO replace with ugettext_lazy()

    # add a new class attribute
    menu = {'dashboard': name,
            'name': verbose_name,
            'order': '2'}

    # override ready method
    def ready(self):
        super(App2Config, self).ready()
        # TODO update class variable 'menu' to add permission information
