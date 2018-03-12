from .base import *

DEBUG = False
ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.dev.application'

secrets = json.loads(open(SECRET_DEV, 'rt').read())

DATABASES = secrets['DATABASES']
