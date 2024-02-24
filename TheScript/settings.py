from pathlib import Path
import socket
import dj_database_url 
from django.http import HttpRequest
from urllib.parse import quote
import mimetypes

import firebase_admin
from firebase_admin import storage
from firebase_admin import credentials, initialize_app, storage

import os
from google.oauth2 import service_account


from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

mimetypes.add_type("text/javascript", ".js", True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3=#&rp*)q1+@5zefhf-@++mr5sq*^84d84oqk%)$yho_-9i%@('

# SECURITY WARNING: don't run with debug turned on in production!

hostname = socket.gethostname()

if hostname in ['localhost','127.0.0.1']:
    DEBUG = False
else:
    DEBUG = False


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
    'livereload',
    
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


# Define your password
password = os.environ.get('POSTGRES_PASSWORD')

# Percent-encode the password
encoded_password = quote(password)

# Construct the connection string for PostgreSQL
connection_string = f"postgres://postgres.gyuxjtoltljhfuguvtlv:{encoded_password}@aws-0-eu-central-1.pooler.supabase.com:6543/postgres"

# Set the DATABASE_URL environment variable (for production)
os.environ["DATABASE_URL"] = connection_string

# Define your local SQLite database configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# If in production, use PostgreSQL configured via DATABASE_URL
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config()


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

CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"},
    "django-backblaze-b2": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Africa/Lusaka'

USE_I18N = True

USE_TZ = True

BACKBLAZE_CONFIG = {
    'application_key_id': os.environ.get('B2_APPLICATION_KEY_ID'),
    'application_key': os.environ.get('B2_APPLICATION_KEY'),
    "bucket": os.environ.get("BACKBLAZE_BUCKET"),
}

# Define MEDIA_ROOT and other settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
UPLOAD_ROOT = '/media/upload'


# this is where Django *looks for* static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# this is where static files are *collected*
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# this is the *URL* for static files
STATIC_URL = '/static/'

DEFAULT_FILE_STORAGE = 'django_backblaze_b2.BackblazeB2Storage'


# Backblaze B2 configurations
CKEDITOR_UPLOAD_PATH = "uploads/"


CKEDITOR_JQUERY_URL = 'https://code.jquery.com/jquery-3.6.0.min.js'  # or use a local path
CKEDITOR_UPLOAD_PATH = 'uploads/'  # define the path for uploaded media files


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'