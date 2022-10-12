# Formateo de cadena

numero = 5
texto = "quijote"
otromas = 1.2

print("el numero es %d y el texto es %s y tiene %f" % (numero, texto, otromas))

print("el numero es {} y el texto es {} y tiene {}". format(numero, texto, otromas))

print("el numero es {1} y el texto es {0} y tiene {2}". format(numero, texto, otromas))

print("el numero es {n1} y el texto es {texto} y tiene {otromas}". format(n1=numero, texto=texto, otromas=otromas))

print(f'el numero es {numero} y el texto es {texto} y tiene {otromas}')

class Juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
#para salida normal
    def __str__(self):
        return f'Mi nombre es {self.nombre} y mi precio es {self.precio}'
#para salida tecnica o depuracion de errores. Si una clase tiene ambas se ejecuta repr
    def __repr__(self):
        return f'Potato({self.nombre},{self.precio})'

j1 = Juguete("Potato", 10.5)
print(j1)

print(str(j1))
print(repr(j1))

import pprint
pprint.pprint(dir(''))

cadena = "en un lugar de la manchA"
print(cadena.count('d'))
print(cadena.lower().count('a'))

n = '5'
print(n.isdigit())

a = '%'
b = 'h'
print(a.isalpha())
print(b.isalpha())
print(cadena.split())
print(cadena.split('en'))
print(cadena.startswith('en'))
print(cadena.endswith('man'))

f = open('D:\Mis Documentos\Cuils familiares.txt', 'r')
datos = f.read()
f.close()
print(datos)

f = open('D:\Mis Documentos\Cuils familiares.txt', 'r')
datos1 = f.readlines()
f.close()
print(datos1)

f = open('mifichero.txt', 'w')
f.write("datos\n")
f.write("datos2\n")
f.close()


def escribe(fichero, datos):
    f = open(fichero, 'w')

    for linea in datos:
        if not linea.endswith('\r') == False:
            linea = linea + '\n'

        f.write(linea)

    f.close()

lista = ['una linea\n', 'dos lineas\n', 'tres lineas\n']

f = open('mifichero1.txt', 'w')
f.writelines(lista)

f.close()

import pickle

class Juguete1:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre

j = Juguete1("Potato", 10.5)

f = open('datos.bin', 'wb')
pickle.dump(j, f)
f.close()

j3 = Juguete1("Potato", 10.5)

f = open('datos.bin', 'rb')
potato = pickle.load(f)
f.close()

print(type(potato))
print(potato.getNombre(), potato.precio)

#class Estado:
#    players = Players()
#    status = Status()
#    life_remaining = 12
#    armor = False

#f = open('gamestatus.dat', 'rb')
#e = pickle.load(f)
#f.close()


class Persona:
    def __init__(self, nombre, apellido, dni, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono

class Empleado(Persona):
    def __init__(self, nombre, apellido, dni, telefono, salario):
        super().__init__(nombre, apellido, dni, telefono)
        self.salario = salario

class Cliente(Persona):
    def __init__(self, nombre, apellido, dni, telefono, categoria):
        super().__init__(nombre, apellido, dni, telefono)
        self.categoria = categoria

emp = Empleado('lucas', 'moy', '123', '233445245', '20000')
print(emp.dni)