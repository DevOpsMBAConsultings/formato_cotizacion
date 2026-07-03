# Formato Cotización - Plantilla Base (Base Quote Template)

Este es un módulo personalizado para Odoo. Su objetivo principal es servir como una **plantilla base** para modificar y profesionalizar el diseño del reporte en PDF de las **Cotizaciones / Órdenes de Venta** (`sale.report_saleorder_document`).

Al ser una plantilla agnóstica, está diseñada para ser un punto de partida limpio que puede ser fácilmente adaptado a la identidad corporativa y a las necesidades específicas de cualquier empresa.

## Características

El módulo reemplaza la estructura estándar de las cotizaciones en Odoo por un diseño estructurado y corporativo. Los cambios base incluyen:

- **Encabezado Corporativo:** Espacio reservado y organizado para incluir el logotipo de la empresa, nombre comercial, dirección y número de identificación fiscal.
- **Diseño de Dos Columnas (Sección Superior):**
  - **Datos del Cliente:** Muestra de forma clara el nombre, contacto, dirección y el vendedor asignado.
  - **Datos de la Cotización:** Detalla el número de documento, fecha de emisión, fecha de expiración y los términos de pago.
- **Tabla de Productos Estructurada:**
  - Diseño con cabecera resaltada (fácilmente personalizable a los colores corporativos de la empresa) y texto en contraste para mayor legibilidad.
  - Columnas organizadas lógicamente: Descripción, Cantidad, Precio Unitario e Importe Total.
  - Formato numérico y de moneda preparado para ser adaptado según la localización requerida.
- **Resumen Financiero:** 
  - Cálculo ordenado del Subtotal.
  - Desglose explícito de impuestos aplicables.
  - Fila de TOTAL general destacada visualmente.
- **Términos y Condiciones:** Bloque inferior reservado para notas legales, términos comerciales y condiciones de la cotización, en caso de estar definidas.

## Aspectos Técnicos

- **Dependencias:** Este módulo depende de la aplicación base de Ventas (`sale`).
- **Compatibilidad:** Diseñado sobre la estructura de vistas de Odoo (revisar compatibilidad de versión en el manifiesto).
- **Vistas Modificadas:** Actúa heredando y reemplazando elementos de la vista original `sale.report_saleorder_document` mediante `xpath`, lo que asegura que las actualizaciones del sistema base no rompan el formato.

## Instrucciones de Personalización e Instalación

1. Clona o descarga este repositorio dentro de la carpeta de *addons* (módulos personalizados) del servidor Odoo.
2. **Personalización:** 
   - Modifica el archivo XML (`views/report_saleorder.xml`) para ajustar colores, tipografías o literales específicos de impuestos y monedas.
   - Reemplaza la imagen del logo en la ruta estática correspondiente o vincula el campo de la imagen de la compañía.
3. Actualiza la lista de aplicaciones de Odoo (Modo desarrollador activado -> *Actualizar lista de aplicaciones*).
4. Busca el módulo **Formato Cotizacion** e instálalo.
