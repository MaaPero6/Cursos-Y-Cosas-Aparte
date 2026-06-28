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
