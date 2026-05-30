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

> [!NOTE]
> Las cadenas en Python son tipos de datos inmutables, por lo que puedes reasignar una cadena diferente a una variable, pero no puedes modificar una cadena directamente: 
> ```python
> greeting = 'hi'
> greeting = 'hello'
> print(greeting) # hello
>
> greeting = 'hi'
> greeting[0] = 'H' # TypeError: 'str' object does not support item assignment
> ```

