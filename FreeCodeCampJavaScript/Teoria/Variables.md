# VARIABLES EN JAVASCRIPT

## ¿Qué es una variable?

En JavaScript, las **variables** actúan como contenedores para almacenar datos a los que puedes acceder y que puedes modificar a lo largo de tu programa.

Puedes imaginar las variables como **cajas etiquetadas** que guardan valores. Gracias a ellas, puedes hacer un seguimiento de números, texto u otros datos y referenciar estos valores siempre que los necesites.

---

## Declaración de variables con `let`

Una forma de declarar una variable en JavaScript es utilizando la palabra clave **`let`**.

```javascript
let age;
```

Cuando declaras una variable sin asignarle un valor inicial, su valor por defecto es **`undefined`** (lo que indica que no tiene ningún valor asignado).

```javascript
let age;
console.log(age); // undefined
```

---

## Asignación de valores e inicialización

Para asignar un valor a una variable se utiliza el **operador de asignación** (`=`):

```javascript
let age = 25;
console.log(age); // 25
```

> [!IMPORTANT]
> El operador de asignación `=` no comprueba igualdad matemática; su función es tomar el valor de la derecha y guardarlo en la variable de la izquierda. El proceso de declarar una variable y asignarle un valor por primera vez se conoce como **inicialización**.

---

## Reasignación de valores

Una ventaja de declarar variables con `let` es que puedes **reasignarles** nuevos valores en cualquier momento mientras se ejecuta el programa (por ejemplo, para actualizar la puntuación en un juego).

```javascript
let age = 25;
console.log(age); // 25

age = 30; // Reasignación
console.log(age); // 30
```

> [!NOTE]
> No es necesario volver a escribir la palabra clave `let` al reasignar un nuevo valor, ya que la variable ya ha sido declarada previamente.

---

## Reglas y buenas prácticas para nombrar variables

Elegir buenos nombres para tus variables hace que tu código sea mucho más legible y mantenible.

### 1. Nombres descriptivos
Usa nombres que describan claramente los datos que representa la variable.

```javascript
// Malos nombres de variables
let x = 10;
let y = "John";

// Buenos nombres de variables
let age = 10;
let userName = "John";
```

### 2. Caracteres permitidos e inicio del nombre
Los nombres de variables deben comenzar por una **letra**, un guion bajo (`_`) o el signo de dólar (`$`). **No pueden empezar por un número**.

```javascript
// Nombres válidos
let age;
let _score;
let $total;

// Nombres inválidos
let 1stPlace; // Error: empieza por un número
```

### 3. Sensibilidad a mayúsculas y minúsculas (*Case-Sensitivity*)
JavaScript distingue entre mayúsculas y minúsculas, por lo que `age` y `Age` son variables completamente distintas.

```javascript
let age = 25;
let Age = 30;

console.log(age); // 25
console.log(Age); // 30
```

### 4. Convención camelCase
En JavaScript, la convención estándar para nombrar variables compuestas por varias palabras es **`camelCase`**: la primera palabra va en minúsculas y cada palabra subsecuente empieza con mayúscula.

```javascript
let thisIsCamelCase;
let anotherExampleVariable;
let freeCodeCampStudents;
```

### 5. Palabras reservadas y caracteres especiales
- **Palabras reservadas**: No puedes usar palabras clave reservadas por el lenguaje (como `let`, `const`, `function`, `return`).
- **Caracteres especiales**: Evita usar símbolos como `!`, `@`, `#`, etc. Limítate a letras, números, `_` y `$`.

> [!TIP]
> Siguiendo estas convenciones, mantendrás un código limpio, legible y fácil de escalar a medida que tus proyectos crezcan.