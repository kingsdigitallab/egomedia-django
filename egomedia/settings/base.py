"""
Django settings for egomedia project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/

For production settings see
https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
"""

import getpass
import logging
import os

from django_auth_ldap.config import LDAPGroupQuery
from kdl_ldap.settings import *  # noqa

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

PROJECT_NAME = 'egomedia'
PROJECT_TITLE = 'Ego Media'

# -----------------------------------------------------------------------------
# Core Settings
# https://docs.djangoproject.com/en/dev/ref/settings/#id6
# -----------------------------------------------------------------------------

ADMINS = ()
MANAGERS = ADMINS

ALLOWED_HOSTS = []

# https://docs.djangoproject.com/en/dev/ref/settings/#caches
# https://docs.djangoproject.com/en/dev/topics/cache/
# http://redis.io/topics/lru-cache
# http://niwibe.github.io/django-redis/
CACHE_REDIS_DATABASE = '0'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/' + CACHE_REDIS_DATABASE,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True
        }
    }
}

CSRF_COOKIE_SECURE = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# -----------------------------------------------------------------------------
# EMAIL SETTINGS
# -----------------------------------------------------------------------------

DEFAULT_FROM_EMAIL = 'noreply@kcl.ac.uk'
EMAIL_HOST = 'smtp.cch.kcl.ac.uk'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = '[Django {}] '.format(PROJECT_NAME)
EMAIL_USE_TLS = False

# Sender of error messages to ADMINS and MANAGERS
SERVER_EMAIL = DEFAULT_FROM_EMAIL

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',

    'activecollab_digger',
    'compressor',
    'django_extensions',

    'kdl_ldap',
    'rest_framework',

    'wagtail.contrib.forms',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.redirects',
    'wagtail.contrib.routable_page',
    'wagtail.contrib.settings',
    'wagtail.contrib.styleguide',
    'wagtail.contrib.table_block',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',
    'wagtailmenus',

    'bakery',
    'wagtailbakery'
]

INSTALLED_APPS += [
    'kdl_wagtail.core',
    'kdl_wagtail.people',
    'kdl_wagtail.zotero',
    'core.apps.CoreConfig'
]

INTERNAL_IPS = ['127.0.0.1']

# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_L10N = False
USE_TZ = True

LOGGING_ROOT = os.path.join(BASE_DIR, 'logs')
LOGGING_LEVEL = logging.WARN

if not os.path.exists(LOGGING_ROOT):
    os.makedirs(LOGGING_ROOT)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(levelname)s %(asctime)s %(module)s '
                       '%(process)d %(thread)d %(message)s')
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'django.log'),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'mail_admins'],
            'level': LOGGING_LEVEL,
            'propagate': True
        },
        'egomedia': {
            'handlers': ['file'],
            'level': LOGGING_LEVEL,
            'propagate': True
        },
    }
}

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = PROJECT_NAME + '.urls'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',

                'activecollab_digger.context_processors.activecollab_digger',

                'wagtail.contrib.settings.context_processors.settings',
                'wagtailmenus.context_processors.wagtailmenus',
            ],
        },
    },
]

WSGI_APPLICATION = PROJECT_NAME + '.wsgi.application'

# -----------------------------------------------------------------------------
# Authentication
# https://docs.djangoproject.com/en/dev/ref/settings/#auth
# -----------------------------------------------------------------------------

if 'wagtail.core' in INSTALLED_APPS:
    LOGIN_URL = '/wagtail/login/'
else:
    LOGIN_URL = '/admin/login/'

AUTH_LDAP_REQUIRE_GROUP = (
    (
        LDAPGroupQuery('cn=kdl-staff,' + LDAP_BASE_OU) | LDAPGroupQuery(
            'cn=ego,' + LDAP_BASE_OU)
    )
)

# -----------------------------------------------------------------------------
# Sessions
# https://docs.djangoproject.com/en/dev/ref/settings/#sessions
# -----------------------------------------------------------------------------

SESSION_COOKIE_AGE = 60 * 60
SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# -----------------------------------------------------------------------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
# https://docs.djangoproject.com/en/dev/ref/settings/#static-files
# -----------------------------------------------------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL.strip('/'))

if not os.path.exists(STATIC_ROOT):
    os.makedirs(STATIC_ROOT)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
    os.path.join(BASE_DIR, 'node_modules'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(STATIC_ROOT, MEDIA_URL.strip('/'))

if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)

# -----------------------------------------------------------------------------
# Installed Applications Settings
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Django Compressor
# http://django-compressor.readthedocs.org/en/latest/
# -----------------------------------------------------------------------------

COMPRESS_ENABLED = True

COMPRESS_CSS_FILTERS = [
    # CSS minimizer
    'compressor.filters.cssmin.CSSMinFilter'
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# -----------------------------------------------------------------------------
# FABRIC
# -----------------------------------------------------------------------------

FABRIC_USER = getpass.getuser()

# -----------------------------------------------------------------------------
# GLOBALS FOR JS
# -----------------------------------------------------------------------------

# Google Analytics ID
GA_ID = ''

# -----------------------------------------------------------------------------
# ActiveCollab Digger
# -----------------------------------------------------------------------------

AC_BASE_URL = 'https://app.activecollab.com/148987'
AC_API_URL = AC_BASE_URL + '/api/v1/'
AC_PROJECT_ID = 982
AC_USER = 36
AC_TOKEN = ''

# -----------------------------------------------------------------------------
# Wagtail
# -----------------------------------------------------------------------------

WAGTAIL_PASSWORD_MANAGEMENT_ENABLED = False
WAGTAIL_PASSWORD_RESET_ENABLED = False

WAGTAIL_SITE_NAME = PROJECT_TITLE

sketchfab_provider = {
    'endpoint': 'https://sketchfab.com/oembed',
    'urls': [
        r'^http(?:s)?://sketchfab\.com/models/.+$',
    ]
}

WAGTAILEMBEDS_FINDERS = [
    # overrides the default oEmbed provider for sketchfab
    {
        'class': 'wagtail.embeds.finders.oembed',
        'providers': [sketchfab_provider],
    },
    # handles all other oEmbed providers the default way
    {
        'class': 'wagtail.embeds.finders.oembed',
    }
]

WAGTAILUSERS_PASSWORD_ENABLED = False
WAGTAILUSERS_PASSWORD_REQUIRED = False

# Wagtail Bakery: https://github.com/wagtail/wagtail-bakery
BUILD_DIR = os.path.join(BASE_DIR, 'build')

BAKERY_VIEWS = (
    'wagtailbakery.views.AllPublishedPagesView',
)

# KDL Wagtail

KDL_WAGTAIL_ITEMS_PER_PAGE = 50
KDL_WAGTAIL_PERSON_MODEL = 'kdl_wagtail_people.Person'

KDL_WAGTAIL_KRACKDOWN_FILTERS = [
    'kdl_wagtail.core.utils.krackdown_anchor',
    'kdl_wagtail.core.utils.krackdown_link',
    'kdl_wagtail.core.utils.krackdown_footnote'
]

KDL_WAGTAIL_ZOTERO_COLLECTION = ''
KDL_WAGTAIL_ZOTERO_LIBRARY_ID = ''
KDL_WAGTAIL_ZOTERO_LIBRARY_TYPE = ''
KDL_WAGTAIL_ZOTERO_NOTE_STYLE = 'chicago-fullnote-bibliography'
KDL_WAGTAIL_ZOTERO_SHORTNOTE_STYLE = 'chicago-note-bibliography'
KDL_WAGTAIL_ZOTERO_TOKEN = ''

# -----------------------------------------------------------------------------
# Automatically generated settings
# -----------------------------------------------------------------------------

# Check which db engine to use:
db_engine = 'django.db.backends.postgresql_psycopg2'
