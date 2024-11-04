# Proyecto EMPIV - 01_02 Diseño de Base de Datos y Modelado

## Descripción del Paso

Este paso se enfoca en el diseño y modelado de la base de datos para la aplicación web del Proyecto EMPIV, estableciendo la estructura de datos necesaria para las funcionalidades clave: gestión de eventos, talleres y locaciones. Este diseño será implementado utilizando Django ORM, permitiendo la creación de modelos y relaciones necesarios de manera eficiente y escalable.

## Objetivos

1. **Definir Modelos Principales:** Crear modelos Django para cada una de las entidades principales: `Eventos`, `Talleres`, y `Locaciones`.
2. **Establecer Relaciones entre Modelos:** Configurar relaciones entre los modelos, permitiendo la asociación entre eventos, talleres y locaciones.
3. **Definir Atributos Clave:** Para cada modelo, se especificarán atributos específicos que serán requeridos por las funcionalidades del sistema.

## Especificaciones de los Modelos

### 1. Modelo `Eventos`

- **Descripción:** Representa cada evento que será gestionado dentro de la aplicación.
- **Atributos Clave:**
  - `titulo`: Título del evento (cadena de texto).
  - `descripcion`: Descripción detallada (texto largo).
  - `fecha`: Fecha y hora del evento.
  - `estado`: Estado del evento (opciones: "vigente", "pasado", "proximo").
  - `ubicacion`: Relación hacia el modelo `Locaciones` para la ubicación.

### 2. Modelo `Talleres`

- **Descripción:** Representa los talleres disponibles y sus datos de contacto.
- **Atributos Clave:**
  - `titulo`: Título del taller.
  - `descripcion`: Descripción y objetivos del taller.
  - `fecha_inicio` y `fecha_fin`: Periodo de duración del taller.
  - `ubicacion`: Relación hacia el modelo `Locaciones`.

### 3. Modelo `Locaciones`

- **Descripción:** Almacena la información de las ubicaciones donde se llevan a cabo eventos y talleres.
- **Atributos Clave:**
  - `nombre`: Nombre de la locación.
  - `direccion`: Dirección completa.
  - `capacidad`: Capacidad máxima de personas.

## Implementación en Django ORM

Los modelos se implementarán en el archivo `models.py` de Django, definiendo cada clase como un modelo de Django y especificando relaciones y atributos. Se utilizarán migraciones para crear la base de datos.

### Ejemplo de Código para `models.py`

```python
from django.db import models

class Locacion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    capacidad = models.IntegerField()

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=50, choices=[('vigente', 'Vigente'), ('pasado', 'Pasado'), ('proximo', 'Próximo')])
    ubicacion = models.ForeignKey(Locacion, on_delete=models.CASCADE)

class Taller(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ubicacion = models.ForeignKey(Locacion, on_delete=models.CASCADE)
```

## Consideraciones Finales

Una vez definidos los modelos, se recomienda realizar pruebas iniciales en Django Shell para validar la integridad de las relaciones y atributos. La creación de migraciones y su ejecución inicial permitirá comprobar la estructura de la base de datos.
