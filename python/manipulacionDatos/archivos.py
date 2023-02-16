# 1ro cual archivo / 2do permisos para el archivo
import os
#c = open('chanchito.txt', 'a')
# r leer
# a modificar sin borrar lo anterior
# w si queremos modificar todo
# x con esto podemos crear archivos

# read() si trabajamos con un archivos pequenios unicamente para mas grandes conviene leer linea a linea readline()
# print(c.readline())  # cada vez que lo ejecutemos nos va devolver la siguiente linea

# for x in c:
#    print(x)

#c.write("\n agregamos una nueva lina")

# c.close()

if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
else:
    print("el archivo no existe")

# os.rmdir('carpeta a eliminar')
