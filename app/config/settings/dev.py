from .base import *

DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com'
]

WSGI_APPLICATION = 'config.wsgi.dev.application'

secrets = json.loads(open(SECRET_DEV, 'rt').read())

INSTALLED_APPS += [
    'django_extensions',
    'storages',
]


DEFAULT_FILE_STORAGE = 'config.storage.DefaultFilesStorage'
# S3 대신 EC2에서 정적파일을 제공 (프리티어의 put 사용량 절감)
# STATICFILES_STORAGE = 'config.storage.StaticFilesStorage'

set_config(secrets, module_name=__name__, start=True)






