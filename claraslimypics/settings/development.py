# -*- coding: utf-8 -*-
from .base import *

INSTALLED_APPS += [
    # required by allauth
    'allauth',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
]

SITE_ID = 1
