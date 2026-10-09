# INTRODUCCIÓN A JAVASCRIPT

## ¿Qué es JavaScript y cómo funciona junto a HTML y CSS?

**JavaScript** es un lenguaje de programación potente que añade interactividad y comportamiento dinámico a los sitios web.

Mientras que **HTML** y **CSS** se utilizan para estructurar el contenido y dar estilo a los elementos de una página, JavaScript va más allá permitiendo funcionalidades más complejas, como la gestión de entradas del usuario, animación de elementos o la creación de aplicaciones web completas.

Por ejemplo, cuando haces clic en un botón, envías un formulario o te desplazas sobre un menú, JavaScript determina cómo debe comportarse la página.

---

## Ejemplo de cómo trabajan juntos

Aquí tienes un ejemplo de cómo se integran estas tres tecnologías:

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    h1 {
      color: green;
    }
  </style>
</head>
<body>
  <h1>Hello, World!</h1>
  <button onclick="alert('Button clicked!')">Click me</button>
</body>
</html>
```

### Desglose del ejemplo:
- **HTML**: Se utiliza para definir el contenido y la estructura (un elemento `<h1>` para el título principal y un elemento `<button>` para el botón).
- **CSS**: Se aplica para dar estilo al título, cambiando el color del texto a verde (`color: green;`).
- **JavaScript**: Se encarga de mostrar una ventana de alerta (`alert('Button clicked!')`) cuando se hace clic en el botón.

---

## Resumen de responsabilidades

- **HTML**: Proporciona la **estructura** y el contenido de la página.
- **CSS**: Añade el **estilo** y el diseño visual.
- **JavaScript**: Habilita la **lógica** y el comportamiento interactivo.

> [!NOTE]
> La combinación de HTML, CSS y JavaScript es fundamental para construir experiencias web modernas, completas e interactivas.