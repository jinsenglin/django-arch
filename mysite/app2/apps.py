from __future__ import unicode_literals
import logging

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from mysite import constants


logger = logging.getLogger(__name__)


class App2Config(AppConfig):
    name = 'app2'
    verbose_name = _('App 2')

    # add a new class attribute
    menu = {'dashboard': name,
            'name': verbose_name,
            'order': 20,
            'scope': [constants.ROLE_SUPER_ADMIN,
                      constants.ROLE_SYSTEM_ADMIN,
                      constants.ROLE_PROJECT_ADMIN,
                      constants.ROLE_PROJECT_USER]}

    # print debug information
    logger.debug(' '.join(['dashboard =', menu['dashboard']]))
    logger.debug(' '.join(['order =', str(menu['order'])]))
    logger.debug(' '.join(['scope =', ','.join(menu['scope'])]))

    # override ready method
    def ready(self):
        """Update class variable 'menu' here if according to other model
        """

        super(App2Config, self).ready()

        # register urlconf
        from django.conf.urls import include, url
        from mysite import urls
        urls.urlpatterns.append(url(r'^app2/', include('app2.urls')))
