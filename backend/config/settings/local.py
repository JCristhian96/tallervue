from .base import *
from . import db


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# <---------------------------->
# Importaciones para hacer DEBUG a querys
from . import dev

dev.load_setting_devs(INSTALLED_APPS, MIDDLEWARE)
INTERNAL_IPS = dev.set_internal_ips()

# <---------------------------->

# Database
DATABASES = db.SQLITE3


# Static files (CSS, JavaScript, Images)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child("media")

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.child('dist', 'static')
]
STATIC_ROOT = BASE_DIR.child("staticfiles")

