from __future__ import unicode_literals

from django.apps import AppConfig


class App1Config(AppConfig):
    name = 'app1'
    menu = {'dashboard': 'app1', 'order': '1'}
