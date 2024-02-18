from pathlib import Path
import os
import socket
import dj_database_url 
from django.http import HttpRequest
from urllib.parse import quote
import mimetypes
from storages.backends.s3boto3 import S3Boto3Storage

mimetypes.add_type("text/javascript", ".js", True)


hostname = socket.gethostname()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3=#&rp*)q1+@5zefhf-@++mr5sq*^84d84oqk%)$yho_-9i%@('

# SECURITY WARNING: don't run with debug turned on in production!
# if hostname == 'localhost' or hostname == '127.0.0.1':
#     DEBUG = True  # Development environment
# else:
#     DEBUG = False  # Production environment
if os.environ.get('DJANGO_SETTINGS_MODULE') == 'production':
    DEBUG = False
else:
    DEBUG = True



# if HttpRequest().get_host() == 'thescript.onrender.com':
#     DEBUG = False
#     ALLOWED_HOSTS = ['thescript.onrender.com']
# else:
#     DEBUG = True
#     ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


ALLOWED_HOSTS = ['thescript.onrender.com','127.0.0.1','localhost','www.thscript.site']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Base',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TheScript.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'Base/Templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'TheScript.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# # Your password
# password = "TheScript.2404"

# # Percent-encode the password
# encoded_password = quote(password)

# # Construct the connection string
# connection_string = f"postgres://postgres.gyuxjtoltljhfuguvtlv:{encoded_password}@aws-0-eu-central-1.pooler.supabase.com:6543/postgres"

# # Set the DATABASE_URL environment variable
# os.environ["DATABASE_URL"] = connection_string

# # Use dj_database_url to parse the connection string
# DATABASES = {
#     'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
# }

# DATABASES = {
#     'default':{
#         'ENGINE':'django.db.backends.postgresql_psycopg2',
#         'NAME': "postgres",
#         'USER': "postgres",
#         'PASSWORD':"Amtx8CaYDwuhcsRH",
#         'HOST': "db.gyuxjtoltljhfuguvtlv.supabase.co",
#         'PORT':"5432"
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Africa/Lusaka'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# this is where Django *looks for* static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# this is where static files are *collected*
STATIC_ROOT = BASE_DIR / 'assets'

# this is the *URL* for static files
STATIC_URL = '/static/'

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Django upgrade).
# See https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
# Deprecated in Django 4.2: STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
# New in Django 4.2: https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-STORAGES

# ------ For development
# STORAGES = {
#     "default": {
#         "BACKEND": "django.core.files.storage.FileSystemStorage",
#     },
#     "staticfiles": {
#         "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
#     },
# }

# ------ For production
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ------ For development

MEDIA_URL = '/media/'

# ------ For production

# AWS_ACCESS_KEY_ID = 'AKIARS64NUXBYCRUXIZK'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'thescriptbucket'
# AWS_QUERYSTRING_AUTH = False

# incorporationg Backblaze B2 Cloud Storage
# ref: https://github.com/jschneier/django-storages/issues/765#issuecomment-699487715

# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_ACCESS_KEY_ID = "0050bf0f76bf18d0000000002"
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_SECRET_ACCESS_KEY = "K0058/HuAOAQsR0UZPz3sD+JLAidkY0"
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_STORAGE_BUCKET_NAME = "Thscript"
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_QUERYSTRING_AUTH = False
# DO NOT change these unless you know what you're doing.
_AWS_EXPIRY = 60 * 60 * 24 * 7
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate"}
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_S3_REGION_NAME = "us-east-005"
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#cloudfront
AWS_S3_CUSTOM_DOMAIN = "f004.backblazeb2.com/file/Thscript/Thscript"
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_S3_ENDPOINT_URL = "https://Thscript.s3.us-east-005.backblazeb2.com"
AWS_S3_FILE_OVERWRITE = False
aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.backblaze.com"

MEDIA_URL = f"https://{aws_s3_domain}/media/"

CKEDITOR_JQUERY_URL = 'https://code.jquery.com/jquery-3.6.0.min.js'  # or use a local path
CKEDITOR_UPLOAD_PATH = 'uploads/'  # define the path for uploaded media files


# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'