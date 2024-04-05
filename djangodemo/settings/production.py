from .base import *

CORS_ALLOWED_ORIGINS = ("http://localhost:3000", "http://localhost:8000",)
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]

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