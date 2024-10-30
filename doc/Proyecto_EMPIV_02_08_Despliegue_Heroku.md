# Proyecto EMPIV - 02_08 Configuración de Despliegue en Heroku

## Descripción del Paso
Este paso documenta el proceso de configuración y despliegue de la aplicación Django en Heroku. Heroku proporciona un entorno de despliegue en la nube fácil de gestionar, ideal para hospedar aplicaciones Django con integración de variables de entorno y configuración automática de dependencias.

## Paso a Paso

### 1. Crear la Aplicación en Heroku
   - Accede a la consola de Heroku y selecciona la opción "Crear nueva aplicación".
   - Asigna un nombre único a la aplicación y elige la región más cercana para optimizar el rendimiento.
   - Una vez creada, toma nota del nombre de la aplicación, ya que se usará para realizar el despliegue.

### 2. Configurar Variables de Entorno
   - En la sección "Settings" de la aplicación en Heroku, selecciona "Reveal Config Vars".
   - Añade las variables de entorno necesarias para que la aplicación Django funcione correctamente, incluyendo las credenciales para S3 y otras configuraciones sensibles.

     | Variable                   | Valor                        |
     |----------------------------|------------------------------|
     | `AWS_ACCESS_KEY_ID`        | Tu clave de acceso AWS       |
     | `AWS_SECRET_ACCESS_KEY`    | Tu secreto de AWS            |
     | `AWS_STORAGE_BUCKET_NAME`  | Nombre del bucket S3         |
     | `SECRET_KEY`               | Clave secreta de Django      |
     | `DEBUG`                    | `False`                      |

### 3. Configurar Archivos para Heroku

#### `Procfile`
   - Crea un archivo llamado `Procfile` en el directorio raíz de tu proyecto. Este archivo indica a Heroku cómo ejecutar tu aplicación.
     ```
     web: gunicorn empiv_project.wsgi --log-file -
     ```

#### `requirements.txt` y `runtime.txt`
   - Asegúrate de que el archivo `requirements.txt` esté actualizado con todas las dependencias necesarias:
     ```bash
     pip freeze > requirements.txt
     ```
   - Si deseas especificar la versión de Python, crea un archivo `runtime.txt` en el que indiques la versión de Python:
     ```
     python-3.9.12
     ```

### 4. Conectar el Repositorio de GitHub con Heroku
   - En la sección "Deploy" de la consola de Heroku, conecta la aplicación con el repositorio de GitHub donde está alojado tu proyecto.
   - Habilita la opción de "Automatic Deploys" para que Heroku despliegue la aplicación cada vez que haya un cambio en la rama `main` o `dev` (según tu configuración).

### 5. Realizar el Primer Despliegue
   - En la consola de Heroku, selecciona "Deploy Branch" para iniciar el primer despliegue manualmente.
   - Verifica en los registros de Heroku que el despliegue se haya completado sin errores.
   - Accede a la URL generada por Heroku para tu aplicación y confirma que la página de inicio se carga correctamente.

## Consideraciones Finales
La configuración de despliegue en Heroku permite una integración sencilla y rápida para hospedar la aplicación en la nube. La conexión con GitHub asegura que los cambios realizados en el código se reflejen automáticamente en el servidor, manteniendo la aplicación actualizada sin necesidad de realizar despliegues manuales.

