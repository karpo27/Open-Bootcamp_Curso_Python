# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# Cilindrada
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
    color = None
    ruedas = None
    puertas = None

class Coche(Vehiculo):
    def atributosCoche(self):
        self.vel = 220
        self.cilin = 2.5
        self.color = "negro"
        self.ruedas = 4
        self.puertas = 5

        print("El Coche es de color", self.color,)
        print("Tiene", self.ruedas, "ruedas")
        print("Tiene", self.puertas, "puertas")
        print("Su velocidad máxima es de", self.vel, "km/h")
        print("Tiene una cilindrada de", self.cilin, "litros")

c = Coche()
c.atributosCoche()
