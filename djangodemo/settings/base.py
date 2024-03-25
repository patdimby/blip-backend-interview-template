import os
from pathlib import Path

import environ

env = environ.Env(DEBUG=(bool, False))

BASE_DIR = Path(__file__).resolve().parent.parent.parent

environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS =  ['*']

SITE_ID = 1

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [   
    'django_extensions', 
    "corsheaders",
    'rest_framework',
    'rest_framework.authtoken',
    'drf_spectacular',
    'drf_spectacular_sidecar',  # required for Django collectstatic discovery

    'drf_chunked_upload', # file upload chunk by chunk
    'queued_storage', # file upload queue by queue
    #'djcelery', #  for workers
    'bootstrap5', # bootstrap5 CSS.
]

LOCAL_APPS = [
    'apps.spectacular',
    'apps.users',    
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',

]

ROOT_URLCONF = "djangodemo.urls"

CORS_ALLOWED_ORIGINS = ("http://localhost:3000", "http://localhost:8000",)
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR, "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "djangodemo.wsgi.application"


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
       'rest_framework.permissions.IsAuthenticated', # for authentication.
       #'rest_framework.permissions.AllowAny', # default
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer', ],
    'DEFAULT_PARSER_CLASSES': ['rest_framework.parsers.JSONParser',],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",  # enables get schemas open api 3.
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

# using redis caches.
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Internationalization
LANGUAGE_CODE = env('LANGUAGE_CODE')
TIME_ZONE = env('TIME_ZONE')
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR, "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

SPECTACULAR_SETTINGS = {
    'TITLE': 'Technical questions',
    'DESCRIPTION': """Test organised for basic comprehension of work.
    There are more responses but for avoiding a large video file, and taking less
    time, keep responses simple.""",
    'VERSION': '1.1.0',
    'SERVE_INCLUDE_SCHEMA': False,
    
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
        "displayOperationId": True,

    },
    # default "SWAGGER_UI_DIST": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest",
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    # OTHER SETTINGS    

}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
