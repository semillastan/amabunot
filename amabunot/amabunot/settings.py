# Django settings for blank project.
import os
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Stanley Semilla', 'semillastan@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Asia/Manila'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = False

MEDIA_ROOT = os.path.join(ROOT_DIR, '..', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(ROOT_DIR, '..', 'static')
STATIC_URL = '/static/'

UPLOAD_DIR = 'uploads'
UPLOAD_ROOT = os.path.join(MEDIA_ROOT, UPLOAD_DIR)
UPLOAD_URL = MEDIA_URL + UPLOAD_DIR + '/'

from django.core.files.storage import FileSystemStorage
UPLOAD_STORAGE = FileSystemStorage(location=UPLOAD_ROOT, base_url=UPLOAD_URL)

ADMIN_MEDIA_PREFIX = '/static/admin'
#ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

STATICFILES_DIRS = (
	
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '18v@3d2oucxmza3rztn^)2p!7!y1bt35&amp;(!101$w-j(7*(#@hw'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
	'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    'django.contrib.auth.context_processors.auth',
)

#GRAPPELLI_ADMIN_TITLE = 'UP ITDC Human Resource Information System'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


AUTH_PROFILE_MODULE = 'accounts.UserProfile'
ROOT_URLCONF = 'amabunot.urls'

TEMPLATE_DIRS = (
	os.path.join(ROOT_DIR, '..', 'templates'),
)

#FIXTURE_DIRS = (
#	os.path.join(ROOT_DIR, '..', 'fixtures'),
#)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'grappelli',
    'django.contrib.admin',
    
    'south',
    'accounts',
    'core',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

"""
# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'hris.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'itdchris', # Or path to database file if using sqlite3.
        'USER': 'rodxavier', # Not used with sqlite3.
        'PASSWORD': 'rodxavierdbpassword1234567890', # Not used with sqlite3.
        'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

LOGIN_REDIRECT_URL = 'http://itdc.bodegapps.com/dashboard'
#"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'hris.upitdc@gmail.com'
EMAIL_HOST_PASSWORD = 'barbecue-IT'
EMAIL_USE_TLS = True
SERVER_EMAIL = 'hris.upitdc@gmail.com'
SEND_BROKEN_LINK_EMAILS = 'True'

#"""
try:
   from local_settings import *
except ImportError:
    raise ImportError('Please provide your own localsettings.py.\n'
                 'Refer to localsettings.py.template for an example')
#"""
