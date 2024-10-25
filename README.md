Aplicación web para escuela de música
Este proyecto es una aplicación web diseñada para una escuela de música, con un backend desarrollado en Python y un frontend en Javascript.

Requisitos previos
Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde python.org.

Instalación
Clona este repositorio en tu máquina local:
git clone https://github.com/nanoska/web_empiv

Accede al directorio del proyecto:
cd web_empiv

Instala las dependencias del backend:
pip install -r requirements.txt

Instala las dependencias del frontend:
cd frontend npm install

Configuración
Antes de ejecutar la aplicación, asegúrate de configurar correctamente el archivo de configuración config.py en la carpeta backend. Aquí puedes establecer la configuración de la base de datos u otros parámetros según sea necesario.

Ejecución
Para ejecutar el backend, desde el directorio raíz del proyecto, utiliza el siguiente comando:
python3 manage.py runserver

Esto iniciará el servidor backend en http://localhost:5000.

Para ejecutar el frontend, desde el directorio frontend, utiliza el siguiente comando:
npm start

Esto iniciará el servidor de desarrollo del frontend en http://localhost:3000.

Uso
Una vez que ambos servidores estén en funcionamiento, puedes acceder a la aplicación abriendo tu navegador y navegando a http://localhost:3000. Aquí podrás interactuar con la aplicación web de la escuela de música.

Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, asegúrate de abrir un problema primero para discutir los cambios propuestos.

Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.

