# DICCIONARIO PYTHON 
my_integer_var = 10 
print(type(my_integer_var))  # <class 'int'> 
 
my_float_var = 4.50 
print(type(my_float_var))  # <class 'float'> 
 
my_string_var = 'hello' 
print(type(my_string_var))  # <class 'str'> 
 
my_boolean_var = True 
print(type(my_boolean_var))  # <class 'bool'> 
 
my_set_var = {7, 'hello', 8.5} 
print(type(my_set_var))  # <class 'set'> 
 
my_dictionary_var = {'name': 'Alice', 'age': 25} 
print(type(my_dictionary_var))  # <class 'dict'> 
 
my_tuple_var = (7, 'hello', 8.5) 
print(type(my_tuple_var))  # <class 'tuple'> 
 
my_range_var = range(5) 
print(type(my_range_var))  # <class 'range'> 
 
my_list = [22, 'Hello world', 3.14, True] 
print(type(my_list)) # <class 'list'> 
 
my_none_var = None 
print(type(my_none_var))  # <class 'NoneType'> 


# Obtener el tipo de dato de una variable: 
my_var_1 = 'Hello world' 
my_var_2 = 21 
 
print(type(my_var_1)) # <class 'str'> 
print(type (my_var_2)) # <class 'int'> 


# Verificar si una variable coincide con un dato especifico: 
isinstance('Hello world', str) # True 
isinstance(True, bool) # True 
isinstance(42, int) # True 
isinstance('John Doe', int) # False 


# Cadenas de texto: 
# Cadenas simples: 
my_str_1 = 'Hello' 
my_str_2 = "World" 

# Cadenas multilineas: 
my_str_3 = """Multiline 
string""" 
my_str_4 = '''Another 
multiline 
string''' 


# Verificar si una cadena contiene uno o mas caracteres: 
my_str = 'Hello world' 
 
print('Hello' in my_str)  # True 
print('hey' in my_str)    # False 
print('hi' in my_str)    # False 
print('e' in my_str)  # True 
print('f' in my_str)  # False 


# Longitud de una cadena de caracteres: 
my_str = 'Hello world' 
print(len(my_str))  # 11 


# Saber caracter de la posicion n(tambien sirve la indexacion negativa): 
my_str = "Hello world" 
 
print(my_str[0])  # H 
print(my_str[6])  # w 


# Concatenacion de cadenas: 
my_str_1 = 'Hello' 
my_str_2 = "World" 
 
str_plus_str = my_str_1 + ' ' + my_str_2 
print(str_plus_str) # Hello World 


# No puedes concatenar una cadena con otro tipo de variable, sin embargo, usar la funcion str() para convertir un numero a cadena:
name = 'John Doe' 
age = 26 
 
name_and_age = name + str(age) 
print(name_and_age) # John Doe26 


# Concatenar usando +=: 
name = 'John Doe' 
age = 26 
 
name_and_age = name  # Start with the name 
name_and_age += str(age)  # Append the age as string 
 
print(name_and_age)  # John Doe26 


# Insertar variables dentro de cadenas de texto usando f o F: 
name = 'John Doe' 
age = 26 
name_and_age = f'My name is {name} and I am {age} years old' 
print(name_and_age) # My name is John Doe and I am 26 years old 
 
num1 = 5 
num2 = 10 
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15 


# Las cadenas en Python son tipos de datos inmutables, por lo que puedes reasignar una cadena diferente a una variable, 
# pero no puedes modificar una cadena directamente: 
greeting = 'hi' 
greeting = 'hello' 
print(greeting) # hello 

greeting = 'hi' 
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment 


# Corte de cadenas(no modifica la cadena original): 
my_str = 'Hello world' 
print(my_str[1:4]) # ell 

my_str = 'Hello world' 
print(my_str[:7])  # Hello w 

my_str = 'Hello world' 
print(my_str[8:])  # rld 


# Tambien hay otro parametro opcional para el corte de cadenas, el step(Sintaxis: [start:stop:step])
# que se usa para especificar el incremento entre cada índice:
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd

# Podemos poner el step en -1 y dejar los otros parametros vacios para invertir la cadena:
my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH


# Metodos mas comunes para las cadenas:
# upper(): Devuelve una nueva cadena con todos los caracteres convertidos a mayúsculas.
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

# lower(): Devuelve una nueva cadena con todos los caracteres convertidos a minúsculas.
my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world

# strip(): Devuelve una nueva cadena con los caracteres especificados de inicio y final eliminados. 
# Si no se pasa ningún argumento, elimina los espacios en blanco de inicio y final.
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"

# split(separador): Divide una cadena en un separador especificado en una lista de cadenas. 
# Si no se especifica un separador, divide por espacios en blanco.
my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']

# join(iterable): Une elementos de un iterable en una cadena con un separador.
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world

# startswith(prefijo): Devuelve un valor booleano indicando si una cadena comienza con el prefijo especificado.
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True

# endswith(sufijo): Devuelve un valor booleano indicando si una cadena termina con el sufijo especificado.
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True

# find(subcadena): Devuelve el índice de la primera ocurrencia de subcadena, o -1 si no encuentra ninguna.
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6

# count(subcadena): Devuelve el número de veces que una subcadena aparece en una cadena.
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2

# capitalize(): Devuelve una nueva cadena con el primer carácter en mayúscula y los demás caracteres en minúscula.
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world

# isupper(): Devuelve True si todas las letras en la cadena están en mayúsculas y False si no.
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False

# islower(): Devuelve True si todas las letras en la cadena están en minúsculas y False si no.
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True

# title(): Devuelve una nueva cadena con la primera letra de cada palabra en mayúscula.
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World

#swapcase(): Invierte las mayúsculas y minúsculas.
my_str = 'hello world'

swapped_my_str = my_str.swapcase()
print(swapped_my_str)  # HELLO WORLD