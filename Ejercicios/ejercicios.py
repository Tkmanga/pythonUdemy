# dato = input('ingrese dato:')

# # print(dato)
# lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

# if lista.count(dato) > 0:
#     print('el dato existe:', dato)
# else:
#     print('el dato no existe', dato)


primero = input('ingrese primero:')
try:
    primeroNumero = int(primero)
except:
    primeroNumero = 'chanchito feliz'

if primeroNumero == 'chanchito feliz':
    print('no ingreso un entero')
    exit()


segundo = input('ingrese segundo:')
try:
    segundoNumero = int(segundo)
except:
    segundoNumero = 'chanchito feliz'
if segundoNumero == 'chanchito feliz':
    print('no ingreso un entero')
    exit()


simbolo = input('ingrese operacion')


if simbolo == '+':
    print('Suma:', primeroNumero+segundoNumero)
elif simbolo == '-':
    print('Resta:', primeroNumero-segundoNumero)
elif simbolo == '*':
    print('Multiplicacion:', primeroNumero*segundoNumero)
elif simbolo == '/':
    print('Division:', primeroNumero/segundoNumero)
else:
    print('no ingreso un simbolo valido')
