# Bucles y secuencias

## ¿Qué son las listas y cómo funcionan?
El tipo de dato lista es una secuencia ordenada de elementos que pueden estar compuestos por cadenas, números o incluso otras listas. Las listas son mutables y usan indexación basada en cero, lo que significa que el primer elemento de la lista está en el índice cero.

```python
cities = ['Los Angeles', 'London', 'Tokyo']
```

Para acceder a un elemento de la lista `cities`, puedes referenciar su número de índice en la secuencia:
```python
cities = ['Los Angeles', 'London', 'Tokyo']
cities[0]
```
El resultado sería:
```text
Los Angeles
```

El indexado negativo se usa para acceder a elementos comenzando desde el final de la lista en lugar del principio en el índice 0. Para acceder al último elemento de cualquier lista, puedes usar `-1` así:
```python
cities = ['Los Angeles', 'London', 'Tokyo']
cities[-1]
```
El resultado sería:
```text
Tokyo
```

Otra forma de crear una lista es usar la estructura `list()`. La estructura `list()` se usa para convertir un iterable en una lista así:
```python
developer = 'Jessica'
print(list(developer))
```
El resultado sería:
```text
['J', 'e', 's', 's', 'i', 'c', 'a']
```

Para obtener el número total de elementos en una lista, puedes usar la función `len()` así:
```python
numbers = [1, 2, 3, 4, 5]
len(numbers)
```
El resultado sería:
```text
5
```

Dado que las listas son mutables, puedes actualizar cualquier elemento en la lista siempre que pases un número de índice válido asignándole un nuevo valor:
```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages)
```
El resultado sería:
```text
['JavaScript', 'Java', 'C++', 'Rust']
```

Si pasas un índice (ya sea positivo o negativo) que está fuera de los límites de la lista, recibirás un `IndexError`:
```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[10] = 'JavaScript'

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
"""
```

Si quieres eliminar un elemento de una lista puedes usar la palabra clave `del` así:
```python
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer)
```
El resultado sería:
```text
['Jane Doe', 'Python Developer']
```

A veces es útil verificar si un elemento está dentro de la lista. Para hacer eso, puedes usar la palabra clave `in` así:
```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']

'Rust' in programming_languages      # True
'JavaScript' in programming_languages # False
```

Es común tener listas anidadas dentro de otras listas. Para acceder a la lista anidada, necesitarás usar su posición (índice 2 en este caso):
```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2]
```
El resultado sería:
```text
['Python', 'Rust', 'C++']
```

Luego, para acceder al segundo idioma de esa lista anidada, usas un segundo par de corchetes con el índice `1` así:
```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2][1]
```
El resultado sería:
```text
Rust
```

Desempaquetar valores de una lista es una técnica usada para asignar valores de una lista a nuevas variables de forma directa:
```python
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer
```
> [!NOTE]
> Si la cantidad de variables en el lado izquierdo del operador de asignación no coincide con la cantidad total de elementos en la lista, recibirás un `ValueError`.

Si necesitas recolectar cualquier elemento restante de una lista, puedes usar el operador asterisco (`*`) así:
```python
developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer
```

Similar a las cadenas, puedes acceder a porciones de una lista usando el operador slice (`:`):
```python
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie']
desserts[1:3]
```
El resultado sería:
```text
['Cookies', 'Ice Cream']
```

También puedes especificar un intervalo de paso que determina cuánto incrementar entre los índices. Si quieres extraer solo los números en posiciones de paso 2 comenzando desde el índice 1:
```python
numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2]
```
El resultado sería:
```text
[2, 4, 6]
```

---

## ¿Cuáles son algunos métodos comunes utilizados para listas?

El método `append()` se usa para agregar un elemento al final de la lista:
```python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
```
El resultado sería:
```text
[1, 2, 3, 4, 5, 6]
```

Si quieres agregar una lista al final de otra usando `append()`, se añadirá como una sublista anidada:
```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers)
```
El resultado sería:
```text
[1, 2, 3, 4, 5, [6, 8, 10]]
```

Con `extend()` puedes desarmar los elementos e incorporar múltiples ítems individuales al final de una lista:
```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers)
```
El resultado sería:
```text
[1, 2, 3, 4, 5, 6, 8, 10]
```

Para insertar un elemento en un índice específico de una lista, puedes usar el método `insert()`. Acepta dos argumentos: el índice de destino y el elemento a insertar:
```python
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)
print(numbers)
```
El resultado sería:
```text
[1, 2, 2.5, 3, 4, 5]
```

Si quieres eliminar un elemento por su valor, puedes usar el método `remove()`. Ten en cuenta que solo eliminará la primera ocurrencia que encuentre:
```python
numbers = [1, 2, 3, 4, 5, 5, 5]
numbers.remove(5)
print(numbers)
```
El resultado sería:
```text
[1, 2, 3, 4, 5, 5]
```

Para eliminar un elemento en un índice específico y recuperarlo, puedes usar el método `pop()`:
```python
numbers = [1, 2, 3, 4, 5]
numbers.pop(1)  # Devuelve el número 2
```
> [!NOTE]
> Si no especificas un índice en el método `pop()`, se elimina y devuelve automáticamente el último elemento de la lista.

Si necesitas vaciar la lista por completo, puedes usar el método `clear()` así:
```python
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)
```
El resultado sería:
```text
[]
```

El método `sort()` se usa para ordenar los elementos en el lugar (modificando la lista original):
```python
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()
print(numbers)
```
El resultado sería:
```text
[1, 2, 19, 35, 41, 67]
```

A diferencia del método `sort()`, la función `sorted()` devuelve una nueva lista ordenada sin alterar la original:
```python
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
```
El resultado sería:
```text
[1, 2, 19, 35, 41, 67]
[19, 2, 35, 1, 67, 41]
```

El método `reverse()` invertirá los elementos de la lista en el lugar:
```python
numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()
print(numbers)
```
El resultado sería:
```text
[1, 2, 3, 4, 5, 6]
```

El método `index()` se usa para encontrar la primera posición donde aparece un elemento:
```python
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java')  # Devuelve 1
```
> [!NOTE]
> Si el elemento buscado no se encuentra dentro de la lista, Python lanzará un `ValueError`.

---

## ¿Qué son las tuplas y cómo funcionan?
Una tupla es un tipo de dato de Python usado para crear una secuencia ordenada de valores. Las tuplas pueden contener conjuntos mixtos de tipos de datos:
```python
developer = ('Alice', 34, 'Rust Developer')
```
Las tuplas son similares a las listas, pero son **inmutables**. Esto significa que sus elementos no pueden cambiarse una vez creadas. Si intentas actualizar un elemento, obtendrás un `TypeError`:
```python
programming_languages = ('Python', 'Java', 'C++', 'Rust')
programming_languages[0] = 'JavaScript'

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: "tuple" object does not support item assignment
"""
```

Para acceder a un elemento de una tupla, usas los corchetes y su número de índice:
```python
developer = ('Alice', 34, 'Rust Developer')
developer[1]  # Devuelve 34
```

También puedes usar indexación negativa para ir desde el final hacia atrás:
```python
numbers = (1, 2, 3, 4, 5)
numbers[-2]  # Devuelve 4
```

Si intentas buscar un índice que no existe, te dará un `IndexError`:
```python
numbers = (1, 2, 3, 4, 5)
numbers[7]

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
"""
```

También puedes crear una tupla usando su constructor `tuple()` pasándole iterables como cadenas, listas u otras tuplas:
```python
developer = 'Jessica'
print(tuple(developer))
```
El resultado sería:
```text
('J', 'e', 's', 's', 'i', 'c', 'a')
```

Para comprobar si un elemento existe dentro de la tupla, utilizas la palabra clave `in`:
```python
programming_languages = ('Python', 'Java', 'C++', 'Rust')

'Rust' in programming_languages       # True
'JavaScript' in programming_languages # False
```

También puedes desempaquetar elementos de una tupla en variables independientes de forma limpia:
```python
developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer
```

Y usar el operador asterisco (`*`) para agrupar los elementos restantes en una lista:
```python
developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer
```

Puedes extraer porciones de una tupla con el operador slice (`:`), devolviendo una nueva tupla:
```python
desserts = ('cake', 'pie', 'cookies', 'ice cream')
desserts[1:3]
```
El resultado sería:
```text
('pie', 'cookies')
```

Intentar borrar un elemento concreto de la tupla usando `del` provocará un error de tipo por su inmutabilidad:
```python
developer = ('Jane Doe', 23, 'Python Developer')
del developer[1]

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: "tuple" object doesn't support item deletion
"""
```

> [!NOTE]
> **¿Cuándo usar una Tupla en lugar de una Lista?**
> Si necesitas una colección dinámica donde vayas a agregar, eliminar y modificar elementos, debes usar una lista. Si trabajas con una colección fija de datos que no debe cambiar bajo ningún concepto, debes usar una tupla.

---

## Métodos comunes de Tuplas

El método `count()` sirve para saber cuántas veces se repite un elemento dentro de la tupla:
```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('Rust')
```
El resultado sería:
```text
2
```
Si el ítem no está en la tupla, devuelve `0`. Si no le pasas argumentos, lanzará un `TypeError`.
```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('JavaScript')  # Devuelve 0
```

El método `index()` te da la posición de la primera ocurrencia del elemento indicado:
```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('Java')  # Devuelve 1
```
> [!NOTE]
> Si el elemento no se encuentra, Python lanzará un `ValueError`.

Puedes pasarle un segundo argumento numérico a `index()` para indicarle a partir de qué índice inicial empezar a buscar:
```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3)
```
El resultado sería:
```text
5
```

Y también puedes acotar la búsqueda añadiendo un tercer argumento numérico como límite final (sin incluirlo):
```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
programming_languages.index('Python', 2, 5)
```
El resultado sería:
```text
2
```

Puedes ordenar los elementos utilizando la función global `sorted()`, que generará una nueva lista ordenada a partir de los datos de la tupla:
```python
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers)
```
El resultado sería:
```text
[2, 3, 7, 13, 18, 45, 67, 78]
```

Puedes personalizar el orden utilizando los parámetros opcionales `key` y `reverse`. Por ejemplo, para ordenar por longitud de caracteres usando `key=len`:
```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
sorted(programming_languages, key=len)
```
El resultado sería:
```text
['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']
```

O en orden descendente con `reverse=True`:
```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, reverse=True))
```
El resultado sería:
```text
['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']
```

---

## ¿Cómo funcionan los bucles?
Los bucles se usan para repetir un bloque de código un número determinado de veces.

El primer bucle que veremos es el bucle `for`, que recorre secuencias (listas, tuplas, cadenas):
```python
programming_languages = ['Rust', 'Java', 'Python', 'C++']
for language in programming_languages:
    print(language)
```
El resultado sería:
```text
Rust
Java
Python
C++
```

Nota que el `print(language)` está indentado dentro del bucle. Sin esa indentación, obtendrías un `IndentationError`:
```python
programming_languages = ['Rust', 'Java', 'Python', 'C++']
for language in programming_languages:
print(language)

"""
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
IndentationError: expected an indented block after 'for' statement on line 3
"""
```

También puedes usar un bucle `for` para recorrer cadenas carácter por carácter:
```python
for char in 'code':
    print(char)
```
El resultado sería:
```text
c
o
d
e
```

Los bucles `for` pueden anidarse, aquí tienes un ejemplo:
```python
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)
```
El resultado sería:
```text
Fruit Apple
Fruit Carrot
Fruit Banana
Vegetable Apple
Vegetable Carrot
Vegetable Banana
```
> [!NOTE]
> El bucle externo iterará a través de cada `category` en la lista `categories`. Para cada `category`, el bucle interno iterará a través de cada `food` en la lista `foods`.

Otro tipo de estructura que puedes usar en Python es la estructura `while`. Este tipo de estructura repetirá un bloque de código hasta que la condición sea `False`. Aquí tienes un ejemplo de cómo usar una estructura `while` para un juego de adivinanzas:
```python
secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')
```
El resultado simulado en consola sería:
```text
Guess the number (1-5): 2
Wrong! Try again.
Guess the number (1-5): 1
Wrong! Try again.
Guess the number (1-5): 3
You got it!
```
> [!NOTE]
> En este ejemplo tenemos una variable `secret_number` con el valor de 3 y una suposición inicial de 0. Luego usamos la función `input` para obtener entrada del usuario, después convertimos la cadena de entrada en un entero con la función `int()` y la asignamos a la variable `guess`. Si el usuario adivina correctamente ingresando 3, se rompe el bucle `while` y se imprime el mensaje `You got it!` en la consola. De lo contrario, se imprime el mensaje `Wrong! Try again.` en la consola, y el bucle se repite, pidiendo al usuario que adivine de nuevo.

Python soporta las sentencias `break` y `continue` para alterar el flujo normal de ejecución de los bucles.

La sentencia `break` se usa para romper y salir del bucle inmediatamente si se cumple una condición:
```python
developer_names = ['Jess', 'Naomi', 'Tom']
for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)
```
El resultado sería:
```text
Jess
```

La sentencia `continue` se usa para saltarse la iteración actual y pasar directamente a la siguiente sin ejecutar las líneas de código que queden por debajo:
```python
developer_names = ['Jess', 'Naomi', 'Tom']
for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer)
```
El resultado sería:
```text
Jess
Tom
```

Tanto los bucles `for` como `while` pueden combinarse con una cláusula `else`, que se ejecuta solo cuando el bucle termina de forma natural (es decir, completó todas sus vueltas y no fue interrumpido por un `break`):
```python
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")
```
El resultado sería:
```text
'sky' has no vowels
'apple' contains the vowel 'a'
'rhythm' has no vowels
'fly' has no vowels
'orange' contains the vowel 'o'
```

---

## Rangos y su Uso en Bucles

La función `range()` se usa para generar una secuencia de enteros basándose en la sintaxis `range(start, stop, step)`:
```python
for num in range(3):
    print(num)
```
El resultado sería:
```text
0
1
2
```
> [!NOTE]
> El argumento final `stop` es obligatorio y no es inclusivo (por eso se para en el 2). Si se omite el `start`, por defecto empieza en 0 y aumenta en pasos de 1.

Puedes usar los argumentos opcionales `start` y `step` para cambiar el punto de inicio y el incremento. Por ejemplo, números pares del 2 al 10 inclusive:
```python
for num in range(2, 11, 2):
    print(num)
```
El resultado sería:
```text
2
4
6
8
10
```

Si ejecutas la función `range()` vacía sin ningún parámetro, obtendrás un `TypeError`. Además, solo acepta números enteros. Si le pasas números con decimales (floats), también lanzará un `TypeError`:
```python
for num in range(1.5, 5.5):
    print(num)

"""
Traceback (most recent call last):
  File "<main.py>", line 1, in <module>
TypeError: 'float' object cannot be interpreted as an integer
"""
```

Puedes generar secuencias en orden decreciente usando un valor negativo para el argumento `step`:
```python
for num in range(40, 0, -10):
    print(num)
```
El resultado sería:
```text
40
30
20
10
```

También se puede usar `range()` combinado con el constructor `list()` para transformarlo directamente en una lista de enteros listos para usar:
```python
numbers = list(range(2, 11, 2))
print(numbers)
```
El resultado sería:
```text
[2, 4, 6, 8, 10]
```

---

## Funciones `enumerate()` y `zip()` en Python

La función `enumerate()` te permite iterar sobre una secuencia llevando el control del índice de cada elemento de forma automática, sin contadores manuales. Devuelve pares de tuplas indexadas:
```python
languages = ['Spanish', 'English', 'Russian', 'Chinese']
for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')
```
El resultado sería:
```text
Index 0 and language Spanish
Index 1 and language English
Index 2 and language Russian
Index 3 and language Chinese
```

También puedes usarlo fuera de un bucle si lo metes dentro de un `list()` para ver sus tuplas:
```python
languages = ['Spanish', 'English', 'Russian', 'Chinese']
print(list(enumerate(languages)))
```
El resultado sería:
```text
[(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]
```
> [!NOTE]
> `enumerate()` acepta un argumento opcional llamado `start` por si quieres cambiar el índice inicial del conteo para que empiece en un número diferente de 0.

La función `zip()` se utiliza cuando necesitas iterar sobre múltiples iterables en paralelo combinándolos en tuplas compartidas:
```python
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')
```
El resultado sería:
```text
Name: Naomi
ID: 1
Name: Dario
ID: 2
Name: Jessica
ID: 3
Name: Tom
ID: 4
```

---

## Comprehensiones de Lista en Python (List Comprehension)
La comprensión de listas te permite crear una nueva lista en una sola línea combinando un bucle `for` y condiciones opcionales dentro de los propios corchetes. Esto acorta mucho tu código:

```python
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)
```
El resultado sería:
```text
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

---

## Métodos Iterables y Funciones de Orden Superior

La función `filter()` selecciona los elementos de un iterable que cumplan la condición lógica de una función que tú definas, devolviendo un iterador con los que den `True`:
```python
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words)
```
El resultado sería:
```text
['mountain', 'river', 'cloud']
```

La función `map()` aplica una función a absolutamente todos los elementos de un iterable uno a uno y te devuelve el conjunto modificado:
```python
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)
```
El resultado sería:
```text
[32.0, 50.0, 68.0, 86.0, 104.0]
```

La función `sum()` realiza la suma completa de todos los valores de un iterable de números:
```python
numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total)
```
El resultado sería:
```text
50
```

Puedes pasarle un argumento numérico opcional llamado `start` para definir un valor inicial para la suma. Se puede pasar como argumento posicional:
```python
numbers = [5, 10, 15, 20]
total = sum(numbers, 10)
print(total)
```
El resultado sería:
```text
60
```

O como argumento de palabra clave para ser más explícito en tu código:
```python
numbers = [5, 10, 15, 20]
total = sum(numbers, start=10)
print(total)
```
El resultado sería:
```text
60
```

---

## Funciones Lambda
Una función lambda es una forma compacta de crear una función de una sola línea y sin un nombre asociado (también llamadas funciones anónimas). Son muy utilizadas como argumentos directos en funciones de orden superior como `filter()` o `map()`:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
```
El resultado sería:
```text
[2, 4]
```

> [!NOTE]
> **Buenas prácticas con Lambdas**
> No las asignes a variables de forma permanente utilizando estructuras como `mi_var = lambda x: x`, ya que para funciones con nombre es mejor usar la palabra clave `def`. Mantén las expresiones cortas, simples y legibles. Si requieres de lógicas más complejas, opta siempre por funciones tradicionales.