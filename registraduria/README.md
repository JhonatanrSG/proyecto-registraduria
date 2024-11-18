# Proyecto Registraduria

Este proyecto es una aplicación web desarrollada con Django para gestionar ciudadanos, sus datos personales y realizar las operaciones básicas de CRUD (Crear, Leer, Actualizar, Eliminar). Permite a los usuarios crear, editar y consultar información de ciudadanos.

## Requisitos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.x**
- **Pip** (el gestor de paquetes de Python)
- **Django 3.x**
- **Base de datos configurada** (por defecto, usa SQLite)

## Instalación

Sigue estos pasos para instalar y configurar el proyecto en tu máquina local.

1. **Clona este repositorio**

    Abre una terminal y ejecuta el siguiente comando para clonar el proyecto desde GitHub:

    ```bash
    git clone https://github.com/tu-usuario/proyecto-registraduria.git
    ```

2. **Crea un entorno virtual**

    Es recomendable crear un entorno virtual para instalar las dependencias del proyecto:

    ```bash
    python -m venv venv
    ```

3. **Activa el entorno virtual**

    - En **Windows**:

      ```bash
      venv\Scripts\activate
      ```

    - En **Linux/Mac**:

      ```bash
      source venv/bin/activate
      ```

4. **Instala las dependencias**

    En la terminal, dentro del directorio del proyecto, ejecuta:

    ```bash
    pip install -r requirements.txt
    ```

    Si aún no tienes un archivo `requirements.txt`, puedes generarlo con el siguiente comando (suponiendo que ya hayas instalado las dependencias previamente):

    ```bash
    pip freeze > requirements.txt
    ```

5. **Configura la base de datos**

    Ejecuta las migraciones para crear las tablas necesarias en la base de datos:

    ```bash
    python manage.py migrate
    ```

6. **Crea un superusuario (opcional)**

    Si quieres acceder al panel de administración de Django, crea un superusuario ejecutando el siguiente comando:

    ```bash
    python manage.py createsuperuser
    ```

    Luego sigue las instrucciones para configurar el nombre de usuario, correo electrónico y contraseña.

7. **Ejecuta el servidor de desarrollo**

    Finalmente, ejecuta el servidor de desarrollo de Django:

    ```bash
    python manage.py runserver
    ```

    Accede a la aplicación en tu navegador mediante la URL `http://127.0.0.1:8000`.

## Estructura del Proyecto

La estructura de carpetas y archivos del proyecto es la siguiente:
./
    directory_structure.txt
    manage.py
    print_structure.py
    README.md
    ciudadanos/
        admin.py
        apps.py
        forms.py
        models.py
        tests.py
        urls.py
        views.py
        __init__.py
        migrations/
            0001_initial.py
            0002_auto_20241117_1621.py
            0003_auto_20241117_2018.py
            __init__.py
            __pycache__/
                0001_initial.cpython-39.pyc
                0002_auto_20241117_1621.cpython-39.pyc
                0003_auto_20241117_2018.cpython-39.pyc
                __init__.cpython-39.pyc
        templates/
            ciudadanos/
                consulta_antecedentes_ciudadano.html
                consulta_mis_antecedentes.html
                edit_user.html
                login.html
                register.html
                summary.html
        __pycache__/
            admin.cpython-39.pyc
            forms.cpython-39.pyc
            models.cpython-39.pyc
            urls.cpython-39.pyc
            views.cpython-39.pyc
            __init__.cpython-39.pyc
    media/
        photos/
            bolteo_avion_t.jpg
            Identificacion_.png
            Logo.png
            Logo_iaKc0HC.png
            Logo_P4YVn0b.png
            QR-HL3-Pista1.png
    photos/
        Logo.png
    registraduria/
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
        __pycache__/
            settings.cpython-39.pyc
            urls.cpython-39.pyc
            wsgi.cpython-39.pyc
            __init__.cpython-39.pyc
    static/
        css/
            style.css
        js/
            script.js


## Dependencias

Las principales dependencias del proyecto están en el archivo `requirements.txt`:

- `Django==3.1.12` - Framework web de Python.
- `gunicorn==20.1.0` - Servidor WSGI para producción.
- `django-crispy-forms==1.10.0` - Para mejorar los formularios en Django.

## Desplegar en Heroku

Si deseas desplegar este proyecto en Heroku, sigue estos pasos:

1. **Instala la CLI de Heroku**:
   
   Descarga e instala la [CLI de Heroku](https://devcenter.heroku.com/articles/heroku-cli).

2. **Crea un archivo `Procfile`**:

   En la raíz de tu proyecto, crea un archivo llamado `Procfile` con el siguiente contenido:


