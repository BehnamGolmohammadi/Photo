from photo.settings import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^)a71zql%u)kg)-_wm8b_8x+dkhltuk8i8+tjm#is87!sh@uys'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SECURE_SSL_REDIRECT = 0
CSRF_COOKIE_SECURE = 0

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'statics'
]