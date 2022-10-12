a = 5
b = 6
c = 7

r1 = a > b
print(r1)

r2 = a < b
print(r2)

r3 = a == b
print(r3)

r4 = (a > 5 and c < 7)
print(r4)

if a >= 6 and b <= 6:
    print("esoty en el if")
elif a == 4:
    print("estoy en elif")
else:
    print("no haz nada")

contador = 5

while contador <= 10:
    print("contador vale", contador)
    contador = contador + 1

contador1 = 1

while contador1 <= 10:
    print("contador vale", contador1)

    if contador1 == 5:
        break
    contador1 = contador1 + 1

print("fuera del while")

lista = [1, 2, 3, 4, 'fin']
tupla = (1, 2, 3, 'c', 'd')

longitud = len(lista)
print("lista tiene", longitud, "elementos")

for valor in lista:
    print(valor)

for numero in range(5, 10):
    print(numero)

lista1 = [3, 10, 8, 1, 6]

listaordenada = sorted(lista1)
print(listaordenada)

listareves = sorted(lista1, reverse=True)
print(listareves)

valor = 3

match valor:
    case 1:
        print("valor 1")
    case 2:
        print("valor 2")
    case 3:
        print("valor 3")
    case 4:
        print("valor 4")

if 5 < 6:
    pass

z = 2
print("el precio es ", z)