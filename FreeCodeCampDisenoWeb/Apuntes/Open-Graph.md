# ETIQUETAS OPEN GRAPH (`og:*`) Y REDES SOCIALES

## ¿Cuál es el papel de las etiquetas Open Graph y cómo afectan al SEO?

El **Protocolo Open Graph (OG)** es un estándar creado por Facebook que permite controlar exactamente cómo se muestra la vista previa de una página web cuando su enlace es compartido en redes sociales (Facebook, LinkedIn, Twitter/X, Discord, Slack, WhatsApp, etc.).

Al definir las propiedades de Open Graph mediante elementos **`<meta>`** dentro de la sección **`<head>`**, se genera una tarjeta visual atractiva (con título, descripción e imagen) que incita a los usuarios a hacer clic e interactuar con la publicación.

---

## Las 4 Propiedades Fundamentales de Open Graph

Aunque existen múltiples etiquetas OG opcionales (como `og:description`, `og:locale`, `og:video` u `og:audio`), hay **cuatro propiedades imprescindibles** que todo sitio web debe definir:

---

### 1. `og:title` (Título del contenido)
Define el título principal que se mostrará en la tarjeta de la publicación en redes sociales.

```html
<meta property="og:title" content="freeCodeCamp.org" />
```

- **`property="og:title"`**: Identifica la propiedad de título de Open Graph.
- **`content="..."`**: Especifica el texto del título.

---

### 2. `og:type` (Tipo de contenido)
Representa la naturaleza o categoría del contenido compartido.

```html
<meta property="og:type" content="website" />
```

- **Valores comunes**: `website` (sitios web generales), `article` (artículos/blogs), `video.movie` (vídeos), `music.song` (música).

---

### 3. `og:image` (Imagen de vista previa)
Especifica la URL de la imagen principal que acompañará la publicación en las redes sociales.

```html
<meta
  property="og:image"
  content="https://cdn.freecodecamp.org/platform/universal/fcc_meta_1920X1080-indigo.png"
/>
```

> [!IMPORTANT]
> **Requisitos de la imagen:**
> Para garantizar una óptima visualización en pantallas de alta resolución, las imágenes de Open Graph deben tener buena calidad y la proporción adecuada:
> - **Recomendado por Facebook:** **1200 x 630 píxeles** (relación de aspecto 1.91:1).
> - **Mínimo absoluto:** **600 x 315 píxeles** para poder mostrar la tarjeta con imagen grande.

---

### 4. `og:url` (URL canónica)
Especifica la URL oficial y permanente del documento que se está compartiendo.

```html
<meta property="og:url" content="https://www.freecodecamp.org" />
```

---

## Ejemplo Completo en el `<head>`

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>freeCodeCamp.org</title>

  <!-- Open Graph Meta Tags -->
  <meta property="og:title" content="freeCodeCamp.org" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="https://cdn.freecodecamp.org/platform/universal/fcc_meta_1920X1080-indigo.png" />
  <meta property="og:url" content="https://www.freecodecamp.org" />
  <meta property="og:description" content="Aprende a programar gratis con proyectos interactivos y certificaciones." />
</head>
```

---

## ¿Cómo afectan las etiquetas Open Graph al SEO?

Aunque las etiquetas Open Graph no influyen directamente en los algoritmos de clasificación de búsquedas tradicionales (como Google Search):

> [!TIP]
> **Beneficio indirecto en SEO:**
> Una publicación en redes sociales bien optimizada con Open Graph captura la atención visual de los usuarios y genera una **tasa de clics (CTR)** mucho mayor. El aumento en el tráfico entrante, el tiempo de permanencia y las menciones sociales transmiten señales positivas de relevancia a los motores de búsqueda.

