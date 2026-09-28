# ESTRUCTURA BASE Y BOILERPLATE EN HTML

## ¿Qué es un boilerplate HTML y por qué es importante?

Un **boilerplate** (o código repetitivo) en HTML es una plantilla de código estándar lista para usar. Se puede comparar con los cimientos de una casa: proporciona la estructura básica e indispensable que todo documento HTML requiere para funcionar correctamente.

Utilizar un boilerplate ahorra tiempo al iniciar nuevos proyectos y ayuda a garantizar que las páginas web estén configuradas siguiendo los estándares web.

### Ejemplo de un boilerplate HTML estándar:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>freeCodeCamp</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
  </body>
</html>
```

---

## Desglose de las partes clave de un boilerplate

### 1. Declaración `<!DOCTYPE html>`
```html
<!DOCTYPE html>
```
Indica al navegador web qué versión de HTML se está utilizando (en este caso, declara que el documento utiliza el estándar **HTML5**).

---

### 2. Etiqueta raíz `<html>`
```html
<!DOCTYPE html>
<html lang="en">
  <!-- Todo el contenido del documento va aquí dentro -->
</html>
```
Es el elemento raíz que envuelve absolutamente todo el contenido del documento HTML. El atributo `lang="en"` (o `lang="es"`) especifica el idioma principal de la página, lo que resulta fundamental para accesibilidad y motores de búsqueda.

---

### 3. Las dos secciones principales: `<head>` y `<body>`
Dentro de la etiqueta `<html>`, el documento se divide estructuralmente en dos partes diferenciadas:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Información de metadatos y configuración -->
  </head>
  <body>
    <!-- Contenido visible: títulos, párrafos, imágenes, etc. -->
  </body>
</html>
```

---

## La sección `<head>` (Configuración tras bambalinas)

La sección `<head>` contiene metadatos y configuraciones técnicas que no se muestran directamente en la pantalla, pero son cruciales para el funcionamiento del sitio web:

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Document Title Goes Here</title>
  <link rel="stylesheet" href="./styles.css" />
</head>
```

### Elementos clave del `<head>`:
- **`<meta charset="UTF-8" />`**: Especifica la codificación de caracteres **UTF-8**, permitiendo representar correctamente acentos, caracteres especiales y emojis.
- **`<meta name="viewport" content="width=device-width, initial-scale=1.0" />`**: Configura la vista para que la página sea responsiva y se adapte correctamente al tamaño de pantalla de dispositivos móviles.
- **`<title>`**: Define el título del documento que se muestra en la pestaña superior del navegador.
- **`<link rel="stylesheet" href="./styles.css" />`**: Enlaza el archivo de hoja de estilos CSS externa donde se define el diseño visual.

> [!NOTE]
> Los metadatos de los elementos `<meta>` también proporcionan información esencial a buscadores (SEO) y redes sociales para generar la vista previa al compartir el enlace.

---

## La sección `<body>` (Contenido visible)

La sección `<body>` es el contenedor donde se coloca todo el contenido que los usuarios verán e interactuarán en la pantalla:

```html
<body>
  <h1>I am a main title</h1>
  <p>Example paragraph text</p>
</body>
```

Aquí se ubican los encabezados (`<h1>`-`<h6>`), párrafos (`<p>`), imágenes (`<img>`), enlaces (`<a>`), formularios, botones y cualquier otro elemento visible.

---

## ¿Por qué es fundamental utilizar un boilerplate?

- **Estructura correcta**: Asegura que la página cumpla con los estándares oficiales de HTML.
- **Compatibilidad**: Garantiza un comportamiento consistente entre distintos navegadores.
- **Prevención de errores**: Evita problemas de codificación de caracteres o fallos de renderizado en dispositivos móviles.

> [!TIP]
> A medida que adquieras más experiencia, puedes personalizar tu propio boilerplate personal añadiendo etiquetas meta adicionales (como Open Graph para redes sociales) o scripts habituales, lo que acelerará tu flujo de trabajo en nuevos proyectos.

