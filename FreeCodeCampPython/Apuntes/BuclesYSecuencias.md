# Bucles y secuencias
## ¿Qué son las listas y cómo funcionan?
El tipo de dato lista es una secuencia ordenada de elementos que pueden estar compuestos por cadenas, números o incluso otras listas. Las listas son mutables y usan indexación basada en cero, lo que significa que el primer elemento de la lista está en el índice cero.

Aquí está la sintaxis básica para una lista:
```python
cities = ['Los Angeles', 'London', 'Tokyo']
```

Para acceder a un elemento de la lista cities, puedes referenciar su número de índice en la secuencia. Ejemplo de cómo acceder al primer elemento de la lista cities:
```python
cities = ['Los Angeles', 'London', 'Tokyo']
cities[0] # 'Los Angeles'
```

El indexado negativo se usa para acceder a elementos comenzando desde el final de la lista en lugar del principio en el índice 0. Para acceder al último elemento de cualquier lista, puedes usar -1 así:
```python
cities = ['Los Angeles', 'London', 'Tokyo']
cities[-1] # 'Tokyo'
```

Otra forma de crear una lista es usar la estructura `list()`. La estructura `list()` se usa para convertir un iterable en una lista así:
```python
developer = 'Jessica'
list(developer) # ['J', 'e', 's', 's', 'i', 'c', 'a']
```

Para obtener el número total de elementos en una lista, puedes usar la función `len()` así:
```python
numbers = [1, 2, 3, 4, 5]
len(numbers) # 5
```

Si quieres actualizar un valor en un índice particular, puedes hacer algo así:
```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']
```

Dado que las listas son mutables, puedes actualizar cualquier elemento en la lista siempre que pases un número de índice válido. Si pasas un índice (ya sea positivo o negativo) que está fuera de los límites de la lista, recibirás un `IndexError`:
```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[10] = 'JavaScript'

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list assignment index out of range
"""
```

Si quieres eliminar un elemento de una lista puedes usar la palabra clave `del` así:
```python
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']
```

A veces es útil verificar si un elemento está dentro de la lista. Para hacer eso, puedes usar la palabra clave `in` así:
```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False
```

A veces es común tener listas anidadas dentro de otras listas así:
```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
```

En este ejemplo, tenemos una lista anidada que contiene tres lenguajes de programación populares. Para acceder a la lista anidada, necesitarás acceder a ella usando el índice 2 ya que las listas están indexadas desde cero:
```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2] # ['Python', 'Rust', 'C++']
```

Luego, para acceder al segundo idioma de esa lista anidada, necesitarás acceder a él usando el índice `1` así:
```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2][1] # 'Rust'
```

Otra técnica común utilizada con listas es desempaquetar valores.

Desempaquetar valores de una lista es una técnica usada para asignar valores de una lista a nuevas variables. Aquí tienes un ejemplo de cómo desempaquetar una lista `developer` en nuevas variables llamadas `name`, `age` y `job`.
```python
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'
```

Aquí, `name` tiene el valor 'Alice', `age` tiene el valor 34, y `job` tiene el valor 'Rust Developer'.

Si necesitas recolectar cualquier elemento restante de una lista, puedes usar el operador asterisco (`*`) así:
```python
developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']
```



En este ejemplo, `name` seguirá teniendo el valor `'Alice'`, y `rest` es una lista de dos elementos: el número `34` y la cadena `'Rust Developer'`.

Si la cantidad de variables en el lado izquierdo del operador de asignación no coincide con la cantidad total de elementos en la lista, entonces recibirás un `ValueError`:
```python
eveloper = ['Alice', 34, 'Rust Developer']
name, age, job, city = developer

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: not enough values to unpack (expected 4, got 3)
"""
```

El último concepto que veremos es el operador slice (`:`). Similar a las cadenas, puedes acceder a porciones de una lista usando el operador slice de esta manera:
```python
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
desserts[1:4] # ['Cookies', 'Ice Cream', 'Pie']
```

En este ejemplo, el índice de inicio es `1` ya que apunta al segundo elemento en la lista. Luego usamos el operador slice seguido de un índice final de `4`, que incluye todo hasta (pero sin incluir) el elemento en ese índice.

Otra cosa que puedes hacer con el operador de corte `:` es especificar un intervalo de paso que determina cuánto incrementar entre los índices. Supongamos que tienes una lista de números como esta:
```python
numbers = [1, 2, 3, 4, 5, 6]
```

Si quieres extraer una lista de solo números pares, puedes usar el operador de slicing así:
```python
numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2] # [2, 4, 6]
```

El primer número par está en el índice `1`, así que ese será el índice de inicio. Como queremos recorrer hasta el final de la lista, omitimos el índice de fin. Por último, especificamos `2` para el intervalo de paso opcional, de modo que solo incrementará en 2 en lugar del valor predeterminado `1`.

## ¿Cuáles son algunos métodos comunes utilizados para listas?
El primer método que veremos es el método `append()`. Este se usa para agregar un elemento al final de la lista. Aquí tienes un ejemplo de cómo usar el método `append()` para agregar el número 6 a la lista de números:
```python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]
```

Si quieres agregar una lista al final de otra, también puedes usar el método append() así:
```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]
```

Observa cómo toda la lista `even_numbers` está anidada dentro de la lista `numbers`.

Pero si quieres agregar todos los números individuales de la lista `even_numbers` al final de la lista `numbers`, entonces puedes usar el método `extend()`.

El método `extend()` es similar al método `append()`, pero con `extend()` puedes agregar múltiples elementos de una lista a otra. Aquí tienes un ejemplo de cómo agregar los números 6, 8 y 10 de una lista al final de la lista `numbers`:
```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]
```

Como puedes ver, la lista anidada ha desaparecido y ahora es solo una lista de números.

Para insertar un elemento en un índice específico de una lista, puedes usar el método `insert()`. Este método acepta dos argumentos: el índice donde deseas insertar el nuevo elemento y el elemento que quieres insertar.

Aquí hay un ejemplo de cómo usar el método `insert()`:
```python
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)

print(numbers) # [1, 2, 2.5, 3, 4, 5]
```

El siguiente código insertará el número 2.5 en el índice 2 de la lista numbers.

Si quieres eliminar un elemento de una lista, puedes usar el método `remove()`. El método `remove()` toma el valor del elemento a eliminar como argumento:
```python
numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)

print(numbers) # [10, 20, 30, 40, 50]
```

Es importante notar que este método solo eliminará la primera ocurrencia de un ítem. No todas ellas:
```python
numbers = [10, 20, 30, 40, 50, 50, 50]
numbers.remove(50)

print(numbers) # [10, 20, 30, 40, 50, 50]
```

Para eliminar un elemento en un índice específico de la lista, puedes usar el método `pop()` así:
```python
numbers = [1, 2, 3, 4, 5]
numbers.pop(1) # The number 2 is returned

print(numbers)
```

Si no especifica un elemento para el método `pop()`, entonces se elimina el último elemento.
```python
numbers = [1, 2, 3, 4, 5]
numbers.pop() # The number 5 is returned
```

Si necesitas vaciar la lista, entonces puedes usar el método `clear()` así:
```python
numbers = [1, 2, 3, 4, 5]
numbers.clear()

print(numbers) # []
```

El siguiente método que vamos a revisar es el método `sort()`. Este método se usa para ordenar los elementos en el lugar. Aquí tienes un ejemplo de cómo ordenar una lista aleatoria de números en el lugar:
```pythom
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers) # [1, 2, 19, 35, 41, 67]
```

A diferencia del método `sort()`, existe la función `sorted()` que funciona para cualquier iterable y devuelve una nueva lista ordenada en lugar de modificar la lista original. Por ejemplo:
```python
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]
```

> [!IMPORTANT]
> Tanto el método `sort()` como la función `sorted()` aceptan parámetros opcionales `key` y `reverse`. Aprenderás más sobre estos parámetros opcionales en una lección futura cuando estudies las tuplas. También aprenderás más sobre otras funciones integradas como `sorted()` en lecciones futuras.

El siguiente método que vamos a ver es el método `reverse()`. Este método invertirá una lista de elementos en el lugar así:
```python
numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()

print(numbers) # [1, 2, 3, 4, 5, 6]
```

El último método que veremos es el método `index`. Este se usa para encontrar el primer índice donde se puede encontrar un elemento en una lista. Aquí tienes un ejemplo de cómo usar el método index para encontrar el lenguaje 'Java' en una lista programming_languages:
```python
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java') # 1
```
Si no se puede encontrar el elemento, entonces Python lanza un `ValueError`:
```python
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('JavaScript')

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'JavaScript' is not in list
"""
```

## ¿Qué son las tuplas y cómo funcionan?
Una tupla es un tipo de dato de Python usado para crear una secuencia ordenada de valores. Las tuplas pueden contener un conjunto mixto de tipos de datos como este:
```python
developer = ('Alice', 34, 'Rust Developer')
```

Las tuplas son similares a las listas, pero mientras las listas son un tipo de dato mutable, las tuplas son inmutables. Esto significa que los elementos en una tupla no pueden cambiarse una vez que se ha creado.

Si intenta actualizar uno de los elementos en la tupla, obtendrá un `TypeError`:
```python
programming_languages = ('Python', 'Java', 'C++', 'Rust')
programming_languages[0] = 'JavaScript'

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'tuple' object does not support item assignment
"""
```

Para acceder a un elemento de una tupla, puedes usar la notación con corchetes y el número de índice:
```python
developer = ('Alice', 34, 'Rust Developer')
developer[1] # 34
```

Si necesitas acceder a elementos comenzando desde el final de una tupla, entonces puedes usar indexación negativa. Aquí tienes un ejemplo de cómo usar un índice negativo para acceder al penúltimo elemento en una tupla:
```python
numbers = (1, 2, 3, 4, 5)
numbers[-2] # 4
```

Si intentas pasar un número de índice que excede o es igual a la longitud de la tupla, recibirás un `IndexError` como este:
```python
numbers = (1, 2, 3, 4, 5)
numbers[7]

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list index out of range
"""
```

Otra forma de crear una tupla es usando el constructor `tuple()` así:
```python
developer = 'Jessica'
tuple(developer) # ('J', 'e', 's', 's', 'i', 'c', 'a')
```

Para la estructura `tuple()`, puedes pasar diferentes iterables como cadenas, listas e incluso otras tuplas.

Para verificar si un elemento está en una tupla, puedes usar la palabra clave `in` así:
```python
programming_languages = ('Python', 'Java', 'C++', 'Rust')
'Rust' in programming_languages # True
'JavaScript' in programming_languages # False
```

También puedes desempaquetar elementos de una tupla tal como lo hiciste con las listas[cite: 2]:

```python
developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer

print(name)  # 'Alice'
print(age)   # 34
print(job)   # 'Rust Developer'
```

En este ejemplo, `name` tiene el valor `'Alice'`, `age` tiene el valor `34` y `job` tiene el valor `'Rust Developer'`.

Si necesitas recoger cualquier elemento restante de una tupla, puedes usar el operador asterisco (`*`) de esta manera:

```python
developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer

print(name)  # 'Alice'
print(rest)  # [34, 'Rust Developer']
```

Aquí, `name` tiene el valor `'Alice'`, y `rest` es una lista compuesta por el número `34` y la cadena `'Rust Developer'`.    

Al igual que con una lista, puedes usar el operador de corte en una tupla para extraer una porción de ella. Aquí tienes un ejemplo de cómo extraer los elementos `'pie'` y `'cookies'` en una tupla separada:
```python
desserts = ('cake', 'pie', 'cookies', 'ice cream')
desserts[1:3]  # ('pie', 'cookies')
```

Recuerda que el primer número representa el índice inicial para la extracción mientras que el segundo número representa el índice final. Pero ten en cuenta que el elemento en el índice final no está incluido en la tupla extraída.

Si necesitas eliminar un elemento de una tupla, eso no es posible porque las tuplas son inmutables. Así que este ejemplo producirá un error:
```python
developer = ('Jane Doe', 23, 'Python Developer')
del developer[1]
"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: "tuple" object doesn't support item deletion
"""
```

## ¿Cuáles son algunos métodos comunes para las tuplas?
El primer método es `count()`. Se usa para determinar cuántas veces aparece un elemento en una tupla. 
Ejemplo de cómo verificar cuántas veces aparece la cadena Rust en una tupla llamada `programming_languages`:
```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('Rust')  # 2
```

Como Rust aparece dos veces en la tupla, el método `count()` devuelve el número 2. Si el elemento especificado en la función `count()` no está presente en la tupla, entonces el valor devuelto es 0:
```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('JavaScript')  # 0
```

Si no se pasan argumentos a la función `count()`, entonces Python genera un `TypeError`:
```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count()
"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: tuple.count() takes exactly one argument (0 given)
"""
```

Otro método es `index()`. Este método se usa para encontrar el índice donde un elemento particular está presente en una tupla. Ejemplo de cómo usar el método `index()` para encontrar el índice de la cadena `Java`:
```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('Java')  # 1
```

Si no se puede encontrar el ítem especificado, entonces Python genera un `ValueError`:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('JavaScript')
"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: tuple.index(x): x not in tuple
"""
```

Otra cosa que puedes hacer con el método `index()` es pasar argumentos opcionales de índice de inicio y fin. 
Ejemplo de cómo pasar un índice de inicio opcional:
```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3)  # 5
```

En este ejemplo, estamos especificando dónde comenzar a buscar la cadena Python. Al pasar el número 3 como segundo argumento a la función `index()`, estamos indicando que la búsqueda comience en el índice 3. Dado que Python aparece dos veces en la tupla, la función `index()` devolverá el índice 5 en lugar del índice 2 debido al uso del argumento opcional de índice de inicio.

También puedes pasar un índice de parada opcional. Aquí tienes un ejemplo modificado de cómo especificar un índice de inicio y de parada:
```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
programming_languages.index('Python', 2, 5)  # 2
```

Ahora el resultado es el índice 2 porque estamos comenzando la búsqueda en el índice 2 y buscando hasta, pero sin incluir, el índice 5.

Otra función comúnmente usada con tuplas es la función `sorted()`, que se puede usar en cualquier iterable, incluidas las tuplas.
Ejemplo de cómo crear una nueva lista de números usando la función `sorted()`:
```python
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers)  # [2, 3, 7, 13, 18, 45, 67, 78]
```

La función `sorted()` siempre creará una nueva lista con los valores ordenados. Esto difiere del método `sort()`, que ordena los elementos de una lista en el lugar y no devuelve una nueva lista.

Si necesitas personalizar el comportamiento de ordenamiento para un iterable, puedes usar los argumentos opcionales `reverse` y `key`. Aquí tienes un ejemplo de cómo usar el argumento `key` para ordenar elementos en una tupla por longitud:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
sorted(programming_languages, key=len)
```

El resultado seria:
```text
['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']
```

Si quieres crear una nueva lista de valores en orden inverso, entonces puedes usar el argumento `reverse` así:
```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, reverse=True))
```

El resultado seria:
```text
['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']
```
>[!NOTE]
> Las tuplas son un tipo de dato común en Python. Entender cómo trabajar con ellas, junto con algunos métodos y funciones útiles, te ayudará a escribir código más eficiente.


## ¿Cómo funcionan los bucles?
El primer bucle que veremos es el bucle `for`.
```python
programming_languages = ['Rust', 'Java', 'Python', 'C++']
for language in programming_languages:
    print(language)
```

El resultado seria:
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

También puedes usar un bucle `for` para iterar a través de otros iterables como una cadena. Aquí tienes un ejemplo de cómo usar un bucle `for` para recorrer la cadena `code` e imprimir cada carácter:

```python
for char in 'code':
    print(char)
```
El resultado seria:
```text
c
o
d
e
```

Los bucles `for`pueden anidarse, aqui un ejemplo:
```python
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)
```

El resultado seria:
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

"""
Ejemplo de ejecución en consola:
Guess the number (1-5): 2
Wrong! Try again.
Guess the number (1-5): 1
Wrong! Try again.
Guess the number (1-5): 3
You got it!
"""
```
> [!NOTE]
> En este ejemplo tenemos una variable `secret_number` con el valor de 3 y una suposición inicial de 0. Luego usamos la función `input` para obtener entrada del usuario, después convertimos la cadena de entrada en un entero con la función `int()` y la asignamos a la variable `guess`. Si el usuario adivina correctamente ingresando 3, se rompe el bucle `while` y se imprime el mensaje `You got it!` en la consola. De lo contrario, se imprime el mensaje `Wrong! Try again.` en la consola, y el bucle se repite, pidiendo al usuario que adivine de nuevo.

Python soporta las sentencias `break` y `continue`.

La sentencia `break` se usa para detener la ejecución de un bucle. Aquí tienes un ejemplo de cómo usar la sentencia `break` para una lista de `developer_names`:
```python
developer_names = ['Jess', 'Naomi', 'Tom']
for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)
```

El resultado seria:
```text
Jess
```

La sentencia `continue` se usa para saltar la iteración actual de un bucle y pasar a la siguiente iteración. Modifiquemos el ejemplo de antes para usar la sentencia `continue` en lugar de `break`:

```python
developer_names = ['Jess', 'Naomi', 'Tom']
for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer)
```

El resultado seria:
```text
Jess
Tom
```

Tanto los bucles `for` como `while` pueden combinarse con una cláusula `else`, que se ejecuta solo cuando el bucle no es terminado por una instrucción `break`. Aquí tienes un ejemplo de cómo usar múltiples bucles `for`:

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
El resultado seria:
```text
'sky' has no vowels
'apple' contains the vowel 'a'
'rhythm' has no vowels
'fly' has no vowels
'orange' contains the vowel 'o'
```

En este ejemplo tenemos una lista de palabras aleatorias, y se usa un `for` para iterar por cada palabra. Dentro del `for` externo, tenemos otro `for` para iterar por cada letra de cada palabra. Si la versión en minúscula de la letra es una vocal, imprimimos la palabra seguida de las vocales que contiene, luego salimos del `for` interno. Si la palabra no contiene vocales, entonces el bloque `else` del bucle interno se activa e imprimimos un mensaje que lo indica.


## ¿Qué son los rangos y cómo puedes utilizarlos en un bucle?
La función `range()` se usa para generar una secuencia de enteros. Aquí está la sintaxis básica para la función `range()`:
```python
range(start, stop, step)
```

El argumento obligatorio `stop` es un entero que representa el punto final para la secuencia de números que se está generando. Aquí tienes un ejemplo de cómo usar la función `range()`:
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
> El código anterior genera una secuencia de números entre 0 y 2. El entero 3 no está incluido porque el argumento `stop` no es inclusivo. Si no se especifica un argumento `start`, entonces el valor predeterminado es 0.

De lo contrario, puedes usar el argumento opcional `start` para comenzar la secuencia de enteros en un número entero distinto de 0. Aquí tienes un ejemplo de cómo generar una secuencia de enteros entre 1 y 4:
```python
for num in range(1, 5):
    print(num)
```

El resultado sería:
```text
1
2
3
4
```

Por defecto, la secuencia de enteros incrementará en 1. Pero si quieres cambiar ese valor predeterminado, puedes usar el argumento opcional `step`. Aquí tienes un ejemplo de cómo generar una secuencia de enteros pares entre 2 y 10:
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

Como se mencionó antes, solo hay un argumento obligatorio para la función `range()`. Si no proporcionas ningún argumento a `range()`, entonces obtendrás un `TypeError`:
```python
for num in range():
    print(num)

"""
Traceback (most recent call last):
  File "<main.py>", line 1, in <module>
TypeError: range expected at least 1 argument, got 0
"""
```

Es importante notar que la función `range()` solo acepta enteros como argumentos, no floats. Recuerda que los floats son números con puntos decimales como 3.4. Si intentas pasar floats como argumentos, obtendrás un `TypeError`:
```python
for num in range(1.5, 5.5):
    print(num)

"""
Traceback (most recent call last):
  File "<main.py>", line 1, in <module>
TypeError: 'float' object cannot be interpreted as an integer
"""
```

Si quieres generar una secuencia de enteros en orden decreciente, entonces puedes usar un entero negativo para el argumento `step`, así:
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

Otra cosa que puedes hacer con la función `range()` es crear una lista de enteros usándola con la estructura `list()`. La estructura `list()` se usa para convertir un iterable en una lista[cite: 2]. Aquí tienes un ejemplo de cómo generar una lista de enteros pares entre 2 y 10:
```python
numbers = list(range(2, 11, 2))
print(numbers)
```

El resultado sería:
```text
[2, 4, 6, 8, 10]
```

La función `range()` es una forma muy útil de generar una secuencia de enteros en Python.


## ¿Cuáles son las funciones Enumerate y Zip y cómo funcionan?
La función `enumerate()` lleva un seguimiento del índice de un iterable y devuelve un objeto `enumerate`.

Si pasamos la lista `languages` a la función `enumerate()` y convertimos su valor devuelto en una lista con la función `list()`, se ve así:

```python
languages = ['Spanish', 'English', 'Russian', 'Chinese']
list(enumerate(languages))

# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]
```
> [!NOTE]
> Cada entrada en el objeto `enumerate` (ahora una lista) es una tupla que contiene un conteo, seguido de un valor del iterable pasado a la función `enumerate()`.

Ahora, vamos a refactorizar el ejemplo de antes para usar la función `enumerate()`:
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
> [!NOTE]
> Desempaquetamos el `count` y el `value` de cada tupla en el objeto `enumerate` en variables llamadas `index` y `language`, respectivamente. Finalmente, ambas variables se usan en un f-string que se imprime en la consola en cada iteración del ciclo. Esto elimina la necesidad de crear y actualizar manualmente una variable `index`.

La función `enumerate()` también acepta un argumento opcional `start` que especifica el valor inicial para el conteo. Si este argumento es omitido, entonces el conteo comenzará en 0. Aquí hay un ejemplo de cómo usar el argumento opcional `start`:

```python
languages = ['Spanish', 'English', 'Russian', 'Chinese']
for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}')
```

El resultado sería:
```text
Index 1 and language Spanish
Index 2 and language English
Index 3 and language Russian
Index 4 and language Chinese
```

Hasta ahora solo hemos estado iterando sobre una lista. Pero, ¿qué pasa si necesitas iterar sobre múltiples iterables en paralelo? Bueno, puedes usar la función `zip()` para eso, que combina listas en pares de elementos y devuelve un iterador de tuplas.

Si pasamos una lista de `developers` y `ids` a la función `zip()` y convertimos su valor devuelto en una lista con la función `list()`, así es como se ve:

```python
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]
list(zip(developers, ids))

# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]
```

Y aquí un ejemplo de cómo usar la función `zip()` con un ciclo `for` para iterar sobre `developers` e `ids`:

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
> [!NOTE]
> En este ejemplo, `zip()` combina las dos listas en pares de elementos y devuelve un iterador de tuplas. El ciclo `for` luego desempaqueta cada tupla en `name` e `id`[cite: 2]. Finalmente, en cada instrucción `print`, estamos imprimiendo cada `name` e `id` de las listas `ids` y `developers` respectivamente.

Las funciones `enumerate()` y `zip()` son muy poderosas, y cuando se combinan con bucles, pueden hacer que tu código sea mucho más conciso.