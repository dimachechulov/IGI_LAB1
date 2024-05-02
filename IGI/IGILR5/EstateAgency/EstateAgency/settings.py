"""
Django settings for EstateAgency project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_78z27=7#&u^oypc357xt5@cph1sdy)3c5hn(dc+^&46o#ti$1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


AUTH_USER_MODEL ='agency.User'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'agency',
    'tz'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'agency.utils.TimezoneMiddleware'
]

ROOT_URLCONF = 'EstateAgency.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'EstateAgency.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CSRF_TRUSTED_ORIGINS = ['http://*', 'https://*']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'agency/static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'store13313@gmail.com'
EMAIL_HOST_PASSWORD = 'mivtrldpigflmwll'
EMAIL_PORT = 587

LOGGING = {
    'version':1,
    'disable_exiting_logger':False,
    'formatters':{
        "standard":{
            "format" : "%(asctime)s %(levelname)s %(name)s %(message)s"
        }
    },
    'handlers':{
        'console': {
            'class' : 'logging.StreamHandler',
            'formatter': "standard",
        },
        'file': {
            'class' : 'logging.FileHandler',
            'formatter': "standard",
            'filename' : "EstateAgency\info.log"
        }
    },
    'loggers':{
        'main':{
            'handlers' : ['console', 'file'],
            'level' : 'DEBUG',
            'propagate' : True,
        }
    }
}


STRIPE_PUBLIC_KEY='pk_test_51MuzOWFO8xyXT4lxSNPtWf1a6XjaDjElcpqpQ3XVE3UaMfcyDWPBP6Vnjijwf6ATdKoI5gLWG6xYWBjTs9LPLnQ800ag9A4ic5'
STRIPE_SECRET_KEY='sk_test_51MuzOWFO8xyXT4lxbZ3IRv7iIqHk0IJ8bcnKyl7HTcbDGmmEDayJgakgsj2vvgEou4R8o5rTBC9NpuwKnx72taNl00BgE47KbI'
STRIPE_WEBHOOK_SECRET='whsec_1b7f1ca18c6e4ca2995958d28097e6dfe3d280b1b7b4606a0f0c3696affba753'


TIME_ZONE = "UTC"


