"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
 
import os

pids=[19168,
18180,
29784,
12688,
23572,
26848,
16916,
25756]
for i in pids:
	os.system(f'taskkill /pid {i} /f')
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_asgi_application()
