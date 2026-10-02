# ATRIBUTOS ID Y CLASES EN HTML Y CSS

## ¿Qué son los IDs y las Clases, y cuándo debes usarlos?

En HTML, los atributos `id` y `class` se utilizan para identificar elementos, lo que permite aplicarles estilos visuales mediante **CSS** o manipularlos dinámicamente con **JavaScript**.

---

## El Atributo `id` (Identificador Único)

El atributo **`id`** asigna un identificador **único** a un elemento HTML en todo el documento.

### Ejemplo de elemento con `id`:
```html
<h1 id="title">Movie Review Page</h1>
```

### Selección en CSS (`#`):
En CSS, los identificadores se seleccionan anteponiendo el símbolo de almohadilla (`#`) al nombre del `id`:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Review page Example</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
    <h1 id="title">Movie Review Page</h1>
  </body>
</html>
```

```css
#title {
  color: red;
}
```

### Reglas indispensables para los valores de `id`:
- **Unicidad:** Un mismo nombre de `id` **nunca debe repetirse** en más de un elemento dentro del mismo documento HTML.
- **Sin espacios:** Los valores de `id` no pueden contener espacios (por ejemplo, `<h1 id="main heading">` es un error que causará fallos en estilos y scripts).
- **Caracteres permitidos:** Únicamente letras, números, guiones bajos (`_`) y guiones (`-`).

> [!WARNING]
> Si incluyes espacios en el atributo `id`, el navegador interpretará el espacio como parte del identificador o generará comportamientos no deseados al aplicar estilos CSS y scripts de JavaScript.

---

## El Atributo `class` (Clases Reutilizables)

A diferencia del atributo `id`, el valor del atributo **`class`** no necesita ser único. Una misma clase puede aplicarse a múltiples elementos HTML.

### Ejemplo de elemento con `class`:
```html
<div class="box"></div>
```

### Múltiples clases en un solo elemento:
Se pueden asignar varias clases a un mismo elemento separándolas con un espacio dentro de las comillas:

```html
<div class="box red-box"></div>
```

### Ejemplo completo con múltiples elementos y clases en CSS (`.`):
En CSS, las clases se seleccionan anteponiendo un punto (`.`) al nombre de la clase:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Colored boxes example</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
    <div class="box red-box"></div>
    <div class="box blue-box"></div>
    <div class="box red-box"></div>
    <div class="box blue-box"></div>
  </body>
</html>
```

```css
.box {
  width: 100px;
  height: 100px;
}

.red-box {
  background-color: red;
}

.blue-box {
  background-color: blue;
}
```

---

## Resumen: ¿Cuándo usar `id` vs. `class`?

- **Usar `class` (Selector `.`):** Cuando quieras aplicar un mismo conjunto de estilos o comportamientos a **varios elementos** a lo largo de la página web.
- **Usar `id` (Selector `#`):** Cuando necesites identificar y apuntar a **un único elemento específico** de manera exclusiva.

> [!TIP]
> **Regla general en diseño web:** Se recomienda utilizar principalmente **clases** para la maquetación y estilos CSS debido a su reusabilidad y flexibilidad.