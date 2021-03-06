# -*- coding: utf-8 -*-
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'TEST':  # This will force django to create a real sqlite database on
                 # the disk, instead of creating it in memory.
                 # We need this to test the async behavior.
            {
                'NAME': 'test_db',
            },
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = [
    'background_task',
]

SECRET_KEY = 'foo'

USE_TZ = True
BACKGROUND_TASK_RUN_ASYNC = False
