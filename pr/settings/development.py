from pr.settings.base import *

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'redmine',
        'USER': 'postgres',
        'PASSWORD': "Let's go turbo!",
        'HOST': 'database1',
        'PORT': '5432'
    }
}
