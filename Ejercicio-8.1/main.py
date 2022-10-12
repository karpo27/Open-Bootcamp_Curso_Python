# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
# lo abráis y escribáis dentro del archivo.
# Para ello, tendréis que acceder dos veces al archivo creado.

a = open('ejemplo.txt', 'r')
a.close()


a = open('ejemplo.txt', 'w')
a.write("Hola mundo!")
a.close()

