# Numeros y operaciones matematicas:
# Suma:
my_int_1 = 56
my_int_2 = 12

sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints) # Integer Addition: 68


# Resta:
my_int_1 = 56
my_int_2 = 12

diff_ints = my_int_1 - my_int_2
print('Integer Subtraction:', diff_ints) # Integer Subtraction: 44


# Multiplicacion:
my_int_1 = 12
my_int_2 = 4

product_ints = my_int_1 * my_int_2
print('Integer Multiplication:', product_ints) # Integer Multiplication: 48


# Division:
my_int_1 = 56
my_int_2 = 12

div_ints = my_int_1 / my_int_2
print('Division:', div_ints) # Division: 4.666666666666667


# Resto de una division 
my_int_1 = 56
my_int_2 = 12

mod_ints = my_int_1 % my_int_2
print('Integer Modulo:', mod_ints) # Integer Modulo: 8


# Division entera(evuelve el entero más grande menor o igual al resultado  )
my_int_1 = 56
my_int_2 = 12

floor_div_ints = my_int_1 // my_int_2
print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4


# Exponenciacion
my_int_1 = 56
my_int_2 = 12

exp_ints = my_int_1 ** my_int_2
print('Integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936


# float(): Devuelve un número de punto flotante construido a partir del número dado:
my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_float_1)  # 56.0
print(type(my_float_1))  # <class 'float'>


# int(): devuelve un entero construido a partir del número dado:
my_float = 12.92563
my_int = int(my_float)

print(my_int)  # 12
print(type(my_int))  # <class 'int'>


# También se pueden usar usar las mismas funciones incorporadas para convertir una cadena de texto en un flotante o entero:
my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))  # 45 <class 'int'>
print(converted_float, type(converted_float))  # 7.8 <class 'float'>


# round(): Redondea un número a un número especificado de lugares decimales. 
# Por defecto, esta función redondea al entero más cercano y devuelve un número entero sin lugares decimales:
my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3


# abs(): Devuelve el valor absoluto de un número:
num = -15

absolute_value = abs(num)
print(absolute_value) # 15


# pow(): Eleva un número a la potencia de otro o realiza exponentiación modular.
result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3


# Si sumas un entero y un flotante, el resultado se convierte automáticamente en un flotante:
my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>


# ASIGNACIONES AUMENTADAS:
# Combina una operación binaria con una asignación en un solo paso. 
# Toma una variable, le aplica una operación con otro valor y almacena el resultado nuevamente en la misma variable.

# += suma el valor de la derecha al de la variable de la izquierda.
my_var = 10
my_var += 5

print(my_var) # 15


# -= resta el operando derecho de la variable izquierda y almacena la diferencia en la variable izquierda:
count = 14
count -= 3

print(count) # 11


# *= multiplica la variable izquierda por el operando derecho y almacena el producto en la variable izquierda:
product = 65
product *= 7

print(product) # 455


# /= divide la variable izquierda por el derecho y almacena el resultado en la variable izquierda:
price = 100
price /= 4

print(price) # 25.0


# //= realiza una división de piso de la variable izquierda por el derecho y almacena el resultado en la variable izquierda:
total_pages = 23
total_pages //= 5

print(total_pages) # 4


# %= calcula el resto de la variable izquierda dividida por la derecha y lo almacena en la variable izquierda:
bits = 35
bits %= 2

print(bits) # 1


# **= eleva la variable izquierda a la potencia del derecho y almacena el resultado en la variable izquierda:
power = 2
power **= 3

print(power) # 8


# También puedes usar algunos operadores de asignación aumentada con cadenas.
# El operador de asignacion de suma:
greet = 'Hello'
greet += ' World'

print(greet) # Hello World


# El operador de asignacion de multiplicacion:
greet = 'Hello'
greet *= 3

print(greet) # HelloHelloHello