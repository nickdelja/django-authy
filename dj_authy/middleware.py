# -*- coding: UTF-8 -*-
from django.conf import settings
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy

from . import _url_to_appropriate_authy_page

import logging
logger = logging.getLogger('django.request')

AUTHY_SESSION_KEY = getattr(settings, 'AUTHY_SESSION_KEY', 'is_authy_authenticated')
AUTHY_IS_REQUIRED_KEY = getattr(settings, 'AUTHY_IS_REQUIRED_KEY', 'require_authy_authentication')


class AuthyAuthenticationRequiredMiddleware(object):
    """
    Allows the system to ensure the user is authy_authenticated

    MIDDLEWARE_CLASSES += (
        'dj_authy.middleware.AuthyAuthenticationRequiredMiddleware',
    )
    """
    def process_request(self, request):
        if request.user.is_authenticated():
            # then use wants authy auth
            if not request.session.get(AUTHY_SESSION_KEY):

                logger.info(request.path)
                # but has not authenticated with authy yet
                if request.path not in [reverse_lazy('dj_authy:holding'),
                                        reverse_lazy('dj_authy:profile'),
                                        settings.LOGOUT_URL]:
                    # and they are not looking at the holding or profile setup page
                    logger.info(u'User authenticating with authy' % request.user)

                    url = _url_to_appropriate_authy_page(request, AUTHY_SESSION_KEY)

                    return redirect(url)
        return None
