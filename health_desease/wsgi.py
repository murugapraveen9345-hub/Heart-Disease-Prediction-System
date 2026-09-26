"""
WSGI config for health_desease project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
orig_db = os.path.join(BASE_DIR, 'db.sqlite3')
tmp_db = os.path.join('/tmp', 'db.sqlite3')

if os.name != 'nt' or os.environ.get('VERCEL'):
    try:
        if os.path.exists(orig_db) and (not os.path.exists(tmp_db) or os.path.getsize(tmp_db) == 0):
            shutil.copy2(orig_db, tmp_db)
            os.chmod(tmp_db, 0o666)
    except Exception as e:
        print(f"Error copying db to /tmp: {e}")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_desease.settings')

application = get_wsgi_application()
app = application

