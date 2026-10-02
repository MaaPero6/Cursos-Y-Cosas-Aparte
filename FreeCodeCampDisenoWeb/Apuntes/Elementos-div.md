# ELEMENTOS DIV Y SEMÁNTICA EN HTML

## ¿Qué son los elementos `<div>` y cuándo deberías usarlos?

El elemento **`<div>`** se utiliza como un contenedor genérico a nivel de bloque para agrupar otros elementos HTML. 

Principalmente, usarás el elemento `<div>` cuando necesites agrupar varios elementos que compartirán un mismo conjunto de reglas o estilos CSS.

### Ejemplo básico de un elemento `<div>`:
```html
<div>
  <p>Example paragraph element.</p>
</div>
```

---

## Uso responsable del `<div>`: Evitar el exceso

Aunque el elemento `<div>` se utiliza con mucha frecuencia en bases de código del mundo real, se debe tener cuidado de **no usarlo en exceso**. Hay muchas ocasiones en las que otro elemento HTML semántico resultará más apropiado.

Por ejemplo, si deseas dividir tu contenido en secciones temáticas, el elemento **`<section>`** es más adecuado que un simple `<div>`.

### Ejemplo de uso del elemento semántico `<section>`:
```html
<section>
  <h2>Mammals</h2>
  <p>
    Mammals are warm-blooded animals with fur or hair. Most give birth to live
    young.
  </p>
  <ul>
    <li>Lion</li>
    <li>Elephant</li>
    <li>Dolphin</li>
  </ul>
</section>
```

---

## ¿Qué es la semántica en HTML y por qué es importante?

La **semántica** se refiere al significado de las palabras o elementos en un lenguaje. En HTML, los elementos poseen un significado explícito para el navegador y las herramientas de accesibilidad:

- **Elemento `<div>`**: **No semántico**. No aporta ninguna información descriptiva sobre el contenido que contiene.
- **Elemento `<section>`**: **Semántico**. Indica claramente que su contenido constituye una sección temática lógica.

> [!IMPORTANT]
> **Beneficios de utilizar HTML semántico:**
> Al usar elementos semánticos en lugar de `<div>` genéricos, el navegador, los motores de búsqueda (SEO) y las tecnologías de asistencia (como lectores de pantalla) comprenderán y procesarán la estructura de la página correctamente en cualquier dispositivo.

