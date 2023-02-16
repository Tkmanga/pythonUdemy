# multiplicar dos números sin usar el símbolo de multiplicación
# mi respuesta
import math as M
""""
primerNumero = int(input('ingrese el primer numero: '))
segundoNumero = int(input('ingrese segundo numero: '))
resultado = 0

while segundoNumero > 0:
    segundoNumero = segundoNumero-1
    print('valor ahora: ', resultado)
    resultado += primerNumero

print('el resultado es: ', resultado)

"""
# solucion profe
""""
a = 4
b = 8
resultado = 0

for x in range(a):
    resultado += b

print(resultado)
"""


# ingresar nombre y apellido e imprimirlo al reves

# mi respuesta
""""
nombre = input('ingrese su nombre: ')

apellido = input('ingrese su apellido: ')

newNombre = ''
newApellido = ''

largoNombre = len(nombre) - 1
largoApellido = len(apellido) - 1
for x in range(len(nombre)):
    newNombre += nombre[largoNombre]
    largoNombre = largoNombre-1

print('nombre:', newNombre)
for x in range(len(apellido)):
    newApellido += apellido[largoApellido]
    largoApellido = largoApellido-1

print('Apellido:', newApellido)
"""

# solucion profe
"""
nombre = 'Nicolas'
apellido = 'Feliz'

concatenacion = nombre + ' ' + apellido

print(concatenacion[::-1])
"""

# escribir una función que encuentre el elemento menor de una lista
# Mi respuesta
"""
listaNumeros = [1, 2, 4, -10, -11]
menor = 0  # no le puedo poner 0 ya que puede que ese sea el menor numero de una lista x
for x in listaNumeros:
    if (x < menor):
        menor = x
print("El menor numero es ", menor)
"""
# solucion profe
"""
listaNumeros = [1, 2, 4, -10, -11]
menor = 'init' 
for x in listaNumeros:
    if (menor == 'init'):
        menor = x
    else:
        menor = x if x < menor else menor
print("El menor numero es ", menor)
"""
# escribir una función que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3
"""
radio = int(input('Ingrese un radio para calcular: '))

print(4/3 * M.pi * radio ** 3)
"""

"""
def calculaVolumen(r):
    return 4 / 3 * 3.14 * r ** 3


resultado = calculaVolumen(6)
print(resultado)
"""
# escribir una función que indique si el usuario es mayor de edad

# mi respuesta, saque el tema de crear objeto usuario!

"""
def esMayor(edad):
    return edad >= 18


print(esMayor(18))

"""
# solucion profe
"""
def esMayor(usuario):
    return usuario.edad > 17


class Usuario:
    def __init__(self, edad):
        self.edad = edad


usuario = Usuario(15)
usuario2 = Usuario(21)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)

print(resultado1, resultado2)

"""
# escribir una función que indique si un número es par o impar
# mi resultado
"""
def esPar(numero):
    return numero % 2 == 0


resultado1 = esPar(2)
print(resultado1)
resultado2 = esPar(3)
print(resultado2)
"""

# solucion profe


"""
def esPar(n):
    return n % 2 == 0


resultado = esPar(11)
"""

# escribir una función que indique cuantas vocales tiene una palabra


# mi respuesta, notamos que si nos llega en mayusucula no va contar como vocal, LO SOLUCIONAMOS HACIENDO x.lower() en la primera iteracion
"""
vocales = ['a', 'e', 'i', 'o', 'u']


def cantidadVocales(p):

    contador = 0
    for x in p:
        for y in vocales:
            if x == y:
                contador += 1
    return contador


palabra = input('ingrese una palabra: ')
resultado = cantidadVocales(palabra)

print(resultado)
"""
# solucion profe
"""
palabra = 'ChAnchitoFeliz'
vocales = 0
for x in palabra:
    y = x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0
"""

# escribir una aplicación que reciba una cantidad infinita de números hasta
# decir basta, luego que devuelva la suma de los números ingresados
"""
palabraClave = '' #hay que tener en consideracion que el usuario puede escribir algo mas que basta o carateres alfanumericos 
contadorInfinito = 0

while palabraClave != 'basta':
    palabraClave = input('ingrese numero o basta para terminar: ')
    if palabraClave == 'basta':
        continue

    contadorInfinito = contadorInfinito + int(palabraClave)
print(contadorInfinito)
"""

"""
palabraClave = ''  # Agregamos la solucion
contadorInfinito = 0

while palabraClave != 'basta':
    palabraClave = input('ingrese numero o basta para terminar: ')
    if palabraClave == 'basta':
        continue
    else:
        try:
            valor = int(palabraClave)
        except:
            print('Dato invalido')
            exit()

    contadorInfinito = contadorInfinito + valor
print(contadorInfinito)
"""
# solucion profe
"""
lista = []
print('Ingrese números y para salir escriba "basta"')
while True:
    valor = input('Ingrese valor: ')
    if valor == 'basta':
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('Dato inválido')
            exit()
resultado = 0
for x in lista:
    resultado += x

print(resultado)
"""
# escribir una función que reciba nombre y apellido y los vaya agregando a
# un archivo


def agregarRegistro(nombre, apellido):
    c = open('registro.txt', 'a')
    c.write("\n nombre:"+' ' + nombre + ' apellido: ' + apellido)
    c.close()


agregarRegistro('jose', 'tacacho')
