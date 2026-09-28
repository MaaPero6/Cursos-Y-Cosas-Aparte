# ATRIBUTOS EN HTML

## ¿Qué son los atributos y cómo funcionan?

Un **atributo** es un valor especial colocado dentro de la etiqueta de apertura de un elemento HTML. Los atributos proporcionan información adicional sobre el elemento o especifican cómo debe comportarse.

### Sintaxis básica de un atributo:
```html
<element attribute="value"></element>
```

- **Nombre del atributo**: Seguido por un signo igual (`=`).
- **Valor del atributo**: Encerrado entre comillas (`"value"`). Puede ser una cadena de texto o un número, dependiendo del atributo.

---

## Atributos de enlace: `href` y `target`

El elemento `<a>` (*anchor element* o elemento ancla) se utiliza para crear hipervínculos. El texto encerrado entre las etiquetas de apertura y cierre es la parte cliqueable.

### Ejemplo de enlace con atributos:
```html
<a href="https://www.freecodecamp.org/news/" target="_blank">Visit freeCodeCamp</a>
```

### Funciones de los atributos:
- **`href`**: Especifica la URL de destino del enlace.
- **`target="_blank"`**: Indica al navegador que debe abrir el enlace en una nueva pestaña.

> [!IMPORTANT]
> Sin el atributo `href`, el enlace no funcionará porque no tendría una dirección de destino definida. Por ello, `href` es un atributo esencial para que un hipervínculo sea operativo.

---

## Atributos de imagen: `src` y `alt`

Dos de los atributos más comunes e importantes para el elemento de imagen (`<img>`) son `src` y `alt`:

### Ejemplo de elemento de imagen:
```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Two tabby kittens sleeping together on a couch." />
```

- **`src`** (*source*): Especifica la ruta o ubicación del archivo de imagen a mostrar. Al igual que `href`, es un atributo obligatorio.
- **`alt`** (*alternative text*): Proporciona una descripción breve en texto de la imagen.

> [!NOTE]
> Aunque el atributo `alt` no es técnicamente obligatorio para que la imagen se muestre, se recomienda encarecidamente incluirlo siempre por **accesibilidad web**. Permite que los lectores de pantalla describan la imagen a personas con discapacidades visuales y actúa como texto de respaldo si la imagen falla al cargar.

---

## Atributos booleanos: el atributo `checked`

Algunos atributos tienen una sintaxis única conocida como **atributos booleanos**. Estos atributos no requieren asignarles un valor con `=`; su simple presencia en la etiqueta de apertura indica que la propiedad está activa.

### Ejemplo de casilla de verificación (checkbox):
```html
<input type="checkbox" checked />
```

- **`type="checkbox"`**: Especifica que la entrada del usuario será una casilla de verificación.
- **`checked`**: Indica que la casilla estará marcada por defecto al cargar la página.

> [!NOTE]
> Si el atributo `checked` está presente en la etiqueta, la casilla estará marcada (`True`). Si se omite el atributo, la casilla estará desmarcada por defecto (`False`).

---

## Otros atributos booleanos comunes

Existen varios atributos booleanos ampliamente utilizados en formularios e interactividad HTML:

- **`disabled`**: Deshabilita el elemento e impide que el usuario pueda interactuar o escribir en él.
- **`readonly`**: Hace que el contenido del campo sea de solo lectura (se puede seleccionar y leer, pero no modificar).
- **`required`**: Marca un campo como obligatorio antes de que el usuario pueda enviar un formulario.

### Ejemplo de campo de texto deshabilitado:
```html
<input type="text" disabled />
```

---

## Conclusión

HTML dispone de multitud de atributos que permiten personalizar el comportamiento, la accesibilidad y la apariencia de los elementos web. Comprender cómo utilizar los atributos correctamente es fundamental para construir sitios web funcionales, dinámicos e inclusivos.