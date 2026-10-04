# LA META DESCRIPCIÓN (`<meta name="description">`) Y EL SEO

## ¿Cuál es el papel de la Meta Descripción y cómo afecta al SEO?

**SEO** (*Search Engine Optimization* u Optimización para Motores de Búsqueda) es el conjunto de prácticas y técnicas diseñadas para mejorar la visibilidad y el posicionamiento de un sitio web en motores de búsqueda como Google o Bing.

Una de las formas fundamentales de optimizar una página web es proporcionar un resumen breve y descriptivo de su contenido utilizando el elemento **`<meta>`**.

---

## Sintaxis de la Meta Descripción

La meta descripción se declara siempre dentro de la sección **`<head>`** del documento HTML:

```html
<meta
  name="description"
  content="Discover expert tips and techniques for gardening in small spaces, choosing the right plants, and maintaining a thriving garden."
/>
```

### Desglose de atributos:
- **`name="description"`**: Indica a los navegadores, motores de búsqueda y herramientas web que este elemento contiene el resumen descriptivo de la página.
- **`content="..."`**: Define el texto descriptivo de la página web.

---

## Visualización en Resultados de Búsqueda (SERP)

La meta descripción **no es visible en el cuerpo de la página web** para los usuarios. Sin embargo, se utiliza directamente en los fragmentos de resultados (*snippets*) de los motores de búsqueda, situándose justo debajo del título del sitio.

### Ejemplos de snippets en buscadores:

> **r/freeCodeCamp**  
> *https://www.reddit.com/r/freeCodeCamp/*  
> **Descripción:** This is the official subreddit for the freeCodeCamp.org community. Learn to code for free together with millions of other people...

> **freeCodeCamp - Repositorio de GitHub**  
> *https://github.com/freeCodeCamp/freeCodeCamp*  
> **Descripción:** Our full-stack web development and machine learning curriculum is completely free and self-paced. We have thousands of interactive coding challenges to help you...

---

## Buenas Prácticas y Consejos de Optimización

> [!IMPORTANT]
> **Longitud concisa:**
> Mantén tus descripciones breves y concisas (idealmente entre 140 y 160 caracteres). Si la descripción es muy larga, los motores de búsqueda la cortarán con puntos suspensivos en la pantalla de resultados.

> [!TIP]
> **Impacto en el tráfico web (CTR):**
> Aunque las meta descripciones no aumentan directamente el posicionamiento en el algoritmo, una descripción atractiva actúa como un anuncio para tu sitio, mejorando la **tasa de clics (CTR)** y atrayendo más visitantes a tu página.

