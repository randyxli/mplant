from mplant.settings.base import *
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mplant',
        'USER': 'mplant',
        'PASSWORD': 'mplant',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}