"""
Django settings for rabbit project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path helper
location = lambda x: os.path.join(BASE_DIR, x)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mlvawq4hpnoex78@xpc_s5@nh)554zp)n&0=9b48(2g#5j*io^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

MANAGERS = (('Manager', 'manager@roofmedia.mx'), ('Oswald', 'oswaldo_alca@mucha-web.com'),)


# Email settings
EMAIL_HOST = 'mail.roofmedia.mx'

EMAIL_USE_TLS = True

EMAIL_PORT = 587


DYNAMIC_FORMS_EMAIL_HIDDEN_RECIPIENTS = 'oswaldo_alca@mucha-web.com, oswaldoalca@gmail.com, info@roofmedia.mx'

DEFAULT_FROM_EMAIL = 'admin@roofmedia.mx'

FEEDBACK_EMAIL_CONFIRMATION = False


# Application definition

INSTALLED_APPS = (
    #'admin_tools_stats',
    #'django_nvd3',
    #'djangobower',
    #'mediagenerator',
    #'admintools_bootstrap',
    #'admin_tools',
    #'admin_tools.theming',
    #'admin_tools.menu',
    #'admin_tools.dashboard',
    #'django_admin_bootstrapped',
    #'grappelli',
    'jet.dashboard',
    'jet',
    'django.contrib.admin',#.apps.SimpleAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #'adminplus',
    'admin_views',
    'captcha',
    'content',
    'mptt',
    'django_mptt_admin',
    'sorl.thumbnail',
    'dynamic_forms',
    'dynamic_forms.contrib.simple_captcha',
    'widget_tweaks',
    'taggit',
    'nocaptcha_recaptcha',
    'secretballot',
    'likes',
    'feedback_form',
    'analytics',
    'mailqueue',
)

# App configs

#mailqueu
MAILQUEUE_QUEUE_UP = True

#taggit
TAGGIT_CASE_INSENSITIVE = True

NORECAPTCHA_SITE_KEY = '6LcubA0TAAAAADJpvkzqT5GEWqBKnbupiYsrWJMT'

NORECAPTCHA_SECRET_KEY = '6LcubA0TAAAAADU6flcOh8h_CxNQ3p671gsJuGs6'

#jet admin
#JET_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultIndexDashboard'

#jet_admin_views
ADMIN_VIEWS_URL_PREFIX = "/intranetRoof"

#admin_tools
#ADMIN_TOOLS_THEMING_CSS = 'admin_tools/styles/theming.css'

#ADMIN_TOOLS_MENU = 'menu.CustomMenu'

#ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

# Django-bower
# ------------

# Specifie path to components root (you need to use absolute path)
#BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')

#BOWER_PATH = '/usr/local/bin/bower'

#BOWER_INSTALLED_APPS = (
#    'd3#3.3.13',
#    'nvd3#1.7.1',
#)



#feedback
FROM_EMAIL = 'feedback@roofmedia.mx'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'dynamic_forms.middlewares.FormModelMiddleware',
    'secretballot.middleware.SecretBallotIpUseragentMiddleware',
    'likes.middleware.SecretBallotUserIpUseragentMiddleware',
)

ROOT_URLCONF = 'rabbit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #location('templates'),
        ],
        #'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                #'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'content.context_processors.get_category_nodes',
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                'django.template.context_processors.request',

            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

#------- Message-boostrap compatibility---------------------
from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
                message_constants.INFO: 'info',
                message_constants.SUCCESS: 'success',
                message_constants.WARNING: 'warning',
                message_constants.ERROR: 'danger'}

WSGI_APPLICATION = 'rabbit.wsgi.application'

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'roofdata',
        'USER': 'roof',
        #'PASSWORD': 'sword',
        'HOST': '198.199.110.115',
        'PORT': '5432',
    }
    #'default': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'roofmedia',
    #    'USER': 'roof',
    #    'PASSWORD': 'st$yh65KNe1',
    #    'HOST': '198.199.110.115',   # Or an IP Address that your DB is hosted on
    #    'PORT': '3306',
    #}
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGES = (
    ('es-MX', 'Spanish'),
)

LOCALE_PATHS = (
#    os.path.join(BASE_DIR, 'sales', 'locale'),
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #'/home/jose/dev/djangodev/rabbit/rabbit/static'
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    #'djangobower.finders.BowerFinder',
)


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#from admintools_bootstrap import ADMIN_MEDIA_BUNDLES

#MEDIA_BUNDLES = ADMIN_MEDIA_BUNDLES



try:
    from settings_local import *
except ImportError:
    pass
