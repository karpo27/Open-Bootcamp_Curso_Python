import operaciones as o
import sys
import ejemplo.suma
import pprint

def main():
    op = o.Operador()
    print(op.multiplicacion(4, 2))
    print(o.PI)
    print(sys.path)
    ejemplo.suma.suma(2, 5)
    print(ejemplo.suma.suma(2, 5))
    mp = ejemplo.suma.Multiplicador()
    print(mp.multiplica(5, 10))

    pprint.pprint(globals())



if __name__ == '__main__':
    main()

variable = 11
print(variable)

globals()['variable'] = 19
print(variable)

def suma1(a, b):
    return a + b

def resta1(a, b):
    return a - b

pprint.pprint(globals())

def prueba(inicial):
    valor = 5
    estado = False
    pprint.pprint((locals()))

prueba(2)
