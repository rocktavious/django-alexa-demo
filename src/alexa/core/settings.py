"""
Django settings for parlour server.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os
import sys
import ast
import datetime
import dj_database_url
from django.contrib import messages


PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), os.pardir))

sys.path.insert(0, os.path.normpath(os.path.join(PROJECT_ROOT, os.pardir)))

SECRET_KEY = '(*c8a72()5%75e@eyg#@0=zd^pl!7=y@'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

APPEND_SLASH = True

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

DEBUG = ast.literal_eval(os.environ.get('DEBUG', 'True'))
DEBUG_TOOLBAR_PATCH_SETTINGS = False
TEMPLATE_DEBUG = True
MAINTENANCE = False

ALLOWED_HOSTS = [
    'alexa.rocktavious.com',
]

# The order in which the apps load determines the overriden templates loading
INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'bootstrap3',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'debug_toolbar',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_expiring_authtoken',
    'rest_framework_swagger',
    'django_extensions',
    'django_alexa',
    'alexa.core',
    'alexa.potter',
    'alexa.presentation',
    'alexa.jarvis',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'alexa.core.urls'

WSGI_APPLICATION = 'alexa.core.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///%s/database.sqlite' % PROJECT_ROOT)
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

STATIC_ROOT = '/static'
MEDIA_ROOT = '/tmp/alexa-media'
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                "django.core.context_processors.debug",
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                "django.core.context_processors.static",
                "django.core.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.core.context_processors.request",
                "django.contrib.auth.context_processors.auth",
            ),
        }
    },
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] %(name)s.%(funcName)s, line %(lineno)d | %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'level': 'ERROR',
            'handlers': ['console'],
        },
        'django_alexa': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'alexa': {
            'level': 'INFO',
            'handlers': ['console'],
        },
    },
}

# override tag name for bootstrap 3
MESSAGE_TAGS = {
    messages.INFO: 'alert-info info',
    messages.SUCCESS: 'alert-success success',
    messages.WARNING: 'alert-warning warning',
    messages.ERROR: 'alert-danger error'
}

LOGIN_URL = "/login"
LOGIN_REDIRECT_URL = "/admin"

REST_FRAMEWORK = {}
# we use a custom jquery url so we can work in offline mode
DEBUG_TOOLBAR_CONFIG = {
    # Toolbar options
    'SHOW_COLLAPSED': True,
    'SHOW_TOOLBAR_CALLBACK': 'alexa.core.debug_toolbar.show_toolbar',
    'JQUERY_URL': '/static/core/js/jquery-1.11.2.min.js',
}

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

EXPIRING_TOKEN_LIFESPAN = datetime.timedelta(days=7)

SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': 'v1',
    'api_path': '/',
    'api_key': '',
    'is_authenticated': False,
    'is_superuser': False,
    'permission_denied_handler': None,
    'resource_access_handler': None,
    'info': {
        'contact': 'kyle.rockman@mac.com',
        'description': 'Rockman Alexa API',
        'title': 'Rockman Alexa API',
    },
    'doc_expansion': 'list',
}
