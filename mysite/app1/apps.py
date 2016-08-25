from __future__ import unicode_literals
import logging

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from mysite import constants


logger = logging.getLogger(__name__)


class App1Config(AppConfig):
    name = 'app1'
    verbose_name = _('App 1')

    # add a new class attribute
    menu = {'dashboard': name,
            'name': verbose_name,
            'order': 10,
            'path': name,
            'scope': [constants.ROLE_SUPER_ADMIN,
                      constants.ROLE_SYSTEM_ADMIN,
                      constants.ROLE_PROJECT_ADMIN,
                      constants.ROLE_PROJECT_USER,
                      constants.ROLE_AUDIT_USER]}

    # print debug information
    logger.debug(' '.join(['dashboard =', menu['dashboard']]))
    logger.debug(' '.join(['order =', str(menu['order'])]))
    logger.debug(' '.join(['scope =', ','.join(menu['scope'])]))
    logger.debug(' '.join(['path =', menu['path']]))

    # override ready method
    def ready(self):
        """Update class variable 'menu' here if according to other model
        """

        super(App1Config, self).ready()

        # register urlconf
        from django.conf.urls import include, url
        from mysite import urls
        urls.urlpatterns.append(url(r'^app1/', include('app1.urls')))
