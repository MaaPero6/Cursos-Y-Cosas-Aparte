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


# Corte de cadenas: 
my_str = 'Hello world' 
print(my_str[1:4]) # ell 

my_str = 'Hello world' 
print(my_str[:7])  # Hello w 

my_str = 'Hello world' 
print(my_str[8:])  # rld 

