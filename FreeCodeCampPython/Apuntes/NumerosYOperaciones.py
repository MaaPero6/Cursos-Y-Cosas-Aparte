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





# Si sumas un entero y un flotante, el resultado se convierte automáticamente en un flotante:
my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>