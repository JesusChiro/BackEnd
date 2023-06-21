# Django

## Creamos el entorno virtual

'''
python -venv venv
'''

## Activamos  el entorno virtual
'''
# Windows
venv/Script/activate

# Linux
source venv/bin/activate
'''

## Instalamos Django
'''
pip install django
'''

## Creamos el proyecto
'''
django-admin startproject mysite
'''

## Ingresa al proyecto
'''
cd mysite
'''

## Ejecutamos las migraciones
'''
python manage.py runserver
'''

## Creamos un super usuario
'''
python manage.py createsuperuser
'''

