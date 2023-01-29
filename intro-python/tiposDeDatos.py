

########################################################################
# Tipos de datos Python
########################################################################

palabra = 'hola mundo'
palabra2 = "hola mundo con comilla doble"

entero = 20  # integer
conDecimales = 20.2  # float
complejo = 1j  # la j es para definir numeros complejos

#print(palabra, palabra2, entero, complejo, conDecimales)
################################
# List
################################

lista = ['hola', 'mundo', 'chanchito', 'feliz']
lista2 = lista.copy()

lista.append('bebe')  # cambia la lista sin necesidad de crear una nueva
# lista.clear()  # limpia todos los elementos de la lista
# print(lista, lista2.count(2))  # el 2do cuenta cuantas veces se repite

# funcion global

# print(len(lista))  # cuantos elementos se encuentran en la lista

largoLista = len(lista)
largoLista2 = len(lista2)
# print(largoLista, largoLista2)
# consultar elementos de una lista
# print(lista[0])

# lista.pop()  # eliminar el ultimo elementos de la lista
# lista.remove('hola')  # elimina el primero que coincida
lista.reverse()  # cambia el orden de la lista
lista.sort()  # vuelve a ordenar la lista NO SE PUEDE HACER SI NO TIENEN EL MISMO TIPO

# print(lista)

################################################################
# Tuplas
################################################################

tupla = ('hola', 'mundo', 'somos', 'una', 'tupla')

# print(tupla[0])

# print(tupla.count('hola'))

# print(tupla.index('somos'))

# print(tupla.append()) #ESTO NO SE PUEDE HACER hay que convertirla a listapri

listaDeTupla = list(tupla)
listaDeTupla.append('grande')
tuplaNueva = tuple(listaDeTupla)
# print(tuplaNueva)

# Range

rango = range(6)  # le indicamos la logitud
# print(rango)

################################
# DICCIONARIO
################################

diccionario = {
    "nombre": "chanchito feliz",
    "raza": "Persa",
    "edad": 23
}
# print(diccionario)
# print(diccionario['nombre'])
# print(diccionario.get('edad'))
diccionario['nombre'] = 'Fluffy'
# print(diccionario['nombre'])
# print(len(diccionario))
diccionario['ronronea'] = True
# print(diccionario)

# diccionario.pop('ronronea')

# print(diccionario)


# diccionario.popitem()  # elimina el ultimo valor al diccionario

# print(diccionario)

# elimina especifciamente un registro del diccionario

# print(diccionario)

#copiaGatito = diccionario.copy()
copiaGatito = dict(diccionario)

del diccionario['ronronea']
# print(diccionario, copiaGatito)

Eywa = {
    "nombre": "Eywa",
    "edad": 999
}

Fluffy = {
    "nombre": "Fluffy",
    "edad": 4
}
Mamba = {
    "nombre": "Black Mamba",
    "edad": 12
}

gatitos = {
    "Eywa": Eywa,
    "Fluffy": Fluffy,
    "Mamba": Mamba
}

perritos = dict(nombre="Chanchito Feliz", edad=6)


print(perritos)

verdadero = True
falso = False

print(verdadero, falso)
