# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno,
# que tenga como atributos su nombre y su nota.
# Deberéis de definir los métodos para inicializar sus atributos,
# imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

a1 = Alumno("Juan Gonzalez", 2)
print("El alumno", a1.nombre, "obtuvo un", a1.nota)

if a1.nota >= 6:
    print("El alumno ha aprobado")

else:
    print("El alumno ha desaprobado")