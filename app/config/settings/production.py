from .base import *

secrets = json.loads(open(SECRET_PRODUCTION, 'rt').read())
set_config(secrets, module_name=__name__, start=True)

DEBUG = False
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com'
]

WSGI_APPLICATION = 'config.wsgi.production.application'

INSTALLED_APPS += [
    'storages',
]

DEFAULT_FILE_STORAGE = 'config.storage.DefaultFilesStorage'
STATICFILES_STORAGE = 'config.storage.StaticFilesStorage'