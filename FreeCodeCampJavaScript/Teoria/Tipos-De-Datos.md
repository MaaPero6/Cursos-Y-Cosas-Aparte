# TIPOS DE DATOS EN JAVASCRIPT

## ¿Qué es un tipo de dato y qué es una variable?

En JavaScript, un **tipo de dato** representa la categoría o clase del valor que estás almacenando (como un número, un texto o una condición lógica).

Una **variable** es un contenedor con nombre que almacena un valor de un tipo de dato específico, lo que te permite hacer referencia a él y manipularlo a lo largo de tu programa.

Es un concepto similar al que se utiliza en matemáticas:
```javascript
x = 2
y = 4

x + y // 6
```
Puedes definir tus propios nombres de variables, asignarles valores y realizar operaciones con ellos. Los tipos de datos le indican al programa cómo debe tratar y procesar cada valor.

---

> [!NOTE]
> - **`console.log()`**: Es una función utilizada para imprimir información en la consola del navegador, muy útil para depurar código.
> - **Comentarios (`//`)**: Se usan para añadir notas en el código que el navegador ignorará al ejecutar la aplicación.

---

## Tipos de datos primitivos

### 1. Numbers (Números)
El tipo de dato `Number` representa tanto números enteros (*integers*) como números con decimales (*floating-point*).

```javascript
// Ejemplos de enteros
console.log(3);
console.log(5);
console.log(-67);

// Ejemplos de números decimales (floating-point)
console.log(3.14);
console.log(7.2);
console.log(-14.5);
```

### 2. Strings (Cadenas de texto)
Un `String` es una secuencia de caracteres utilizada para representar texto. Se puede delimitar usando comillas dobles (`"..."`) o comillas simples (`'...'`).

```javascript
// Cadena con comillas dobles
console.log("I love to code!");

// Cadena con comillas simples
console.log('I love to code!');
```

### 3. Booleans (Booleanos)
Un `Boolean` representa solo uno de dos valores posibles: `true` (verdadero) o `false` (falso).

```javascript
let isLoggedIn = true;
let isSubscribed = false;
```
Se utilizan principalmente para evaluar condiciones y controlar el flujo del programa (por ejemplo, mostrar el panel de control si el usuario ha iniciado sesión o la página de login si no lo ha hecho).

### 4. `undefined` y `null`
- **`undefined`**: Significa que una variable ha sido declarada pero aún no se le ha asignado ningún valor.
- **`null`**: Es un valor asignado intencionalmente para representar la ausencia total de valor o un objeto "vacío".

```javascript
let item;
console.log(item); // undefined

let selectedColor = null; // Intencionalmente sin valor
```

### 5. Symbol y BigInt
Son tipos de datos primitivos más específicos:

- **`Symbol`**: Representa un valor único e inmutable que a menudo se usa como clave para propiedades únicas en objetos.
```javascript
const uniqueKey = Symbol('mySymbol');
```

- **`BigInt`**: Permite trabajar con enteros numéricos extremadamente grandes que superan el límite del tipo `Number` convencional (se define agregando una `n` al final del número).
```javascript
const bigNumber = 1234567890123456789012345678901234567890n;
```

---

## Tipos de datos complejos

### Object (Objetos)
A diferencia de los tipos primitivos, un `Object` es una estructura de datos compleja que permite almacenar colecciones de pares clave-valor (*key-value pairs*).

```javascript
const user = {
  name: "Alice",
  age: 30
};

console.log(user.name); // Alice
```

---

> [!TIP]
> Comprender los tipos de datos en JavaScript es esencial para manipular la información de forma correcta, ya que cada tipo tiene sus propias propiedades y comportamientos específicos.

