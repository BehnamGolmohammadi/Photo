from photo.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^)a71zql%u)kg)-_wm8b_8x+dkhltuk8i8+tjm#is87!sh@uys'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = []

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'statics'
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Site framwork settings
SITE_ID = 2

# robots mudole
ROBOTS_USE_HOST = False
ROBOTS_USE_SITEMAP = False

# email setting
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'linuxbehnam@gmail.com'
EMAIL_HOST_PASSWORD = 'zfjvrjnjbvwpivjs'