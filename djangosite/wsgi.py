import os
import sys

path = '/home/Xabcent/my-first-blog'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangosite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()