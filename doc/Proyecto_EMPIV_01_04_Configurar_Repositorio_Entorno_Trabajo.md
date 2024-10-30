
# Proyecto EMPIV - 01_04 Configurar Repositorio y Entorno de Trabajo

## Descripción del Paso
Este paso se enfoca en configurar el entorno de trabajo para el desarrollo del proyecto y establecer el repositorio en GitHub. La configuración adecuada del entorno local y del repositorio garantiza un flujo de trabajo ordenado y facilita la colaboración, el control de versiones, y el despliegue automatizado mediante GitHub Actions.

## Objetivos
1. **Crear y Configurar el Repositorio en GitHub:** Crear un repositorio para el proyecto y proteger las ramas principales (`dev` y `main`).
2. **Configurar GitHub Actions para Despliegue Automatizado:** Definir un flujo de trabajo que permita realizar despliegues automáticos en Heroku cada vez que se haga un push a `dev` o `main`.
3. **Preparar el Entorno Local:** Configurar el entorno de desarrollo local con los archivos necesarios (`requirements.txt`, `.env`), para asegurar consistencia entre los entornos de desarrollo y producción.

## Pasos Detallados
### 1. Creación y Configuración del Repositorio en GitHub
   - Inicia un repositorio en GitHub para el proyecto `EMPIV`. Configura el repositorio como privado o público según las necesidades del proyecto.
   - Configura protecciones de rama en `dev` y `main` para prevenir cambios directos, forzando la creación de pull requests para revisiones de código.
   - Clona el repositorio en tu máquina local:
     ```bash
     git clone https://github.com/tu_usuario/empiv.git
     ```

### 2. Configuración de GitHub Actions para Despliegue Automatizado
   - Dentro del repositorio, crea un directorio `.github/workflows/` y añade un archivo `deploy.yml` para definir el flujo de trabajo automatizado.
   - Configura el archivo YAML para ejecutar pruebas y desplegar en Heroku cuando se haga push a `dev` o `main`.
   - Ejemplo básico de configuración para Heroku:
     ```yaml
     name: Deploy to Heroku

     on:
       push:
         branches:
           - main
           - dev

     jobs:
       deploy:
         runs-on: ubuntu-latest
         steps:
           - uses: actions/checkout@v2
           - name: Log in to Heroku
             run: |
               echo "$HEROKU_API_KEY" | docker login --username="$HEROKU_USERNAME" --password-stdin registry.heroku.com
           - name: Deploy to Heroku
             run: |
               git push heroku main
         env:
           HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
           HEROKU_USERNAME: ${{ secrets.HEROKU_USERNAME }}
     ```
   - Asegúrate de configurar los secretos (`HEROKU_API_KEY`, `HEROKU_USERNAME`) en GitHub.

### 3. Preparación del Entorno Local
   - **Archivo `requirements.txt`:** Genera un archivo `requirements.txt` para especificar las dependencias del proyecto.
     ```bash
     pip freeze > requirements.txt
     ```
   - **Archivo `.env`:** Crea un archivo `.env` para almacenar variables de entorno sensibles. Este archivo debe incluir configuraciones como `SECRET_KEY`, credenciales de S3, y configuraciones de base de datos.
   - **Configuración de `.gitignore`:** Asegúrate de agregar archivos como `.env`, `__pycache__`, y otros archivos temporales a `.gitignore` para evitar que se suban al repositorio.

## Consideraciones Finales
Al completar este paso, el repositorio estará preparado para control de versiones, y el entorno local contará con configuraciones y dependencias organizadas. El despliegue automático mediante GitHub Actions facilitará la implementación de cambios en Heroku cada vez que se aprueben cambios en `dev` o `main`.
