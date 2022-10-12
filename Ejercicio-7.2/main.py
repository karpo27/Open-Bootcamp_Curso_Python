# En este segundo ejercicio tendréis que crear un script que nos diga si es la hora de ir a casa.
# Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
# En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario,
# haréis una operación para calcular el tiempo que queda de trabajo.

import time

fecha = time.ctime()
print("Fecha:", time.ctime())

a = time.strptime(fecha)

if a.tm_hour >= 19:
    print("Ya es hora de ir a casa...")

else:
    tiempo_restante = 19 - a.tm_hour
    print("Aún quedan", tiempo_restante, "horas de trabajo")