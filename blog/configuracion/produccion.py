"""
from .base import * 

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""

from .base import *

DEBUG = False
ALLOWED_HOSTS = [*]

import dj_database_url
from decouple import config

DATABASES = {
    'default':dj_database_url.config(
        default =config('DATABASE_URL')) 
    }

STATICFILES_DIRS = (BASE_DIR,'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

