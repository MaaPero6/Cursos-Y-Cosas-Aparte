# INTRODUCCIÓN A HTML Y DISEÑO WEB

## ¿Qué es HTML y qué papel desempeña en la red?

**HTML** (*HyperText Markup Language* o Lenguaje de Marcado de Hipertexto) es el lenguaje de marcado fundamental para crear y estructurar páginas web. Cuando visitas un sitio web y ves contenido como párrafos, títulos, enlaces, imágenes o vídeos, todo eso está definido mediante HTML.

HTML representa el contenido y la estructura de una página web mediante el uso de **elementos**.

### Ejemplo de elementos HTML:
```html
<h1>Main heading element</h1>

<p>I am a paragraph element.</p>
```

- La mayoría de los elementos tienen una **etiqueta de apertura** (de inicio) y una **etiqueta de cierre** (de fin).
- Entre esas dos etiquetas se coloca el contenido, el cual puede ser texto u otros elementos HTML.

Ejemplo de un elemento de párrafo:
```html
<p>I love coding!</p>
```

---

## Etiquetas de apertura y cierre

Tanto las etiquetas de apertura como las de cierre comienzan con un corchete angular izquierdo (`<`) y terminan con un corchete angular derecho (`>`), con el nombre de la etiqueta colocado entre estos corchetes angulares.

Estructura de las etiquetas de apertura y cierre de un párrafo:
```html
<p>

</p>
```

- **Etiqueta de apertura:** `<p>`
- **Etiqueta de cierre:** `</p>` (se distingue por incluir una barra diagonal `/` inmediatamente después del corchete angular izquierdo).

> [!NOTE]
> Aunque los nombres de las etiquetas HTML no distinguen entre mayúsculas y minúsculas, es una convención ampliamente aceptada y una buena práctica escribir siempre las etiquetas en **minúsculas** (por ejemplo, `<p>` en lugar de `<P>`).

---

## Elementos vacíos (Void Elements)

Algunos elementos HTML no tienen etiqueta de cierre ni contenido. Estos se conocen como **elementos vacíos** (*void elements*).

Un ejemplo común es el elemento de imagen (`<img>`):
```html
<img>
```

Los elementos vacíos no pueden contener texto ni otros elementos anidados y sólo cuentan con una etiqueta de inicio. A veces también verás elementos vacíos que incluyen una barra diagonal `/` antes de `>`:
```html
<img />
```

> [!IMPORTANT]
> Aunque muchos formateadores de código como **Prettier** eligen incluir el `/` en elementos vacíos (`<img />`), la especificación oficial de HTML indica que la presencia de la `/` en etiquetas de inicio de elementos vacíos *"no marca la etiqueta como autocerrada, sino que es innecesaria y no tiene ningún efecto"*. En el desarrollo real verás ambas formas, por lo que es importante estar familiarizado con las dos.

---

## Atributos de HTML

Un **atributo** es un valor especial que se utiliza para ajustar o extender el comportamiento y las propiedades de un elemento HTML. Los atributos se incluyen dentro de la etiqueta de apertura.

### Atributo `src`
El atributo `src` (*source*) se utiliza para especificar la ubicación o la URL de la imagen que se va a mostrar:
```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" />
```

### Atributo `alt`
Para los elementos de imagen, es una buena práctica incluir siempre el atributo `alt` (*alternative text*), el cual proporciona un texto descriptivo breve para la imagen:
```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Two tabby kittens sleeping together on a couch." />
```

- **Utilidad del `alt`**:
  - Proporciona accesibilidad para personas que utilizan lectores de pantalla.
  - Se muestra en pantalla si la imagen no logra cargarse por un error en la URL o en la red.

---

## El rol de HTML junto con CSS y JavaScript

¿Es HTML suficiente por sí solo para construir un sitio web? Depende del objetivo:
- Para un proyecto pequeño de práctica que solo muestre texto e imágenes, HTML por sí solo puede ser suficiente.
- Para un sitio web profesional y moderno, es necesario combinar **HTML**, **CSS** y **JavaScript**.

### División de responsabilidades:
- **HTML**: Se encarga del **contenido y la estructura**.
- **CSS**: Se encarga del **estilo visual y el diseño**.
- **JavaScript**: Se encarga de agregar **interactividad y lógica**.

> [!TIP]
> #### Analogía del edificio:
> Podemos comparar la creación de una página web con la construcción de un edificio:
> - **HTML:** Representa los bloques, el concreto y el hierro que forman la estructura de las paredes (la base resistente).
> - **CSS:** Representa el diseño interior y exterior, la pintura y la decoración que hacen que el edificio sea visualmente atractivo.
> - **JavaScript:** Representa el sistema eléctrico y de agua, que asegura que el edificio funcione de manera interactiva.