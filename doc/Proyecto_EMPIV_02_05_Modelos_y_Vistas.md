
# Proyecto EMPIV - 02_05 Modelos y Vistas de la Aplicación

## Descripción del Paso
Este documento describe la implementación de los modelos y vistas esenciales de la aplicación EMPIV, los cuales gestionan la información de eventos, locaciones y talleres, así como las vistas asociadas que permiten la interacción con estos modelos en la interfaz.

## Modelos Definidos

### 1. Modelo `Location`
   - **Descripción:** Representa las ubicaciones donde se realizan eventos y talleres.
   - **Atributos Principales:**
      - `name`: Nombre de la locación.
      - `address`, `city`, `state`: Información de dirección.
      - `phone`, `email`, `website`: Datos de contacto.
      - `image`: Imagen representativa de la locación.
      - `capacity`: Capacidad de personas de la locación.
      - `iframe`: Código para incrustar un mapa o referencia de ubicación.

### 2. Modelo `Event`
   - **Descripción:** Representa los eventos que se gestionan en la plataforma.
   - **Atributos Principales:**
      - `name`: Nombre del evento.
      - `short_description`, `description`: Descripciones corta y detallada del evento.
      - `date`, `time`: Fecha y hora del evento.
      - `location`: Relación con el modelo `Location`.
      - `image`: Imagen asociada al evento.
      - `state`: Estado del evento (vigente, pasado o próximo).

### 3. Modelo `EventReservation`
   - **Descripción:** Gestiona las reservaciones para los eventos.
   - **Atributos Principales:**
      - `event`: Relación con el modelo `Event`.
      - `name`, `email`, `phone`: Datos de contacto de quien realiza la reserva.

### 4. Modelo `Workshop`
   - **Descripción:** Representa los talleres disponibles.
   - **Atributos Principales:**
      - `name`: Nombre del taller.
      - `description`: Descripción detallada del taller.
      - `day`, `init_time`, `end_time`: Día y horario de inicio y fin.
      - `price`: Precio del taller.
      - `location`: Relación con `Location`.
      - `max_participants`: Número máximo de participantes permitidos.

## Vistas Definidas

### Vistas para Eventos

- **EventListView**: Muestra una lista de todos los eventos ordenados por fecha.
- **EventDetailView**: Muestra el detalle de un evento específico, incluyendo un formulario de reserva.
- **EventCreateView** y **EventUpdateView**: Permiten la creación y actualización de eventos, accesibles solo para usuarios con permisos.
- **EventDeleteView**: Permite eliminar un evento.

### Vistas para Locaciones

- **LocationListView**: Muestra una lista de todas las locaciones disponibles.
- **LocationDetailView**: Muestra los detalles de una locación específica.
- **LocationCreateView** y **LocationUpdateView**: Permiten la creación y actualización de locaciones.

### Vistas para Talleres

- **WorkshopListView**: Muestra una lista de todos los talleres.
- **WorkshopDetailView**: Muestra el detalle de un taller.
- **WorkshopCreateView** y **WorkshopUpdateView**: Permiten la creación y actualización de talleres.
- **WorkshopDeleteView**: Permite eliminar un taller.

## Consideraciones Finales
Esta configuración de modelos y vistas permite una gestión completa de eventos, locaciones y talleres en la aplicación. Las relaciones entre los modelos están diseñadas para facilitar la recuperación de datos y el manejo de dependencias entre eventos y sus locaciones. Las vistas implementadas siguen buenas prácticas de seguridad y permisos, asegurando que solo usuarios con permisos específicos puedan crear, actualizar o eliminar entradas.

