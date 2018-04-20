from .common import *

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'community_connect',
        'USER': 'community_connect',
        'PASSWORD': 'MY_AWESOME_PASSWORD',
        'HOST': 'localhost',
        # Leaving port black should work, if it doesn't, 5432 should work.
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['*']

DEBUG = True
