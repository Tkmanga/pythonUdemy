class Usuario:
    # definimos un constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print(
            'Hola mi nombre es', self.nombre, self.apellido
        )


class Admin(Usuario):
    def superSaludo(self):
        print('Hola! me llamo', self.nombre, 'y soy administrador')


usuario = Usuario('Felipe', 'Feliz')
usuario2 = Usuario('jose', 'tacacho')

# print(usuario)  # Esto nos va imprimir el valor donde esta guardado en memoria
# esto nos va imprimir el valor que buscamos
#print(usuario.nombre, usuario.apellido)

#print(usuario2.nombre, usuario2.apellido)

# usuario.saludo()
# usuario.nombre = 'LALALA'  # modificamos el nombre
# usuario.saludo()
# del usuario.nombre  # eliminamos el registro nombre
# del usuario  # eliminamos el usuario creado
# usuario2.saludo()

admin = Admin('Super', 'Feliz')
admin.saludo()
admin.superSaludo()
