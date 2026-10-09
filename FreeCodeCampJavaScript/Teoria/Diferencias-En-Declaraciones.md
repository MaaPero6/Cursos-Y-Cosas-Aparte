# DIFERENCIAS EN LAS DECLARACIONES DE VARIABLES (`let`, `const`, `var`)

## ¿Cómo funcionan `let` y `const` en la declaración, asignación y reasignación?

En el JavaScript moderno, **`let`** y **`const`** son las formas preferidas para declarar variables. Aunque ambas se utilizan para almacenar datos, difieren fundamentalmente en cómo manejan la asignación inicial y la reasignación de valores.

---

## La palabra clave `let`

La palabra clave `let` te permite declarar variables cuyo valor puede actualizarse o reasignarse más adelante. Puedes pensar en `let` como un contenedor flexible: una vez guardado un valor, puedes cambiarlo según lo requiera la ejecución del programa.

### Declaración y reasignación con `let`:
```javascript
let score = 10;
console.log(score); // 10

score = 20; // Reasignación permitida
console.log(score); // 20
```

- **Declaración sin valor inicial**: Puedes declarar una variable con `let` sin asignarle un valor de inmediato (su valor por defecto será `undefined`).
```javascript
let age;
console.log(age); // undefined

age = 25;
console.log(age); // 25
```

- **Prohibición de redeclaración**: Aunque una variable declarada con `let` se puede reasignar, **no se puede volver a declarar** con el mismo nombre en el mismo ámbito.
```javascript
let age = 25;
let age = 90; // SyntaxError: Identifier 'age' has already been declared
```

---

## La palabra clave `const`

La palabra clave `const` se utiliza para declarar variables **constantes**. Una vez asignado un valor a una variable `const`, no se puede volver a reasignar.

### Asignación inmutable con `const`:
```javascript
const maxScore = 100;
console.log(maxScore); // 100

maxScore = 200; // TypeError: Assignment to constant variable.
```

> [!IMPORTANT]
> A diferencia de `let`, las variables declaradas con `const` **deben inicializarse obligatoriamente en el momento de su declaración**. Intentar declararla sin asignarle un valor generará un error de sintaxis:
> ```javascript
> const age; // SyntaxError: Missing initializer in const declaration
> ```

Al igual que con `let`, tampoco es posible volver a declarar una variable `const` existente.

---

## Comparativa: `let` vs `const` vs `var`

| Característica | `let` | `const` | `var` (Tradicional) |
| :--- | :--- | :--- | :--- |
| **Reasignable** | Sí | No | Sí |
| **Inicialización obligatoria** | No (`undefined`) | Sí | No (`undefined`) |
| **Redeclarable** | No | No | Sí |
| **Uso recomendado** | Para valores cambiantes | Opción por defecto para constantes | No recomendado (ámbito global/de función propenso a errores) |

> [!NOTE]
> **La palabra clave `var`**: Es la forma antigua de declarar variables en JavaScript. Funciona de manera similar a `let` respecto a la reasignación, pero tiene un ámbito (*scope*) más amplio que suele causar errores imprevistos. En el desarrollo moderno se desaconseja su uso.

---

## ¿Cuándo usar cada una?

- **Usa `const`** por defecto para cualquier valor o configuración que no deba cambiar accidentalmente durante la ejecución.
- **Usa `let`** cuando sepas que el valor de la variable cambiará a lo largo del tiempo (como el puntaje de un juego, un contador de bucle o una bandera booleana).