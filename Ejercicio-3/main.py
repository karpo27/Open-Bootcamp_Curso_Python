#Calculadora de Indice de Masa Corporal (IMC)

peso = float(input("¿Cual es tu peso en kg?"))
estatura = float(input("¿Cual es tu estatura en m?"))

imc = round(peso / (estatura**2),2)
print("Tu índice de masa corporal es ", imc)

if imc < 18.5:
    print("Por lo tanto tu peso es inferior al normal")
elif imc >= 18.5 and imc < 24.9:
    print("Por lo tanto tu peso es normal")
elif imc >= 24.9 and imc < 29.9:
    print("Por lo tanto tu peso es superior al normal")
else:
    print("Por lo tanto tu tienes obesidad")
