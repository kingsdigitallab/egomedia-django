from .base import *  # noqa

ALLOWED_HOSTS = ['ego.kdl.kcl.ac.uk']

INTERNAL_IPS = INTERNAL_IPS + ['']

DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'NAME': 'app_ego_liv',
        'USER': 'app_ego',
        'PASSWORD': '',
        'HOST': ''
    },
}

SECRET_KEY = ''
