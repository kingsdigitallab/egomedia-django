from .base import *  # noqa

ALLOWED_HOSTS = ['egomedia.kdl.kcl.ac.uk']

INTERNAL_IPS = INTERNAL_IPS + ['']

DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'NAME': 'app_egomedia_liv',
        'USER': 'app_egomedia',
        'PASSWORD': '',
        'HOST': ''
    },
}

SECRET_KEY = ''
