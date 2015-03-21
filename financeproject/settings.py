"""
Django settings for financeproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.insert(0, '/home/gsl/financeproject')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '54_cr33_ay(0$w14du^+-z_6w071nqjana28aq-t*anp7088sp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


mysql_name = 'finance_db'
mysql_user = 'finance_account'
mysql_pass = 'finance_passwd'
mysql_host = ''
mysql_host_s = ''
mysql_port = ''


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'madmin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'financeproject.urls'

WSGI_APPLICATION = 'financeproject.wsgi.application'



## session setting
SESSION_ENGINE = "django.contrib.sessions.backends.file"


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': mysql_name,                      # Or path to database file if using sqlite3.
        'USER': mysql_user,                      # Not used with sqlite3.
        'PASSWORD': mysql_pass,                  # Not used with sqlite3.
        'HOST': mysql_host,                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': mysql_port,                      # Set to empty string for default. Not used with sqlite3.
    },

    'slave': {
        'ENGINE': 'django.db.backends.mysql',   # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': mysql_name,                      # Or path to database file if using sqlite3.
        'USER': mysql_user,                      # Not used with sqlite3.
        'PASSWORD': mysql_pass,                  # Not used with sqlite3.
        'HOST': mysql_host_s,                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': mysql_port,                      # Set to empty string for default. Not used with sqlite3.
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


## logging

LOGGING_FILE = os.path.join(BASE_DIR, 'log/logfile')
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=LOGGING_FILE,
                    filemode='w')


