import os

settings = {
    'DEBUG': True,
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    'STATICFILES_DIRS': (
        os.path.abspath(os.path.dirname(__file__)),
    ),
    'STATIC_ROOT': os.path.abspath(os.path.join(os.path.dirname(__file__), 'static')),
    'STATIC_URL': '/static/',
}