import os
from .default import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='^92l&5_l2f-ik5xlav!7*cat904fro-lmdd@0kgz@c*nxua3@p')
DEBUG = env.bool('DJANGO_DEBUG', default=True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DJANGO_MYSQL_DB_NAME', default='database'),
        'USER': env('DJANGO_MYSQL_USER', default='root'),
        'HOST': env('DJANGO_MYSQL_URL', default='127.0.0.1'),
        'PASSWORD': env('DJANGO_MYSQL_PASSWORD', default='')
    }
}

SITE_ID = 1
