# Crea un script que le pida al usuario una lista de países (separados por comas).
# Éstos se deben almacenar en una lista.
# No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

# Pido al usuario que ingrese listado de paises:
paises = input("Ingresa un listado de paises:")

#Coloco Mayusculas al inicio de cada palabra:
lista_paises = paises.title()

#Agrupo paises en lista:
lista_paises1 = lista_paises.split()

#Remuevo paises repetidos usando set():
lista_paises2 = set(lista_paises1)

#Convierto a lista nuevamente, y ordeno alfabeticamente y muestro por pantalla:
lista_paises_final = sorted(list(lista_paises2))
print(lista_paises_final)

