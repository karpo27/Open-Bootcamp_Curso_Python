# En este segundo ejercicio, tendréis que crear un archivo py
# y dentro crearéis una clase Vehículo, haréis un objeto de ella,
# lo guardaréis en un archivo y luego lo cargamos.

class Vehiculo:
    color = None
    velocidad = 0

    def __init__(self, color, velocidad):
        self.color = color
        self.velocidad = velocidad

    def __str__(self):
        return f"Soy el vehiculo de color {self.color} y tengo una velocidad de {self.velocidad} km/h"

v = Vehiculo("verde", 220)


file = open("archivo-ejercicio-8.2", "w")
file.write(str(v))
file.close()

file = open("archivo-ejercicio-8.2", "r")
texto_file = file.readlines()
print(texto_file)
