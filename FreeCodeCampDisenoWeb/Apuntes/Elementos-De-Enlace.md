# ELEMENTO DE ENLACE (<link>) EN HTML

## ¿Cuál es el papel del elemento `<link>` y cómo enlaza hojas de estilo externas?

El elemento `<link>` se utiliza para vincular recursos externos al documento HTML, tales como hojas de estilo (CSS), fuentes tipográficas e íconos.

### Sintaxis básica para enlazar una hoja de estilo CSS externa:
```html
<link rel="stylesheet" href="./styles.css" />
```

### Desglose de atributos clave:
- **`rel`**: Especifica la relación existente entre el documento HTML y el recurso enlazado. Para hojas de estilo, el valor debe ser `"stylesheet"`.
- **`href`**: Especifica la ruta o URL donde se encuentra el recurso externo.
- **Ruta relativa `./`**: La sintaxis `./` indica al navegador que debe buscar el archivo (en este caso `styles.css`) en la misma carpeta o directorio del archivo HTML actual.

> [!NOTE]
> Es una buena práctica fundamental en el desarrollo web mantener separados la estructura (HTML) y los estilos (CSS) en archivos independientes, enlazándolos mediante la etiqueta `<link>`.

---

## Ubicación del elemento `<link>` en el documento HTML

El elemento `<link>` es un elemento vacío (no tiene etiqueta de cierre) y debe ubicarse siempre dentro de la sección `<head>` del documento HTML.

### Ejemplo de integración en el `<head>`:
```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Ejemplo de uso del elemento link</title>
  <link rel="stylesheet" href="./styles.css" />
</head>
```

---

## Enlazar fuentes externas (Google Fonts)

Es muy común encontrar múltiples elementos `<link>` en proyectos profesionales. Un caso típico es la importación de fuentes tipográficas desde servicios como **Google Fonts**.

### Ejemplo de importación de fuentes tipográficas:
```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  href="https://fonts.googleapis.com/css2?family=Playwrite+CU:wght@100..400&display=swap"
  rel="stylesheet"
/>
```

> [!TIP]
> **Optimización con `rel="preconnect"`:**
> El valor `preconnect` en el atributo `rel` instruye al navegador para establecer una conexión anticipada con el servidor externo (como los servidores de fuentes de Google). Esto reduce la latencia y acelera el tiempo de carga de los recursos visuales.

---

## Enlazar un favicon (Ícono del sitio)

Otro uso indispensable del elemento `<link>` es la definición del **favicon** del sitio web.

### Ejemplo de enlace a un favicon:
```html
<link rel="icon" href="favicon.ico" />
```

- **¿Qué es un favicon?** Es la abreviatura de *favorite icon*. Es la pequeña imagen o logotipo que muestran los navegadores en la pestaña superior junto al título de la página web.

---

## Resumen

El elemento `<link>` es esencial para la modularidad de un sitio web, permitiendo conectar el documento HTML estructurado con hojas de estilo externas, tipografías personalizadas e íconos de identidad de marca.

