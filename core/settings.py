"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os

from django.conf import settings
from celery.schedules import crontab

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m44%%^%sua=@y+^x8ohs*^410#71b7@6+7rs_!$&pv6pd9(38z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    # 'django_crontab',
    'clearcache',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',

    'django_celery_beat',

    'account.apps.AccountConfig',
    'mehsullar.apps.MehsullarConfig',
    'company.apps.CompanyConfig',
    'maas.apps.MaasConfig',
    'gunler.apps.GunlerConfig',

    'django_extensions',
    'django_filters',
    'rest_auth',
]

SIMPLE_JWT = {
    # When set to True, if a refresh token is submitted to the TokenRefreshView, a new refresh token will be returned along with the new access token.
    'ROTATE_REFRESH_TOKENS': True,
    # refresh tokens submitted to the TokenRefreshView to be added to the blacklist
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',  # TWO types either HMAC  or RSA for HMAC 'HS256', 'HS384', 'HS512: SIGNING_KEY setting will be used as both the signing key and the verifying key.  asymmetric RSA RS256', 'RS384', 'RS512' SIGNING_KEY setting must be set to a string that contains an RSA private key. Likewise, the VERIFYING_KEY
    'SIGNING_KEY': settings.SECRET_KEY,  # content of generated tokens.
    # The verifying key which is used to verify the content of generated tokens
    'VERIFYING_KEY': None,
    # The audience claim to be included in generated tokens and/or validated in decoded tokens
    'AUDIENCE': None,
    'ISSUER': None,  # ssuer claim to be included in generated tokens

    # Authorization: Bearer <token> ('Bearer', 'JWT')
    'AUTH_HEADER_TYPES': ('Bearer',),
    # The database field from the user model that will be included in generated tokens to identify users.
    'USER_ID_FIELD': 'id',
    # value of 'user_id' would mean generated tokens include a “user_id” claim that contains the user’s identifier.
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    # The claim name that is used to store a token’s type
    'TOKEN_TYPE_CLAIM': 'token_type',

    # The claim name that is used to store a token’s unique identifier.
    'JTI_CLAIM': 'jti',
    # which specifies how long access tokens are valid
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    # how long refresh tokens are valid.
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'crm',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Baku'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

AUTH_USER_MODEL = 'account.User'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CELERY STUFF
CELERY_BROKER='redis://redis:6379/0'
CELERY_RESULT_BACKEND='redis://redis:6379/0'

# BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Baku'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

CELERYBEAT_SCHEDULE = {
    "maas_goruntuleme_create_task": {
        "task": "maas_goruntuleme_create_task",
        "schedule": crontab(0,0,'*', day_of_month="1"),
    },
    "maas_goruntuleme_create_task_15": {
        "task": "maas_goruntuleme_create_task_15",
        "schedule": crontab(0,0,'*', day_of_month="15"),
    },
    "work_day_creater_task20": {
        "task": "work_day_creater_task20",
        "schedule": crontab(0, 0, '*', day_of_month="20"),
    },
    "work_day_creater_task25": {
        "task": "work_day_creater_task25",
        "schedule": crontab(0, 0, '*', day_of_month="25"),
    },

    "work_day_creater_holding_task20": {
        "task": "work_day_creater_holding_task20",
        "schedule": crontab(0, 0, '*', day_of_month="20"),
    },
    "work_day_creater_holding_task25": {
        "task": "work_day_creater_holding_task25",
        "schedule": crontab(0, 0, '*', day_of_month="25"),
    },

    "work_day_creater_shirket_task20": {
        "task": "work_day_creater_shirket_task20",
        "schedule": crontab(0, 0, '*', day_of_month="20"),
    },
    "work_day_creater_shirket_task25": {
        "task": "work_day_creater_shirket_task25",
        "schedule": crontab(0, 0, '*', day_of_month="25"),
    },

    "work_day_creater_ofis_task20": {
        "task": "work_day_creater_ofis_task20",
        "schedule": crontab(0, 0, '*', day_of_month="20"),
    },
    "work_day_creater_ofis_task25": {
        "task": "work_day_creater_ofis_task25",
        "schedule": crontab(0, 0, '*', day_of_month="25"),
    },

    "work_day_creater_shobe_task20": {
        "task": "work_day_creater_shobe_task20",
        "schedule": crontab(0, 0, '*', day_of_month="20"),
    },
    "work_day_creater_shobe_task25": {
        "task": "work_day_creater_shobe_task25",
        "schedule": crontab(0, 0, '*', day_of_month="25"),
    },

    "work_day_creater_komanda_task20": {
        "task": "work_day_creater_komanda_task20",
        "schedule": crontab(0, 0, '*', day_of_month="20"),
    },
    "work_day_creater_komanda_task25": {
        "task": "work_day_creater_komanda_task25",
        "schedule": crontab(0, 0, '*', day_of_month="25"),
    },

    "work_day_creater_vezife_task20": {
        "task": "work_day_creater_vezife_task20",
        "schedule": crontab(0, 0, '*', day_of_month="20"),
    },
    "work_day_creater_vezife_task25": {
        "task": "work_day_creater_vezife_task25",
        "schedule": crontab(0, 0, '*', day_of_month="25"),
    },
}