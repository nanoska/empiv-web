
# Proyecto EMPIV - 01_03 Estructuración del Proyecto Django

## Descripción del Paso
Este paso se centra en la configuración y estructuración inicial del proyecto Django. La meta es organizar el proyecto para un desarrollo eficiente, configurando las bases que permitirán una integración sencilla con servicios externos como Amazon S3, Heroku, y GitHub Actions.

## Objetivos
1. **Inicializar el Proyecto Django:** Crear el proyecto principal en Django que contendrá las aplicaciones necesarias.
2. **Configurar la Aplicación Principal:** Añadir configuraciones iniciales en el archivo `settings.py` para soportar almacenamiento en S3, despliegue en Heroku y el uso de variables de entorno.
3. **Definir Buenas Prácticas de Configuración:** Asegurarse de que las configuraciones de seguridad y despliegue sigan las mejores prácticas, incluyendo el uso de archivos `.env` y la protección de datos sensibles.

## Pasos Detallados
### 1. Inicialización del Proyecto Django
   - En la terminal, navega al directorio deseado y ejecuta el comando para iniciar el proyecto Django:
     ```bash
     django-admin startproject empiv_project
     ```
   - Entra al directorio del proyecto y crea una aplicación inicial para manejar las funcionalidades principales:
     ```bash
     cd empiv_project
     python manage.py startapp core
     ```

### 2. Configuración de `settings.py`
   - **Variables de Entorno:** Utiliza el paquete `django-environ` para cargar las variables de entorno desde un archivo `.env`. Esto facilita la configuración segura de datos sensibles como credenciales de S3 y claves secretas.
     ```python
     import environ

     env = environ.Env()
     environ.Env.read_env()
     SECRET_KEY = env('SECRET_KEY')
     ```
   - **Configuración de Bases de Datos y Almacenamiento de Archivos:** Define los parámetros de la base de datos y añade configuraciones para almacenar archivos en S3.
   - **Configuración de Despliegue (Heroku):** Asegúrate de que `settings.py` incluye configuraciones específicas para despliegue en Heroku, como el uso de `django_heroku` y ajustes de `ALLOWED_HOSTS`.

### 3. Buenas Prácticas en Configuración
   - **Archivos Sensibles en `.env`:** Coloca todos los datos sensibles y configuraciones específicas del entorno en el archivo `.env`, evitando su inclusión en el repositorio.
   - **Configuración de Seguridad en Producción:** Define valores seguros para `DEBUG`, `ALLOWED_HOSTS`, y configura `SECURE_SSL_REDIRECT` y `CSRF_COOKIE_SECURE` para producción.

## Consideraciones Finales
Al finalizar este paso, el proyecto tendrá una estructura sólida para el desarrollo, con configuraciones flexibles que permiten adaptar el entorno entre desarrollo y producción. Se recomienda verificar que las configuraciones de `settings.py` funcionan tanto en entornos locales como en el despliegue inicial en Heroku.

