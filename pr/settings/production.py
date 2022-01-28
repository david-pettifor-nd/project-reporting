from pr.settings.base import *

SECRET_KEY = 'vhy%=dl-f4g=q==0sfn-nzmquk=@fza%#y=+r98r3meflu4zg2'
DEBUG = False


ALLOWED_HOSTS = ['redmine.crc.nd.edu','redmine-new.crc.nd.edu']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'redmine',
        'USER': 'redmine',
        'PASSWORD': 'redminepass',
        'HOST': 'database1',
        'PORT': '5432'
    },
    'staff': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'redmine',
        'USER': 'crc_staff',
        'PASSWORD': 'resolutions are the same',
        'HOST': 'database1',
        'PORT': '5432'
    }
}

#CAS_REDIRECT_URL = '/reports/home/'
#CAS_IGNORE_REFERER = True
#CAS_SERVER_URL = 'https://login.nd.edu/cas/login'
#CAS_AUTO_CREATE_USERS = False

LOGIN_URL = '/reports/oidc/authenticate/'
LOGIN_REDIRECT_URL = '/reports/home/'
LOGOUT_REDIRECT_URL = '/reports/home/'

# OIDC (Okta) authentication
_OIDC_BASE_URL = 'https://okta.nd.edu/oauth2/ausxosq06SDdaFNMB356/v1'
OIDC_RP_CLIENT_ID = '0oa2z5gv7bixc4wDi357'
OIDC_RP_CLIENT_SECRET = 'qFz0Z6vhp0hfP3dxeJ4Hr6Y6T_p8LpWTbpFB8iMu'

OIDC_OP_AUTHORIZATION_ENDPOINT = "{}/authorize".format(_OIDC_BASE_URL)
OIDC_OP_TOKEN_ENDPOINT = "{}/token".format(_OIDC_BASE_URL)
OIDC_OP_USER_ENDPOINT = "{}/userinfo".format(_OIDC_BASE_URL)

OIDC_RP_SIGN_ALGO = "RS256"
OIDC_OP_JWKS_ENDPOINT = "{}/keys".format(_OIDC_BASE_URL)

OIDC_OP_LOGOUT_URL_METHOD = "users.provider_logout"
OIDC_OP_LOGOUT_ENDPOINT = "{}/logout".format(_OIDC_BASE_URL)

# This setting restricts Django from creating new users upon first login to okta
OIDC_CREATE_USER = False #ENV.bool('DJANGO_OIDC_CREATE_USER', default=False)  # Default is True in OIDC library

# This is the middleware setting to say how often to check for valid okta session.
OIDC_RENEW_ID_TOKEN_EXPIRY_SECONDS = 900 #ENV.int('DJANGO_OIDC_RENEW_ID_TOKEN_EXPIRY_SECONDS', default=900)

# We have to store the ID token (not the access token) to do a provider logout.
OIDC_STORE_ID_TOKEN = True
OIDC_VERIFY_SSL = False

AUTHENTICATION_BACKENDS = (
    #'django.contrib.auth.backends.ModelBackend',
    #'cas.backends.CASBackend',
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
)

FORCE_SCRIPT_NAME = '/reports/'

