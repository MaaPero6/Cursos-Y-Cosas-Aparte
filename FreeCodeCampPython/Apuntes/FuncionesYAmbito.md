# FUNCIONES Y AMBITO

## ¿Cómo funcionan las funciones en Python?
Las funciones son piezas reutilizables de código que se ejecutan cuando las llamas. Python incluye funciones integradas que facilitan comenzar, como `print()`.

## Funciones integradas útiles

- **`input()`**: Permite pedir la entrada del usuario.
```python
name = input('What is your name?') # El usuario escribe "Kolade" y pulsa Enter
print('Hello', name) # Output: Hello Kolade
```

- **`int()`**: Convierte un número, booleano y una cadena numérica en un entero.
```python
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0
```

## Funciones personalizadas
Para definir una función propia se usa la palabra clave `def`, seguida del nombre de la función, paréntesis y dos puntos. El código que ejecuta la función se llama **cuerpo de la función**:
```python
def hello():
    print('Hello World')
```

Para ejecutarla, hay que llamarla con su nombre seguido de paréntesis:
```python
hello() # Hello World
```

> [!WARNING]
> Como siempre, la indentación es crucial. El cuerpo de la función debe estar indentado correctamente o Python lanzará un error.

## Parámetros y argumentos
Las funciones pueden recibir valores a través de **parámetros**, que son variables de marcador de posición definidas entre los paréntesis:
```python
def calculate_sum(a, b):
    print(a + b)
```

- **Parámetros**: las variables `a` y `b` en la definición de la función.
- **Argumentos**: los valores concretos que se pasan al llamar a la función.

```python
calculate_sum(3, 1) # 4
```

> [!NOTE]
> Si llamas a la función sin el número correcto de argumentos, obtendrás un `TypeError`:
> ```python
> calculate_sum()
> # TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'
> ```

## La palabra clave `return`
Las funciones usan `return` para salir y devolver un valor. Si no se usa explícitamente, Python devuelve `None` por defecto:
```python
def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None
```

Para que la función devuelva el resultado correctamente, hay que usar `return`:
```python
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum) # 4
```

## ¿Qué es el ámbito (scope) en Python y cómo funciona?
El ámbito determina el punto en el que puedes acceder a una variable. Controla la vida útil de una variable y cómo se resuelve en diferentes partes del código.

Para determinar el ámbito correctamente, Python sigue la **regla LEGB**:
- **L - Local**: Variables definidas en funciones o clases.
- **E - Envolvente (Enclosing)**: Variables definidas en funciones anidadas o de cierre.
- **G - Global**: Variables definidas al nivel superior del módulo o archivo.
- **B - Incorporado (Built-in)**: Nombres reservados de Python (funciones, módulos, palabras clave...).

### Ámbito local
Una variable declarada dentro de una función solo puede ser accedida dentro de esa función:
```python
def my_func():
    my_var = 10 # Localmente en my_func
    print(my_var)

my_func() # 10
print(my_var) # NameError: name 'my_var' is not defined
```

### Ámbito envolvente
Una función anidada puede acceder a las variables de la función en la que está anidada, pero no al revés:
```python
def outer_func():
    msg = 'Hello there!'

    def inner_func():
        print(msg) # Accede a msg de outer_func

    inner_func()

outer_func() # Hello there!
```

Si se necesita que la función externa acceda a una variable modificada dentro de la función interna, se usa la palabra clave `nonlocal`:
```python
def outer_func():
    msg = 'Hello there!'
    res = ""  # Se declara res en el ámbito envolvente

    def inner_func():
        nonlocal res  # Permite modificar la variable del ámbito envolvente
        res = 'How are you?'
        print(msg)

    inner_func()
    print(res)

outer_func()
# Hello there!
# How are you?
```

### Ámbito global
Las variables declaradas fuera de cualquier función o clase son globales y se pueden acceder desde cualquier parte del programa:
```python
my_var = 100

def show_var():
    print(my_var)

show_var() # 100
print(my_var) # 100
```

Si se quiere modificar una variable global desde dentro de una función, se usa la palabra clave `global`:
```python
my_var = 10

def change_var():
    global my_var  # Permite modificar la variable global
    my_var = 20

change_var()
print(my_var) # 20
```

### Ámbito incorporado (Built-in)
Se refiere a todas las funciones, módulos y palabras clave integradas de Python. Están disponibles en cualquier parte del programa:
```python
print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False
```