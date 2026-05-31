# BOOLEANOS Y CONDICIONALES

## Operadores de comparacion:
| **Operator** | **Name** | **Description** |
| :--- | :--- | :--- |
| == | Equal to | Checks if two values are equal |
| != | Not equal to | Checks if two values are not equal |
| > | Greater than | Checks if the left value is greater than the right value |
| < | Less than | Checks if the left value is less than the right value |
| >= | Greater than or equal to | Checks if the left value is greater than or equal to the right value |
| <= | Less than or equal to | Checks if the left value is less than or equal to the right value |

### Ejemplos de como funcionan:
```python
print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True
```

## El condicionante mas basico: el `if`
Sintaxis basica:
```python
if condition:
    pass # Code to execute if condition is True
```

- Las sentencias `if` comienzan con la palabra clave `if`.
- `condition` es una expresión que se evalúa como `True` o `False`, seguida de dos puntos (`:`).
- El cuerpo de la sentencia `if` constituye un bloque de código, que es un grupo de sentencias que pertenecen juntas. En Python, el nivel de indentación es lo que define un bloque de código.

> [!NOTE]
> En el ejemplo anterior, el cuerpo de la sentencia `if` contiene una sentencia `pass`. Cuando se ejecuta una sentencia `pass`, no sucede nada. Esta es una palabra clave especial que puede usarse como marcador de posición para código futuro y es útil cuando no se permiten bloques de código vacíos.

> [!WARNING]
> Como hemos dicho antes, la indentación es crucial en Python. Un bloque de código se define por su indentación. Si no indentas correctamente, obtendrás un error. Es el equivalente a meterlo entre llaves {} en otros lenguajes de programacion.

El código dentro del cuerpo de la sentencia `if` se ejecuta solo cuando la condición evalúa a `True`, por ejemplo:
```python
age = 18

if age >= 18:
    print('You are an adult') # You are an adult
```

En el caso anterior, si `age` fuera menor que `18` no se imprime nada por terminal. Pero y si queremos que se imprima algo en el caso de que la condición sea falsa? Para eso usamos el `else`:
```python
age = 12

if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult yet') # You are not an adult yet
```

Puede haber situaciones en las que quieras tener en cuenta múltiples condiciones. Para hacer eso, Python te permite extender tu declaración `if` con la palabra clave `elif` (else if). Por ejemplo:
```python
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child
```

> [!NOTE]
> Podemos encadenar tantos `elif` como queramos.

## ¿Qué son los valores Truthy y Falsy, y cómo funcionan los operadores booleanos y el cortocircuito?
Aunque los operadores de comparación y sentencias condicionales son herramientas poderosas para controlar el flujo de tus programas, a menudo te encontrarás en situaciones en las que necesitas comparar múltiples valores a la vez. Esto puede llevar a sentencias condicionales anidadas, por ejemplo:
```python
is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
```

El ejemplo anterior primero verificará si `is_citizen` es `True`. Si es así, pasará a la sentencia `if` anidada y verificará si `age` es mayor o igual a 18. Dado que `age` es mayor o igual a 18, el mensaje que se imprimirá en la terminal será `You are eligible to vote`. Si `is_citizen` fuera `False`, el mensaje que se imprimiría en la terminal habría sido `You are not eligible to vote`.

> [!NOTE]
> Si estás trabajando con sentencias condicionales más complejas, puedes usar los operadores de Python `and`, `or` y `not`.
> #### Operadores lógicos y cortocircuito
> - **and:** devuelve `True` si ambas condiciones son verdaderas.
> - **or:** devuelve `True` si alguna de las condiciones es verdadera.
> - **not:** invierte el valor de la condición.

En Python, cada valor tiene un valor booleano inherente, o un sentido incorporado de si debe ser tratado como `True` o `False` en un contexto lógico. Muchos valores se consideran truthy, es decir, evalúan a `True` en un contexto lógico. Otros son falsy, lo que significa que evalúan a `False`.

Aquí hay unos ejemplos de valores falsy:
- `None`
- `False`
- Entero `0`
- Flotante `0.0`
- Cadenas vacías `""`

Otros valores como números distintos de cero y cadenas no vacías son truthy.

Si deseas verificar si un valor es truthy o falsy, puedes usar la función incorporada bool(). Esta convierte explícitamente un valor a su equivalente booleano y devuelve `True` para valores truthy y `False` para valores falsy. Aquí hay algunos ejemplos:
```python
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True
```