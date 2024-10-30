# Proyecto EMPIV - 02_07 Configuración de Vistas y Rutas para Eventos y Talleres

## Descripción del Paso
Este paso documenta las vistas y rutas configuradas para la gestión de eventos y talleres en la aplicación. Las vistas permiten listar, crear, actualizar, y eliminar tanto eventos como talleres, además de ofrecer detalles específicos para cada uno. Las rutas asociadas facilitan el acceso a estas funcionalidades desde URLs intuitivas.

## Rutas Configuradas

### Rutas para Talleres (`academy/urls.py`)
- **`talleres/list/`**: Muestra la lista de todos los talleres disponibles.
- **`taller/create/`**: Permite crear un nuevo taller.
- **`taller/<int:pk>/`**: Muestra el detalle de un taller específico.
- **`taller/update/<int:pk>/`**: Permite actualizar la información de un taller existente.
- **`taller/delete/<int:pk>/`**: Elimina un taller específico.

### Rutas para Eventos y Locaciones (`events/urls.py`)
- **`list/`**: Lista todos los eventos en orden cronológico.
- **`evento/<int:pk>/`**: Muestra el detalle de un evento específico.
- **`evento/create/`**: Permite la creación de un nuevo evento.
- **`evento/update/<int:pk>/`**: Actualiza la información de un evento existente.
- **`evento/delete/<int:pk>/`**: Elimina un evento específico.
- **`locaciones/`**: Lista todas las locaciones.
- **`locacion/<int:pk>/`**: Muestra los detalles de una locación específica.
- **`locacion/create/`**: Permite la creación de una nueva locación.

## Vistas Definidas

### Vistas para Talleres (`academy/views.py`)

- **WorkshopListView**: Lista todos los talleres, ordenados por fecha de creación.
- **WorkshopDetailView**: Muestra el detalle de un taller específico.
- **WorkshopCreateView**: Permite a usuarios con permisos crear un nuevo taller.
- **WorkshopUpdateView**: Permite a usuarios con permisos actualizar un taller existente.
- **WorkshopDeleteView**: Permite a usuarios con permisos eliminar un taller específico.

### Vistas para Eventos (`events/views.py`)

- **EventListView**: Lista todos los eventos en orden cronológico.
- **EventDetailView**: Muestra el detalle de un evento específico, incluyendo un formulario de reserva.
- **EventCreateView**: Permite la creación de un evento, disponible solo para usuarios con permisos.
- **EventUpdateView**: Permite actualizar un evento existente.
- **EventDeleteView**: Permite eliminar un evento específico.

### Vistas para Locaciones (`events/views.py`)
- **LocationListView**: Lista todas las locaciones.
- **LocationDetailView**: Muestra detalles de una locación.
- **LocationCreateView** y **LocationUpdateView**: Permiten crear y actualizar locaciones, disponibles solo para usuarios con permisos.

## Consideraciones Finales
Las rutas y vistas configuradas en este paso proporcionan una interfaz completa para la gestión de eventos, talleres y locaciones. La estructura de permisos asegura que solo los usuarios autorizados puedan realizar acciones de creación, actualización o eliminación. Estas vistas están configuradas para facilitar la interacción de los usuarios con el contenido de manera organizada y eficiente.

