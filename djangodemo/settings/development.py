from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'medica',
        'USER': 'root',
        'PASSWORD': 'Ma$terkey1',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}