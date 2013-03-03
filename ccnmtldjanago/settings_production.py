# flake8: noqa
from settings_shared import *

TEMPLATE_DIRS = (
    "/var/www/ccnmtldjanago/ccnmtldjanago/ccnmtldjanago/templates",
)

MEDIA_ROOT = '/var/www/ccnmtldjanago/uploads/'
# put any static media here to override app served static media
STATICMEDIA_MOUNTS = (
    ('/sitemedia', '/var/www/ccnmtldjanago/ccnmtldjanago/sitemedia'),
)

COMPRESS_ROOT = "/var/www/ccnmtldjanago/ccnmtldjanago/media/"
DEBUG = False
TEMPLATE_DEBUG = DEBUG

SENTRY_SITE = 'ccnmtldjanago'
SENTRY_SERVERS = ['http://sentry.ccnmtl.columbia.edu/sentry/store/']

import logging
from raven.contrib.django.handlers import SentryHandler
logger = logging.getLogger()
# ensure we havent already registered the handler
if SentryHandler not in map(type, logger.handlers):
    logger.addHandler(SentryHandler())

    # Add StreamHandler to sentry's default so you can catch missed exceptions
    logger = logging.getLogger('sentry.errors')
    logger.propagate = False
    logger.addHandler(logging.StreamHandler())

try:
    from local_settings import *
except ImportError:
    pass
