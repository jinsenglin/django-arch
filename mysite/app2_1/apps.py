from __future__ import unicode_literals

from django.apps import AppConfig


class App21Config(AppConfig):
    name = 'app2_1'
    menu = {'dashboard': 'app2', 'panel': 'app2_1', 'order': '2'}
