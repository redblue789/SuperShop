
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-demo'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = ['django.contrib.staticfiles','shop']

MIDDLEWARE = []

ROOT_URLCONF = 'pearl_site.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
}]

STATIC_URL = 'static/'
