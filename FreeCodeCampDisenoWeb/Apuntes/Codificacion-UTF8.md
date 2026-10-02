# CODIFICACIÓN DE CARACTERES UTF-8 EN HTML

## ¿Qué es la codificación de caracteres UTF-8 y por qué es necesaria?

**UTF-8** (*UCS Transformation Format 8*) es el estándar universal de codificación de caracteres más utilizado en la web.

La **codificación de caracteres** es el método que utilizan las computadoras para traducir texto a datos binarios que se pueden almacenar y procesar. En informática, el texto se almacena como una secuencia de caracteres donde cada uno se representa mediante uno o varios **bytes** (1 byte = 8 bits).

UTF-8 es compatible con todo el conjunto de caracteres **Unicode**, lo que le permite representar prácticamente cualquier carácter, símbolo, letra acentuada (como la `é` o la `ñ`), signo de puntuación y emoji de todos los idiomas del mundo.

---

## Declaración de UTF-8 en HTML

Para definir la codificación UTF-8 en un documento HTML, se utiliza el elemento `<meta>` con el atributo `charset` dentro de la sección `<head>`:

```html
<meta charset="UTF-8" />
```

### Ejemplo completo en un documento HTML:
```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejemplo de codificación UTF-8</title>
  </head>
  <body>
    <p>Café, España, Niño, 🚀</p>
  </body>
</html>
```

> [!IMPORTANT]
> Si no incluyes la etiqueta `<meta charset="UTF-8" />`, los navegadores podrían interpretar los caracteres acentuados o especiales de forma incorrecta, mostrando símbolos extraños o rotos (conocidos como *mojibake*, por ejemplo `CafÃ©` en lugar de `Café`).

> [!NOTE]
> Se recomienda colocar `<meta charset="UTF-8" />` como una de las primeras etiquetas dentro del `<head>` para garantizar que el navegador conozca el juego de caracteres antes de procesar cualquier texto o script.

