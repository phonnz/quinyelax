"""
Django settings for quinyelax project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^@qj38c$_z#3g3b)_vzp$=ih$dla*51gee_5!#f9coa4n*x%p6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quinyelax'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'quinyelax.urls'

WSGI_APPLICATION = 'quinyelax.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'heroku_def8bd258b9a2f5',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'b24e30407e8f86',
        'PASSWORD': 'b7b12203',
        'HOST': 'us-cdbr-east-06.cleardb.net',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', 
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'quinyelax',                      # Or path to database file if using sqlite3.
#         # The following settings are not used with sqlite3:
#         'USER': 'root',
#         'PASSWORD': 'adminadmin',
#         'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
#         'PORT': '', 
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


#Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mensajes@nyxtechnology.com'
EMAIL_HOST_PASSWORD = 'NyxT3ch!'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'registro@festivalcervantino.gob.mx'
SERVER_EMAIL = 'mensajes@nyxtechnology.com'