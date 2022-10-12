# En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora:
# sumar, restar, multiplicar y dividir.
# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas.
# Los resultados tenéis que mostrarlos por consola.

# Importo las operaciones basicas de la calculadora:
import calculadora

def operando ():
    operacion = input("Escoge la operación que deseas realizar:\n"
                        "Suma: oprime S\n"
                        "Resta: oprime R\n"
                        "Multiplicación: oprime M\n"
                        "División: oprime D\n")

    if operacion == "S" or operacion == "s":
        num1 = float(input("Ingresa el primer número:"))
        num2 = float(input("Ingresa el segundo número:"))
        print("El resultado es:", calculadora.suma(num1, num2))

    elif operacion == "R" or operacion == "r":
        num1 = float(input("Ingresa el minuendo:"))
        num2 = float(input("Ingresa el sustraendo:"))
        print("El resultado es:", calculadora.resta(num1, num2))

    elif operacion == "M" or operacion == "m":
        num1 = float(input("Ingresa el primer factor:"))
        num2 = float(input("Ingresa el segundo factor:"))
        print("El resultado es:", calculadora.multiplicacion(num1, num2))

    elif operacion == "D" or operacion == "d":
        num1 = float(input("Ingresa el dividendo:"))
        num2 = float(input("Ingresa el divisor:"))
        print("El resultado es:", calculadora.division(num1, num2))

    else:
        print("El valor ingresado no es correcto")

    end()

def end():
    accion = input("¿Quieres realizar otra operación? S/N")

    if accion == "S" or accion == "s":
        operando()
    elif accion == "N" or accion == "n":
        pass
    else:
        print("El valor ingresado no es correcto")
        end()

operando()
