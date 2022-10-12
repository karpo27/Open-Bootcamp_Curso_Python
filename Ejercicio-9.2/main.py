# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá
# los elementos impares de una lista pasada por parámetro con filter
# y realizará una suma de todos estos elementos obtenidos mediante reduce.

# Defino lista ejemplo:
lista_ejemplo = [1, 22, 15, 4, 71, 6, 7, 96]

# Defino funcion que chequea pares/impares:
def Operacion(x):
    if x % 2 == 0:
        return False

    else:
        return True

# Armo lista de impares del resultado de pasar filter por lista_ejemplo:
lista_numeros_impares = list(filter(Operacion, lista_ejemplo))
print("La lista de impares es:", lista_numeros_impares)

# Defino funcion para pasar por reduce:
def Suma(x1, x2):
    return x1 + x2

# Uso reduce para obtener suma de elementos:
from functools import reduce

suma_numeros_impares = reduce(Suma, lista_numeros_impares)
print("El resultado de la suma de la lista es:" , suma_numeros_impares)

