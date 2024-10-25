# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Establece las variables de entorno necesarias
ENV PYTHONUNBUFFERED=1

# Corre las migraciones y colecta los archivos estáticos
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# Expone el puerto en el que la app correrá
EXPOSE 8000

# Define el comando para correr la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
