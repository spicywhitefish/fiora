from settings import *

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'fiora_db',
    }
}
SECRET_KEY='_s9uqd^tka_6v9g3%+rc!f^=9pja!rqnw2j81p)f=4=$1f$j0s'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}