from pr.settings.base import *

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'redmine',
        'USER': 'redmine',
        'PASSWORD': 'redminepass',
        'HOST': 'db',
        'PORT': '5432'
    }
}