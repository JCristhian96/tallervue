from .base import os, BASE_DIR


SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child(os.getenv("DB_LOCAL")),
    }
}
