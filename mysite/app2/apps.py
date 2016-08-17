from __future__ import unicode_literals

from django.apps import AppConfig


class App2Config(AppConfig):
    name = 'app2'
    menu = {'dashboard': 'app2', 'order': '2'}
