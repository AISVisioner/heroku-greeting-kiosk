""" Production Settings """

# import os
# import dj_database_url
from .base import *

############
# DATABASE #
############
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.getenv('DATABASE_URL')
#     )
# }


############
# SECURITY #
############

DEBUG = False # bool(os.getenv('DJANGO_DEBUG', ''))

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    # Set to your Domain here (eg. 'yourwebsite.com')
    ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'greetingkiosk.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'greeting_kiosk',
        'USER': 'aisvisioner',
        'PASSWORD': 'aisvisioner',
        'HOST': 'localhost',
        'PORT': 5432,
    },
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)