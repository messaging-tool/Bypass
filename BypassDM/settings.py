from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
from decouple import config


# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('DJANGO_SECRET_KEY')
# SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
SECRET_KEY ='django-insecure-my2im41=03e3%hhjni1a6#b+^-#o#_i=zl_fss9oz=4t@4#u57'


# DEBUG = os.environ.get('DEBUG') == "TRUE"

DEBUG = os.environ.get("DJANGO_DEBUG")


DEBUG = False


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config('DJANGO_DEBUG', cast=bool)
# DEBUG = os.environ.get("DJANGO_DEBUG")

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

ALLOWED_HOSTS = ['bypassdms.com', 'bypass-production-b7db.up.railway.app']


# ALLOWED_HOSTS=["127.0.0.1", "localhost", "bypassdms.com", "bypassdm.up.railway.app"]



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'BypassDM_V1',
    'autho',
    'LandingPage',
    'tinymce',
    
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

ROOT_URLCONF = 'BypassDM.urls'

LOGIN_URL = '/autho/twitter_login/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR],
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

WSGI_APPLICATION = 'BypassDM.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'phmWsqvJFZUGPFfb63ss',
        'HOST': 'containers-us-west-198.railway.app',
        'PORT': '6491',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('PGDATABASE'),
#         'USER':os.environ.get('PGUSER'),
#         'PASSWORD':os.environ.get('PGPASSWORD'),
#         'HOST':os.environ.get('PGHOST'),
#         'PORT':os.environ.get('PGPORT')

# }
# }




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'LandingPage/templates/LandingPage/static']



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#TWITTTER SETTINGS
TWITTER_API_KEY='YOUR_API_KEY'
TWITTER_API_SECRET='YOUR_API_SECRET'
TWITTER_CLIENT_ID='YOUR_CLIENT_ID'
TWITTER_CLIENT_SECRET='YOUR_CLIENT_SECRET'
TWITTER_OAUTH_CALLBACK_URL='YOUR_CALLBACK_URL'


# TWITTER_API_KEY='593NrAcO26W8hOcLb3wdnnRhR'
# TWITTER_API_SECRET='7YKHBkcRcUDGNXqtFLI63wbYkK84BaOoHHzhnw7VLzxOa3hxhK'

CSRF_TRUSTED_ORIGINS = ['https://bypassdms.com']



LOGIN_REDIRECT_URL = '/BypassDM_V1/tweet/'

TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'advlist autolink lists link image charmap print preview anchor',
    'toolbar': 'undo redo | bold italic | alignleft aligncenter alignright | bullist numlist outdent indent | link image',
    'width': '100%',
    'height': 320,
}
