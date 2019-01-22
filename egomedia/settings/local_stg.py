from .base import *  # noqa

ALLOWED_HOSTS = ['egomedia-stg.kdl.kcl.ac.uk']

CACHE_REDIS_DATABASE = '1'
CACHES['default']['LOCATION'] = '127.0.0.1:6379:' + CACHE_REDIS_DATABASE

INTERNAL_IPS = INTERNAL_IPS + ['']
ALLOWED_HOSTS = ['']

DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'NAME': 'app_egomedia_stg',
        'USER': 'app_egomedia',
        'PASSWORD': '',
        'HOST': ''
    },
}

SECRET_KEY = ''
