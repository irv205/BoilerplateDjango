Boilerplate (Django, Django REST Framework)

> Framework [Django 3.1.6](https://docs.djangoproject.com/en/3.1/releases/3.1/)

## Indice

* [Acerca](#Acerca)
* [Requisitos](#Requisitos)
* [Estructura Boilerplate](#Estructura)
* [Instalacion](#Instalacion)
* [Postman](#Postman)
* [Documentacion](#Documentacion)

## Acerca

Framework construido para facilitar el desarrollo de proyectos, creando la estructura base
de un proyecto.

## Requisitos

- VirtualEnv
- Python 3
- Pip
- PosgreSQL

## Paquetes extras
```
- Setuptools en caso de tener algun problema al estar instalando los requerimientos, 
tome en cuenta instalar estos paquetes de pip.
pip install setuptools
```

## Estructura del proyecto

```
boilerplate/
    venv/
        ...
    apps/
        user/
        ... more apps here

    common/
        baseModel.py
        pagination.py

    project/
        __init__.py
        urls.py
        wsgi.py
        settings.py

     templates/

    .env.example
    Django-boilerplate-v1.postman_collection.json
    Django-boilerplate-v1.postman_environment.json
    manage.py
    requirements.txt
```

## Instalacion
> Instalar requisitos anteriores,
> Descargar o clonar el proyecto.

#### Con Bash
```
# Dar permisos a installation.sh
$ chmod +x installation.sh

# Iniciar Instalacion
$ bash installation.sh
```

#### Sin Bash
```
# Crear entorno virtual (dentro del proyecto)
$ python3 -m venv venv

# Activar entorno virtual
$ source venv/bin/activate

# Desactivar
$ deactivate

# Copiar env de ejemplo y agregar datos
cp .env.example .env
$ nano .env

# Instalar requerimientos (Con el entorno virtual activado)
$ pip install -r requirements.txt

# En caso de algun problema al instalar requerimientos tome en cuenta el siguiente comando
$ pip install setuptools
```

#### Comando 
```
# Migraciones
$ python manage.py migrate

# Ejecutar proyecto
$ python manage.py runserver

# Ejecutar archivos estaticos
$ python manage.py collectstatic

# Crear un super usuario para accesar al panel de Django
$ python manage.py createsuperuser
```

## Crear app (Modulo)
```
# En...
$ cd apps/
$ django-admin startapp myapp
```

## Estructura .ENV
```
DEBUG=
SECRET_KEY=
APP_NAME=
WEBSITE_URL=
SERVER_URL=
TIME_ZONE=
PAGINATION=

DB_ENGINE='django.db.backends.postgresql'
DB_HOST=
DB_NAME=
DB_OWNER=
DB_PASSWORD=
DB_PORT=

EMAIL_USE_TLS=
EMAIL=
EMAIL_BACKEND=
EMAIL_HOST=
EMAIL_USER=
EMAIL_PASSWORD=
EMAIL_PORT=
```

## Doc Endpoint 
> Collection para importar a Postman para virualizar la carpeta de los endpoint.
```
Django-boilerplate-v1.postman_collection.json
```
> Environment para tener acceso al host (http://127.0.0.1:8000/) y tambien obtener el access y refresh token para los endpoint que requiere autentificacion.
```
Django-boilerplate-v1.postman_environment.json
```

# Documentacion

* [Python 3](https://www.python.org/doc/)
* [Django 3](https://docs.djangoproject.com/es/3.1/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [PIP](https://pip.pypa.io/en/stable/)
* [Virtualenv](https://pypi.org/project/virtualenv/)
* [PostgreSQL](https://www.postgresql.org/)
* [JWT](https://medium.com/django-rest/django-rest-framework-jwt-authentication-94bee36f2af8)
* [Environ](https://django-environ.readthedocs.io/en/latest/)