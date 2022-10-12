import _thread
import time

#def horaActual(nombre_thread, tiempo_de_espera):
    #time.sleep(tiempo_de_espera)

    #print(f'hilo: {nombre_thread} - {time.ctime(time.time())}')

#_thread.start_new_thread(horaActual, ("thread uno", 1))
#_thread.start_new_thread(horaActual, ("thread dos", 5))

#while True:
    #pass

import logging

#logging.basicConfig(level=logging.INFO)
#logging.info("arranca programa")
#logging.debug("prueba de debug")
#logging.warning("hace calor")
#logging.error("test")
#logging.critical("adios")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mifuncion(x):
    if x % 2 == 0:
        return True

    return False

resultado = filter(mifuncion, numeros)
print(list(resultado))

def cuadrado(x):
    return x * x

resultado1 = map(cuadrado, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(resultado1))

from functools import reduce

def suma(a, b):
    print(f'a={a}, b={b}')
    return a + b

numeros1 = [1, 2, 3, 4, 5]
resultado2 = reduce(suma, numeros1)
print(resultado2)

cursos = ['Java', 'Python', 'Git']
asistentes = [15, 20, 4]

demo = zip(cursos, asistentes)
print(list(demo))

lista = [1 == 1, 2 == 2, 3 == 4]
resultado3 = any(lista)
print(resultado3)

resultado4 = all(lista)
print(resultado4)

a = 5.5
b = 5.4
c = 5.6

print(round(a))
print(round(b))
print(round(c))

print(max(1, 2, 4, 16, 3))

from getpass import getpass

user = input("username: ")
passwd = getpass("password: ")

print(user, passwd)

secreto = 50
valor = input("pon el numero")
print(int(valor))