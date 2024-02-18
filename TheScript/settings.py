from pathlib import Path
import os
import socket
import dj_database_url 
from django.http import HttpRequest
from urllib.parse import quote
import mimetypes
# from google.oauth2 import service_account
# from storages.backends.s3boto3 import S3Boto3Storage

from storages.backends.s3boto3 import S3Boto3Storage

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

mimetypes.add_type("text/javascript", ".js", True)



# ... (existing code)

# Initialize Firebase


# Configure the storage bucket
# FIREBASE_BUCKET = storage.bucket(app=firebase_admin.get_app(name='image_upload_app'))


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

# Your password
password = "TheScript.2404"

# Percent-encode the password
encoded_password = quote(password)

# Construct the connection string
connection_string = f"postgres://postgres.gyuxjtoltljhfuguvtlv:{encoded_password}@aws-0-eu-central-1.pooler.supabase.com:6543/postgres"

# Set the DATABASE_URL environment variable
os.environ["DATABASE_URL"] = connection_string

# Use dj_database_url to parse the connection string
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

# Set the path to the service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(BASE_DIR, 'key.json')





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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'assets'


# Define MEDIA_ROOT and other settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
UPLOAD_ROOT = '/media/upload'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Backblaze B2 configurations
AWS_ACCESS_KEY_ID = '0050bf0f76bf18d0000000002'
AWS_SECRET_ACCESS_KEY = 'K0058/HuAOAQsR0UZPz3sD+JLAidkY0'
AWS_STORAGE_BUCKET_NAME = 'Thscript'

# Optional configurations
AWS_S3_REGION_NAME = 'us-east-1'  
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_REGION_NAME}.backblazeb2.com'

# Optional: Set the location within the bucket
AWS_LOCATION = 'static'

# Static and media URLs
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"

CKEDITOR_UPLOAD_PATH = "uploads/"

