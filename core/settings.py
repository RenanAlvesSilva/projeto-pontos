from pathlib import Path
import os
from django.contrib.messages import constants as messages
import pytz
from django.conf.locale.pt_BR import formats as br_formats
from decouple import config
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DATABASE_URL = config('DATABASE_URL')
DEBUG = config('DEBUG', default = False, cast= bool)

ALLOWED_HOSTS = ['*']

#Apps Padrão Django
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

#APS DE TERCEIROS
THIRD_PARTY_APPS = [
    'django_filters',
]

#Meus Apps
MY_APPS = [
    'Base',
    'Adm',
    'Controle'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + MY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Base.middleware.UserGroupMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR , 'templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'


DATABASES = {
    'default':dj_database_url.config(default= DATABASE_URL, conn_max_age = 1800)
}


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
HORA_CORRETA = pytz.timezone('America/Sao_Paulo')

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

br_formats.DATE_FORMAT = 'd/m/Y'
br_formats.TIME_FORMAT = 'H:i:s'


CSRF_TRUSTED_ORIGINS = ['https://gerenciamento-rio2parking.up.railway.app',
'https://localhost:8000']

STATIC_URL = 'static/'
STATICFILES_DIR = [
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

WHITENOISE_MAX_AGE = 31536000 

LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'Login'

MESSAGES_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}
