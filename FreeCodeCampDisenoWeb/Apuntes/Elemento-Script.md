# EL ELEMENTO SCRIPT (`<script>`) EN HTML

## ¿Cuál es el papel del elemento `<script>` y cómo se enlaza a archivos JavaScript externos?

El elemento **`<script>`** se utiliza para incrustar o vincular código ejecutable en un documento HTML, siendo **JavaScript** el lenguaje por excelencia utilizado para este fin.

### ¿Para qué se usa JavaScript en las páginas web?
JavaScript aporta **interactividad y comportamiento dinámico** a los sitios web. Algunos ejemplos comunes incluyen:
- Formularios dinámicos que validan la entrada del usuario en tiempo real.
- Carruseles de imágenes y galerías interactivas.
- Juegos web y animaciones complejas.
- Manipulación de elementos del documento (DOM).

---

## Modos de inclusión de JavaScript

Existen dos formas principales de incluir código JavaScript en una página web:

### 1. JavaScript integrado (Inline Script)
Se escribe el código directamente entre las etiquetas de apertura `<script>` y cierre `</script>` dentro del documento HTML:

```html
<body>
  <script>
    alert("Welcome to freeCodeCamp");
  </script>
</body>
```

---

### 2. JavaScript externo (External Script)
Se vincula un archivo de script independiente mediante el atributo **`src`** (*source*):

```html
<script src="path-to-javascript-file.js"></script>
```

- **Atributo `src`**: Especifica la ruta relativa o la URL donde se encuentra guardado el archivo JavaScript externo.

---

## Principio de diseño: Separación de responsabilidades

Aunque es técnicamente posible escribir JavaScript directamente dentro del documento HTML, la mejor práctica en el desarrollo web profesional es utilizar archivos externos.

> [!NOTE]
> **Separación de responsabilidades (*Separation of Concerns*):**
> Es un principio fundamental del diseño de software que promueve dividir un programa en secciones independientes donde cada una aborda una responsabilidad distinta:
> - **HTML**: Define la **estructura** y el contenido.
> - **CSS**: Controla el **diseño** y la presentación visual.
> - **JavaScript**: Gestiona la **lógica** e interactividad.

> [!TIP]
> **Ubicación recomendada:**
> Generalmente las etiquetas `<script>` se colocan al final del `<body>` (justo antes de la etiqueta de cierre `</body>`) o en el `<head>` utilizando atributos como `defer` para evitar bloquear el renderizado visual de la página mientras se descarga el script.