# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1730728/data/www/vorotaguru.ru/vorotaguru')
sys.path.insert(1, '/var/www/u1730728/data/vorotaguru_env/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'vorotaguru.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()