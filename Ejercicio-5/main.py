# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

insertar_año = int(input("Inserta un año para saber si es bisiesto o no: "))

def año(insertar_año):
    if insertar_año > 0 and insertar_año % 4 == 0:
        print("El año", insertar_año, "es bisiesto")
    elif insertar_año == 0:
        print("El año", insertar_año, "no es bisiesto")
    else:
        print("El año", insertar_año, "no es bisiesto")

año(insertar_año)