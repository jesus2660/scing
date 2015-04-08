"""
Django settings for SCIng project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v)gut^!9$#draawb+bh30y8eukiv!7(6!roqw^b2_t8t@5$)af'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'suit',
    'django.contrib.admin',
    'main',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SCIng.urls'

WSGI_APPLICATION = 'SCIng.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-VE'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

SUIT_CONFIG = {
    'ADMIN_NAME': 'SCIng',
    'HEADER_DATE_FORMAT': 'l, j F Y', # Saturday, 16 March 2013
    'HEADER_TIME_FORMAT': 'H:i',       # 18:42'
    'CONFIRM_UNSAVED_CHANGES': True,
    'MENU': (
             
        {'app': 'auth', 'label': 'Usuarios', 'icon':'icon-lock'},

        {'label': 'Universidad', 'icon':'icon-book', 'models': ('main.semestre', 'main.escuela','main.unidadacademica','main.profesor')},

        {'label': 'Estudiantes', 'icon':'icon-user', 'models': ('main.estudiante', 'main.culminacion','main.inscripcion','main.exoneracion')},

        {'label': 'Comunidades', 'icon':'icon-map-marker', 'models': ('main.comunidad', 'main.asesor')},
        
        {'label': 'Proyectos', 'icon':'icon-flag', 'models': ('main.proyecto', 'main.aprobacion','main.renovacion','main.reestructuracion','main.cierre')},
    )
    
}

MEDIA_ROOT = '/media/'

STATIC_ROOT = '/static/'