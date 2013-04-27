from tmster.settings import *
import dj_database_url
DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASES = {'default':
                   dj_database_url.config(
                  default='postgres://kayethano:90ldenb0y@localhost:5432/tmster')
        }

#CuantoDev Facebook Settings
FACEBOOK_APP_ID = ''
FACEBOOK_APP_SECRET = '' 




