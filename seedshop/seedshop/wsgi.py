"""
WSGI config for seedshop project.
"""
import os
import sys

# Render deployment के लिए path fix
sys.path.append('/opt/render/project/src')

# Settings module set करो
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seedshop.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

