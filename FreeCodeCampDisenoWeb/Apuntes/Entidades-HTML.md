# ENTIDADES Y REFERENCIAS DE CARACTERES EN HTML

## ¿Qué son las entidades HTML y por qué son necesarias?

Una **entidad HTML** (o referencia de carácter) es una secuencia especial de caracteres utilizada para representar símbolos reservados o caracteres especiales en HTML.

### El problema de los caracteres reservados:
Supongamos que deseas mostrar en pantalla la frase de texto: `This is an <img/> element`.

Si escribes directamente el código en tu archivo HTML:
```html
<!-- CÓDIGO INCORRECTO -->
<p>This is an <img /> element</p>
```

El analizador del navegador (*HTML parser*) interpreta el símbolo de menor que (`<`) seguido del nombre de una etiqueta como el inicio de un elemento HTML real (en este caso, intentará renderizar una imagen en medio del texto).

---

## Solución: Tipos de referencias de caracteres

Para mostrar caracteres reservados como texto plano sin confundir al navegador, se utilizan las entidades HTML. Existen tres tipos de referencias:

---

### 1. Referencias de caracteres nombradas (Named References)
Comienzan con un signo de ampersand (`&`), seguido del nombre asignado al carácter, y terminan con un punto y coma (`;`).

#### Ejemplo de uso:
```html
<p>This is an &lt;img /&gt; element</p>
```

Al renderizarse en el navegador, el texto mostrado será:
> `This is an <img /> element`

#### Ejemplo renderizando código HTML como texto:
```html
<p>&lt;p&gt;learning is fun&lt;/p&gt;</p>
```
> Renderizado en pantalla: `<p>learning is fun</p>`

#### Entidades nombradas más comunes:
- **`&lt;`**: Muestra `<` (*less-than*)
- **`&gt;`**: Muestra `>` (*greater-than*)
- **`&amp;`**: Muestra `&` (*ampersand*)
- **`&quot;`**: Muestra `"` (*comilla doble*)
- **`&nbsp;`**: Muestra un espacio en blanco de no separación (*non-breaking space*)

---

### 2. Referencias numéricas decimales (Decimal Numeric References)
Comienzan con el signo de ampersand y la almohadilla (`&#`), seguido de uno o más dígitos en código decimal Unicode, y terminan con punto y coma (`;`).

#### Sintaxis y ejemplos:
```html
<p>Símbolo menor que: &#60;</p>
<p>Copyright: &#169;</p>
<p>Marca registrada: &#174;</p>
```

- **`&#60;`**: Muestra `<`
- **`&#169;`**: Muestra `©` (Símbolo de copyright)
- **`&#174;`**: Muestra `®` (Símbolo de marca registrada)

---

### 3. Referencias numéricas hexadecimales (Hexadecimal Numeric References)
Comienzan con el signo de ampersand, la almohadilla y la letra x (`&#x`), seguido de los dígitos hexadecimales Unicode, y terminan con punto y coma (`;`).

#### Sintaxis y ejemplos:
```html
<p>Símbolo menor que: &#x3C;</p>
<p>Símbolo del Euro: &#x20AC;</p>
<p>Letra griega Omega: &#x03A9;</p>
```

- **`&#x3C;`**: Muestra `<`
- **`&#x20AC;`**: Muestra `€` (Símbolo del Euro)
- **`&#x03A9;`**: Muestra `Ω` (Letra griega mayúscula Omega)

---

## Tabla resumen de entidades comunes

| Carácter / Símbolo | Nombre | Referencia Nombrada | Ref. Decimal | Ref. Hexadecimal |
| :---: | :--- | :---: | :---: | :---: |
| `<` | Menor que | `&lt;` | `&#60;` | `&#x3C;` |
| `>` | Mayor que | `&gt;` | `&#62;` | `&#x3E;` |
| `&` | Ampersand | `&amp;` | `&#38;` | `&#x26;` |
| `©` | Copyright | `&copy;` | `&#169;` | `&#xA9;` |
| `®` | Marca Registrada | `&reg;` | `&#174;` | `&#xAE;` |
| `€` | Euro | `&euro;` | `&#8364;` | `&#x20AC;` |

> [!NOTE]
> **Recomendación de uso:**
> Las referencias nombradas (como `&lt;` o `&copy;`) suelen ser más fáciles de recordar y leer en el código fuente que los códigos numéricos decimales o hexadecimales.

