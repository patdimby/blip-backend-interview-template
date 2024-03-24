from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env('DB_NAME'),
        "USER": env('DB_USER'),
        "PASSWORD": env('DB_PASS'),
        "HOST": env('DB_PASS'),
        "PORT": env('DB_PORT'),
    }
}