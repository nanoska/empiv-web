# Proyecto EMPIV - Alcance y Objetivos

## Descripción General

El Proyecto EMPIV tiene como objetivo desarrollar una aplicación web para una escuela de música especializada en instrumentos de viento. Este proyecto está encargado al estudio de desarrollo Satori y será implementado por completo por el ingeniero de software asignado.

## Secciones de la Aplicación Web

La aplicación web incluirá las siguientes secciones principales:

1. **Inicio (Landing Page):**

   - Página de entrada que ofrecerá una muestra de cada una de las secciones de la página web.

2. **Sobre Nosotros:**

   - Contendrá un texto descriptivo e imágenes del proyecto.
   - Se debe habilitar una opción de exportación en formato PDF para presentaciones futuras.

3. **Eventos:**

   - Los eventos se mostrarán en tarjetas clickeables con bordes de color que indican su estado.
     - Verde para eventos vigentes.
     - Rojo para eventos pasados.
     - Un badge adicional marcará el "PRÓXIMO" evento destacado.
   - Cada tarjeta será clickeable, permitiendo acceder al detalle de cada evento.

4. **Talleres:**

   - Presentación de talleres en formato de tarjeta.
   - Cada tarjeta incluirá una descripción y un botón de contacto que redirige a WhatsApp con un mensaje prearmado.

5. **Contacto:**
   - Formulario de contacto que redirige a WhatsApp con un mensaje de consulta.

## Exclusiones de la Primera Versión

Para esta primera fase de desarrollo, no se incluirán las siguientes características:

- Sistema de gestión y autenticación de usuarios.
- Detalle extendido de cada taller.
- Sistema de reservas para eventos.
- Galería de imágenes.

## Especificaciones Técnicas

- **Lenguaje y Framework:** Python (Django Templates)
- **Almacenamiento de Imágenes:** Amazon S3
- **Dominio:** Hostinger
- **Despliegue:** Heroku (cuenta educativa gratuita)
- **Repositorio de Código y Deploy:** GitHub con automatización mediante GitHub Actions para las ramas `dev` y `main`.

## Modelos de Datos Necesarios

Se crearán los siguientes modelos en Django:

- **Eventos**
- **Talleres**
- **Locaciones**: Contendrá información de las ubicaciones de los eventos y talleres.
