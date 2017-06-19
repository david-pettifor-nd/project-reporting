from pr.settings.base import *

SECRET_KEY = 'hwqm-j5hk80(boz%uy_wy+h)ouye*6dyjl&h17fn7xf$_#1095'
DEBUG = False


ALLOWED_HOSTS = ['turbo.crc.nd.edu']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'redmine_default',
        'USER': 'redmine_system',
        'PASSWORD': 'Lets go turbo!',
        'HOST': 'turbo.crc.nd.edu',
        'PORT': '5432'
    }
}

LOGIN_URL = '/reports/login/'
LOGOUT_URL = '/reports/logout/'

CAS_REDIRECT_URL = '/reports/home/'
CAS_IGNORE_REFERER = True
CAS_SERVER_URL = 'https://login.nd.edu/cas/login'
CAS_AUTO_CREATE_USERS = False


#AUTHENTICATION_BACKENDS = (
#    'django.contrib.auth.backends.ModelBackend',
#    'cas.middleware.CASMiddleware',
#)

CAS_REDIRECT_URL = '/reports/home/'
CAS_IGNORE_REFERER = True
CAS_SERVER_URL = 'https://login.nd.edu/cas/login'
CAS_AUTO_CREATE_USERS = False

