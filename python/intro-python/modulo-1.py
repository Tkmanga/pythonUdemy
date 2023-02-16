
# import modulos as primerModulo  # traemos el modulo y renombramos para usarlo
# de esta forma traemos solo lo que necesitamos
from modulos import saludo, mascotas
from camelcase import CamelCase

c = CamelCase()
s = 'esta oracion necesita CamelCase'
camelcased = c.hump(s)
print(camelcased)

# print(mascotas)
# saludo('nicolas')

# pip uninstall nombre del modulo
