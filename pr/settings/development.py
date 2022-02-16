from pr.settings.base import *

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'redmine',
        'USER': 'redmine',
        'PASSWORD': 'redminepass',
        'HOST': 'postgresql',
        'PORT': '5432'
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'management',
    'django_extensions',
    # 'skillsmatrix.apps.SkillsmatrixConfig',
    #'cas',
    'mozilla_django_oidc',
]

USE_TZ = False