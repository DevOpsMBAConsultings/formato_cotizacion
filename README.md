# Formato Cotización - Suplidora JC

Este es un módulo personalizado para Odoo diseñado para la empresa **Suplidora JC**. Su objetivo principal es modificar y personalizar el diseño del reporte en PDF de las **Cotizaciones / Órdenes de Venta** (`sale.report_saleorder_document`).

## Características

El módulo reemplaza la estructura estándar de las cotizaciones en Odoo por un diseño más limpio y corporativo, adaptado a las necesidades de Suplidora JC. Entre los cambios más destacados se incluyen:

- **Encabezado Personalizado:** Incluye el logotipo de la empresa, el nombre comercial, dirección y RUC (Registro Único de Contribuyente).
- **Diseño de Dos Columnas:**
  - **Datos del Cliente:** Muestra el nombre, contacto, dirección y el vendedor asignado.
  - **Cotización:** Detalla el número de cotización, fecha, fecha de expiración y las condiciones de pago.
- **Tabla de Productos Modificada:**
  - Diseño con cabecera en azul corporativo (`#2c3f90`) y texto en blanco para mayor legibilidad.
  - Columnas específicas para: Descripción, Cantidad, Precio y Importe.
  - Símbolo de moneda (B/.) predefinido para Balboas Panameños.
- **Resumen Financiero:** 
  - Cálculo de Subtotal.
  - Inclusión del impuesto ITBMS 7% detallado de forma explícita.
  - Fila de TOTAL destacada en color azul corporativo.
- **Términos y Condiciones:** Espacio en la parte inferior para incluir notas y condiciones de la cotización si están definidas.

## Aspectos Técnicos

- **Dependencias:** Este módulo depende de la aplicación base de Ventas (`sale`).
- **Versión:** `19.0.1.0.0` (Compatible con la arquitectura base, revisar compatibilidad exacta de versión Odoo en despliegue).
- **Vistas Modificadas:** Actúa sobre el template `report_saleorder_document_inherit_suplidora_jc`, heredando de `sale.report_saleorder_document` con prioridad 30 mediante `xpath`.

## Instalación

1. Clona o descarga este repositorio dentro de la carpeta de *addons* (módulos personalizados) de tu servidor Odoo.
2. Actualiza la lista de aplicaciones de Odoo (Modo desarrollador activado -> *Actualizar lista de aplicaciones*).
3. Busca el módulo **Formato Cotizacion** e instálalo.

## Autor

**Antigravity**
