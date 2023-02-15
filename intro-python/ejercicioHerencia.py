class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola soy un', self.tipo, ' y mi saludo es el', self.onomatopeya)


class Gato(Animal):
    tipo = 'Gato'

    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('hola soy un gato extendido!')


class Perro(Animal):
    tipo = 'Perro'

    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('Hola soy un Perro extendido!')


class Canario(Animal):
    tipo = 'Canario'

    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('Hola soy un canario extendido!')


gato = Gato('Rockyta', 'maullido')
gato.saludo()
perro = Perro('Bandida', 'ladrido')
perro.saludo()
canario = Canario('piolin', 'cantar')
canario.saludo()
