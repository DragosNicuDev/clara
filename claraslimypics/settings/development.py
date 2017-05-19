# -*- coding: utf-8 -*-
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DATABASE_NAME'),
        'USER': get_env_variable('DATABASE_USER'),
        'PASSWORD': get_env_variable('DATABASE_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS += [
    # required by allauth
    'allauth',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',

    'crispy_forms',

    'photo',
]

# The tyoe of content that is allowed to be uploaded
CONTENT_TYPES = ['image']

# Limit uploads to 0.5MB
MAX_UPLOAD_SIZE = 524288

CRISPY_TEMPLATE_PACK = 'bootstrap3'

SITE_ID = 1

MEDIA_URL = '/media_cdn/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")
