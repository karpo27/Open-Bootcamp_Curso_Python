
def mifuncion(nombre):
    print("Hola", nombre)

def matematica(a, b):

    def suma(a, b):
        print(a + b)

    def resta(a, b):
        print(a - b)

    suma(a, b)
    resta(a, b)

mifuncion("Victor")
matematica(5, 3)

def suma1(a, b=1):
    print(a + b)

suma1(2)
suma1(2, 4)

def suma2(*args):
    resultado = 0
    for arg in args:
        resultado += arg

    print(resultado)

suma2(1, 2, 5, 7, 0, 3, 4, 4)
suma2(2, 5, 0)

def suma3(**kwargs):
    if "coche" not in kwargs:
        return
    if kwargs["coche"] == "bonito":
        print("tu coche es bonito")

suma3(coche = "bonito")

def suma4(**kwargs):
    if "coche" not in kwargs:
        return
    if kwargs["coche"] == "bonito":
        print("tu coche es bonito")

suma4(coche = "bonito")

def operaciones(a, b):
    return a + b, a - b, a * b, a / b

suma, resta, mult, div = operaciones(2, 4)
print(suma)
print(resta)
print(mult)
print(div)

anonima = lambda nombre, nombre2: \
    print("hola", nombre, nombre2)

anonima("juan", "pepe")

sumatoria = lambda x: x + x

print(sumatoria(2))