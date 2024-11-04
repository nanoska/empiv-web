# Proyecto EMPIV - Fase 3: Desarrollo de la Interfaz (Frontend)

## Descripción General

La fase 3 se enfoca en el desarrollo de la interfaz de usuario del proyecto EMPIV. Esta etapa incluye la construcción de templates, la integración con los datos dinámicos desde el backend, y la implementación de funcionalidades adicionales para mejorar la experiencia del usuario.

## 3.1 Diseño y Maquetación de Templates Django

### Objetivo

Construir la estructura HTML de cada página principal del sitio, aplicando un diseño CSS básico y asegurando que las secciones sean fáciles de navegar.

### Paso a Paso

1. **Landing Page**: Crear un template básico que muestre una vista general del sitio, destacando cada sección (Sobre Nosotros, Eventos, Talleres, Contacto).
2. **Sección Sobre Nosotros**: Estructurar esta sección para mostrar texto e imágenes descriptivas del proyecto. Asegurarse de que el formato sea adecuado para posibles exportaciones en PDF.
3. **Eventos y Talleres**: Crear templates en formato de tarjetas, utilizando estilos CSS para diferenciar el estado de los eventos (verde para actuales, rojo para pasados, "próximo" con un badge). Esta sección incluirá una sección para staff users, donde se pueda desarrollar el CRUD de los modelos.
4. **Formulario de Contacto**: Diseñar un formulario de contacto que incluya campos básicos como nombre, correo electrónico y mensaje.

### Consideraciones

- Asegurar consistencia en el diseño visual entre las páginas.
- Implementar CSS para hacer los elementos responsivos y asegurar una buena experiencia en dispositivos móviles.

## 3.2 Integrar las Plantillas con el Backend

### Objetivo

Conectar cada template con las vistas y modelos de Django para cargar y mostrar datos dinámicos, como listas de eventos y talleres.

### Paso a Paso

1. **Vistas de Listado y Detalle**: Conectar los templates de listado (`event_list.html`, `workshop_list.html`) con las vistas correspondientes (`EventListView`, `WorkshopListView`). Asegurarse de que los datos se carguen dinámicamente desde la base de datos.
2. **Integración de Datos Dinámicos**: Utilizar el contexto de las vistas para mostrar datos específicos en los templates, como la lista de talleres disponibles o la ubicación de eventos.
3. **Navegación y Enlaces**: Asegurarse de que los enlaces y botones en cada página redirijan correctamente a las vistas de detalle de eventos y talleres.

### Consideraciones

- Verificar que los datos dinámicos se muestran correctamente en cada sección.
- Asegurar que los enlaces internos entre páginas funcionan adecuadamente.

## 3.3 Implementación de Funcionalidades Adicionales

### Objetivo

Añadir funcionalidades extra que mejoren la usabilidad y estética del sitio.

### Paso a Paso

1. **Exportación a PDF en "Sobre Nosotros"**: Implementar una opción para exportar el contenido de la sección "Sobre Nosotros" en formato PDF, utilizando una librería como `xhtml2pdf` o `WeasyPrint`.
2. **Estado de los Eventos con Colores**: Aplicar estilos CSS condicionales en las tarjetas de eventos para que muestren bordes de color según el estado del evento (verde, rojo, o badge de "próximo").
3. **Formulario de Contacto con WhatsApp**: Configurar el formulario de contacto para que redirija al usuario a WhatsApp con un mensaje predefinido.

### Consideraciones

- Asegurarse de que la exportación a PDF incluya todos los elementos necesarios y que el formato sea correcto.
- Verificar que la funcionalidad de contacto a través de WhatsApp funcione en dispositivos móviles y de escritorio.

## 3.4 Implementar Funcionalidades de Contacto

### Objetivo

Agregar un formulario de contacto funcional en la sección "Contacto" que permita a los usuarios enviar mensajes directamente.

### Paso a Paso

1. **Formulario HTML**: Crear un formulario en el template `contact.html` con los campos necesarios (nombre, email, mensaje).
2. **Enlace a WhatsApp**: Configurar el botón de envío para que redirija a un enlace de WhatsApp, pasando el contenido del formulario en el mensaje.

### Consideraciones

- Asegurarse de que el mensaje se construye correctamente en el enlace de WhatsApp.
- Verificar que el formulario funciona en dispositivos móviles, donde WhatsApp está configurado.

## Conclusiones

La Fase 3 establece una interfaz visual y funcional para los usuarios, conectando los templates con el backend y añadiendo funcionalidades adicionales. Estos elementos son clave para una experiencia de usuario intuitiva y accesible.
