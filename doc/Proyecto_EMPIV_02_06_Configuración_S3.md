
# Proyecto EMPIV - 02_06 Configuración de Amazon S3 para Almacenamiento de Imágenes

## Descripción del Paso
Este paso explica la configuración de Amazon S3 para almacenar imágenes en el proyecto Django. Esta integración permite que los archivos multimedia, como imágenes, se almacenen de manera eficiente en la nube, manteniendo el servidor web ligero y mejorando el rendimiento.

## Paso a Paso

### 1. Crear un Bucket en Amazon S3
   - Accede a la consola de Amazon S3 y crea un nuevo bucket con un nombre único.
   - Asegúrate de que el bucket sea privado para mantener el control de acceso.
   - Configura las políticas de permisos de tal manera que solo la aplicación tenga acceso.

### 2. Obtener Credenciales de Acceso de AWS
   - Crea un nuevo usuario en la consola de AWS IAM con permisos programáticos.
   - Asigna los permisos necesarios, como `AmazonS3FullAccess` o una política específica para el bucket.
   - Guarda las credenciales de `AWS_ACCESS_KEY_ID` y `AWS_SECRET_ACCESS_KEY`.

### 3. Instalar Dependencias
   - Instala `boto3` y `django-storages`, que permiten a Django comunicarse con S3:
     ```bash
     pip install boto3 django-storages
     ```

### 4. Configurar `settings.py` en Django
   - Añade las configuraciones para que Django use S3 como almacenamiento de archivos estáticos y de medios.
   - Ejemplo de configuración:

     ```python
     # settings.py
     import os
     
     INSTALLED_APPS += ['storages']

     AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
     AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
     AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')

     AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
     AWS_DEFAULT_ACL = None
     AWS_S3_OBJECT_PARAMETERS = {
         'CacheControl': 'max-age=86400',
     }

     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
     MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

     STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
     STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
     ```

### 5. Configuración de Variables de Entorno en `.env`
   - Define en tu archivo `.env` las variables necesarias para conectar con S3:
     ```
     AWS_ACCESS_KEY_ID=tu_acceso
     AWS_SECRET_ACCESS_KEY=tu_secreto
     AWS_STORAGE_BUCKET_NAME=nombre_del_bucket
     ```

### 6. Pruebas
   - Realiza pruebas subiendo una imagen desde el panel de administración de Django o a través de un formulario para verificar que la integración funciona correctamente.

## Consideraciones Finales
Esta configuración de S3 permite que el proyecto almacene archivos multimedia de forma segura y escalable, liberando carga en el servidor y optimizando el almacenamiento. Además, la configuración de almacenamiento en la nube facilita la administración de archivos y permite un acceso controlado.

