def miFuncion():
    print('Mi primera funcion!')

# miFuncion()


def imprimeDato(*nombre):
    print('El nombre completo es: ', nombre)

#imprimeDato('chanchito', 'feliz', 'rosado')


def nombreCompleto(apellido, nombre):
    print(nombre, apellido)


def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])


#nombreCompleto2(nombre='chanchito', apellido='feliz')


def miFuncion2(argumento='chanchito'):
    print(argumento)


# miFuncion2('batman')
# miFuncion2()

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + ' ' + el
    return i


nombres = concatenaNombres(['jose', 'dario', 'tacacho'])
print(nombres)

# recursividad


def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i-1)


recursion(10)

# cuando sirve la recursividad? trabajar sobre coleccion de datos o intentar conectarnos a un provider
