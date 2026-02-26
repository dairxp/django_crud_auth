# Django CRUD Auth

Aplicación web de gestión de tareas con autenticación de usuarios, desarrollada con Django 6.0.

## Características

- Registro e inicio de sesión de usuarios
- Crear, leer, actualizar y eliminar tareas (CRUD)
- Marcar tareas como completadas
- Interface responsive con Bootstrap

## Requisitos

- Python 3.12+
- Django 6.0.2
- PostgreSQL (producción)

## Instalación

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Estructura

- `djangocrud/` - Configuración principal del proyecto
- `tasks/` - Aplicación de gestión de tareas
- `templates/` - Plantillas HTML

## Modelos

- User - Usuario (Django Auth)
- Task - Tarea con título, descripción e importancia

## Despliegue Render
 
Configurado para Render con WhiteNoise, PostgreSQL y variables de entorno.
=> https://django-crud-auth-ibxf.onrender.com/
