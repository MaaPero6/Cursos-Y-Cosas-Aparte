¿Qué es la codificación de caracteres UTF-8, y por qué es necesaria?

UTF-8, o UCS Transformation Format 8, es una codificación de caracteres estandarizada ampliamente usada en la web. La codificación de caracteres es el método que usan las computadoras para almacenar caracteres como datos. Esencialmente, todo el texto en una página web es una secuencia de caracteres almacenados como uno o más bytes. En informática, un byte es una unidad de datos que consiste en 8 bits, o dígitos binarios. UTF-8 soporta todos los caracteres del conjunto de caracteres Unicode, e incluye caracteres y símbolos de todos los sistemas de escritura, idiomas y símbolos técnicos. Aquí tienes un ejemplo de cómo usar el elemento meta con el atributo charset para establecer la codificación de caracteres a UTF-8:

<meta charset="UTF-8" />

Al establecer la codificación de caracteres en UTF-8, se asegurará de que el carácter acentuado "e" (é) se muestre correctamente en la página. Aquí hay un ejemplo de código extendido utilizando la codificación de caracteres UTF-8:

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Examples of the UTF-8 encoding</title>
  </head>
  <body>
    <p>Café</p>
  </body>
</html>

Para cada nuevo proyecto que crees, debes incluir este elemento meta con el atributo charset configurado en UTF-8.
