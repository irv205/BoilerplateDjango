import os
import environ
from datetime import timedelta
from pathlib import Path

def getenv(hash):

    env = environ.Env()
    env.read_env(env.str('ENV_PATH', '.env'))

    try:
        val = env(hash)
        if val == 'True': val = True
        else: val == False

        return val
    except KeyError:
        error_msg = "Add the {} environment variable".format(hash)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv('DEBUG')
APP_NAME = getenv('APP_NAME')
SERVER_URL = getenv('SERVER_URL')

#Auth
AUTH_USER_MODEL = 'user.User'

ALLOWED_HOSTS = ['*']


#Email Config
EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_USER = getenv('EMAIL_USER')
EMAIL_PASSWORD = getenv('EMAIL_PASSWORD')
EMAIL_PORT = getenv('EMAIL_PORT')
EMAIL_USE_TLS = getenv('EMAIL_USE_TLS')

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APP = [
    'corsheaders',
    'django_filters',
    'rest_framework',
    'import_export',
]

MY_APPS = [
    'apps.user',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APP + MY_APPS

#Reference JWT:
#https://medium.com/django-rest/django-rest-framework-jwt-authentication-94bee36f2af8

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(days=7),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=7),
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    #'EXCEPTION_HANDLER': 'common.exception_handler.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'common.pagination.PageNumberPagination',
    'PAGE_SIZE': getenv('PAGINATION'),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

#CORS
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'myproject.urls'

#template
SETTINGS_PATH = os.path.dirname(os.path.abspath(__file__))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            (os.path.join(SETTINGS_PATH, 'templates'))
        ],
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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': getenv('DB_HOST'),
        'NAME': getenv('DB_NAME'),
        'USER': getenv('DB_OWNER'),
        'PASSWORD': getenv('DB_PASSWORD'),
        'PORT': getenv('DB_PORT')
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

#Add Logs
#Generar un archivo logs que captura todo el trafico

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

AWS_ENABLE = getenv("AWS_ENABLE")

if AWS_ENABLE:

    print('use aws s3')

    AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_CLOUD_FRONT_URL = getenv('AWS_CLOUD_FRONT_URL')
    AWS_REGION = getenv('AWS_REGION')
    AWS_LOCATION = 'static'
    if AWS_CLOUD_FRONT_URL:
        AWS_S3_CUSTOM_DOMAIN = '%s' % AWS_CLOUD_FRONT_URL
    else:
        AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    # AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_ENCRYPTION = True

    # Static files
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_S3_BUCKET_NAME_STATIC = getenv('AWS_STORAGE_BUCKET_NAME')

    if AWS_CLOUD_FRONT_URL:
        STATIC_URL = "https://%s/" % (AWS_CLOUD_FRONT_URL)
    else:
        STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STORAGE_BUCKET_NAME)

    # Media files
    DEFAULT_FILE_STORAGE = 'project.storage_backends.MediaStorage'

else: 
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_URL = '/media/'
    MEDIA_ROOT=os.path.join(BASE_DIR, "media")

SITE_ID = 2
