from __future__ import unicode_literals

from django.apps import AppConfig


class App22Config(AppConfig):
    name = 'app2_2'
    menu = {'dashboard': 'app2', 'panel': 'app2_2', 'order': '1'}
