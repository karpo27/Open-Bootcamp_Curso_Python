

class Juguete:
    encendido = True

    def enciende(self):
        self.encendido = True

    def apaga(self):
        self.encendido = False

    def isEncendido(self):
        return self.encendido



class Estatica:
    numero = 1

    def incrementa():
        Estatica.numero += 1

Estatica.incrementa()
print(Estatica.numero)

class Opciones:
    ServidorSeguro = True
    Reiniciar = False

class MiClase(Juguete):
        nombre = None
        color = None

        def __init__(self, nombre):
            self.color = "Verde"
            self.nombre = nombre

p = MiClase("midinosaurio")

print(p.color)
print(p.nombre)

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")

p = Perro()
p.sonido()

g = Gato()
g.sonido()


class Motor:
    tipo = "diesel"

class Ventanas:
    cantidad = 4

class Ruedas:
    cantidad = 4

class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()

class Coche:
    motor = Motor()
    carroceria = Carroceria()

c = Coche()
print(c.motor.tipo)
print(c.carroceria.ventanas.cantidad)