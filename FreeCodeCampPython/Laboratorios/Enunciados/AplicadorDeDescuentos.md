# Construye una función Apply Discount

En este laboratorio escribirás una función que calcula el precio final de un artículo después de aplicar un descuento porcentual.

Por ejemplo, si el precio de un artículo es 50 y se aplica un descuento de 20, el monto del descuento es 10 y el precio final es 40.

**Objetivo:** Cumple las historias de usuario a continuación para completar el laboratorio.

**Historias de usuario:**

- Debes definir una función llamada apply_discount.

- La función apply_discount debe tomar exactamente dos parámetros: price y discount.

- Si price no es un número (int o float), la función debe devolver la cadena The price should be a number.

- Si discount no es un número (int o float), la función debe devolver la cadena The discount should be a number.

- Si price es menor o igual a 0, la función debería devolver la cadena The price should be greater than 0.

- Si discount es menor que 0 o mayor que 100, la función debe devolver la cadena The discount should be between 0 and 100.

- Si ambas entradas son válidas, la función debe calcular el descuento como un porcentaje del precio.

- La función debe devolver el precio final después de aplicar el descuento.
