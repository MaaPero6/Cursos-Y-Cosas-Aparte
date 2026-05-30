# CADENAS DE TEXTO
## Cadenas simples:
```python
my_str_1 = 'Hello' 
my_str_2 = "World" 
```

## Cadenas multilineas:
```python
my_str_3 = """Multiline 
string""" 
my_str_4 = '''Another 
multiline 
string''' 
```

## Verificar si una cadena contiene uno o mas caracteres:
```python
my_str = 'Hello world' 
 
print('Hello' in my_str)  # True 
print('hey' in my_str)    # False 
print('hi' in my_str)    # False 
print('e' in my_str)  # True 
print('f' in my_str)  # False 
```

## Longitud de una cadena de caracteres:
```python
my_str = 'Hello world' 
print(len(my_str))  # 11 
```

## Saber caracter de la posicion n(tambien sirve la indexacion negativa):
```python
my_str = "Hello world" 
 
print(my_str[0])  # H 
print(my_str[6])  # w 
```

## Concatenacion de cadenas:
```python
my_str_1 = 'Hello' 
my_str_2 = "World" 
 
str_plus_str = my_str_1 + ' ' + my_str_2 
print(str_plus_str) # Hello World 
```
### Concatenar usando +=
```python
name = 'John Doe' 
age = 26 
 
name_and_age = name  # Start with the name 
name_and_age += str(age)  # Append the age as string 
 
print(name_and_age)  # John Doe26 
```

No puedes concatenar una cadena con otro tipo de variable, sin embargo, usar la funcion str() para convertir un numero a cadena:
```python
name = 'John Doe' 
age = 26 
 
name_and_age = name + str(age) 
print(name_and_age) # John Doe26 
```

## Insertar variables dentro de cadenas de texto usando f o F: 
```python
name = 'John Doe' 
age = 26 
name_and_age = f'My name is {name} and I am {age} years old' 
print(name_and_age) # My name is John Doe and I am 26 years old 
 
num1 = 5 
num2 = 10 
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15 
```

> [!IMPORTANT]
> ### A TENER EN CUENTA: 
> Las cadenas en Python son tipos de datos inmutables, por lo que puedes reasignar una cadena diferente a una variable, pero no puedes modificar una cadena directamente: 
> ```python
> greeting = 'hi'
> greeting = 'hello'
> print(greeting) # hello
>
> greeting = 'hi'
> greeting[0] = 'H' # TypeError: 'str' object does not support item assignment
> ```

## Corte de cadenas: 
```python
my_str = 'Hello world'
print(my_str[1:4]) # ell

my_str = 'Hello world'
print(my_str[:7])  # Hello w

my_str = 'Hello world'
print(my_str[8:])  # rld
```
Tambien hay otro parametro opcional para el corte de cadenas, el step(Sintaxis: [start:stop:step]) que se usa para especificar el incremento entre cada índice:
```python
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd
```

Podemos poner el step en -1 y dejar los otros parametros vacios para invertir la cadena:
```python
my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH
```

> [!IMPORTANT] 
> ### A TENER EN CUENTA:
> El corte de cadenas no modifica la cadena original.

## Metodos mas comunes para las cadenas:

- **upper()**: Devuelve una nueva cadena con todos los caracteres convertidos a mayúsculas.
```python
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD
```

- **lower()**: Devuelve una nueva cadena con todos los caracteres convertidos a minúsculas.
```python
my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world
```

- **strip()**: Devuelve una nueva cadena con los caracteres especificados de inicio y final eliminados. Si no se pasa ningún argumento, elimina los espacios en blanco de inicio y final.
```python
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"
```

- **split(separador)**: Divide una cadena en un separador especificado en una lista de cadenas. Si no se especifica un separador, divide por espacios en blanco.
```python
my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']
```

- **join(iterable)**: Une elementos de un iterable en una cadena con un separador.
```python
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world
```

- **startswith(prefijo)**: Devuelve un valor booleano indicando si una cadena comienza con el prefijo especificado.
```python
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True
```

- **endswith(sufijo)**: Devuelve un valor booleano indicando si una cadena termina con el sufijo especificado.
```python
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True
```

- **find(subcadena)**: Devuelve el índice de la primera ocurrencia de subcadena, o -1 si no encuentra ninguna.
```python
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6
```

- **count(subcadena)**: Devuelve el número de veces que una subcadena aparece en una cadena.
```python
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2
```

- **capitalize()**: Devuelve una nueva cadena con el primer carácter en mayúscula y los demás caracteres en minúscula.
```python
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world
```

- **isupper()**: Devuelve True si todas las letras en la cadena están en mayúsculas y False si no.
```python
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False
```

- **islower()**: Devuelve True si todas las letras en la cadena están en minúsculas y False si no.
```python
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True
```

- **title()**: Devuelve una nueva cadena con la primera letra de cada palabra en mayúscula.
```python
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
```

- **swapcase()**: Invierte las mayúsculas y minúsculas.
```python
my_str = 'hello world'

swapped_my_str = my_str.swapcase()
print(swapped_my_str)  # HELLO WORLD
```
