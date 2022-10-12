# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:
# la columna id de tipo entero, la columna nombre que será de tipo texto y
# la columna apellido que también será de tipo texto.
#
# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
#
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3

connection = sqlite3.connect("ejercicio-11.1.db")
cursor = connection.cursor()

query1 = '''CREATE TABLE Alumnos(id INT NOT NULL,
nombre TEXT,
apellido TEXT,
PRIMARY KEY(id))'''
cursor.execute(query1)

query2 = '''INSERT INTO Alumnos(id, nombre, apellido) VALUES
(1, 'Juan', 'Garcia'),
(2, 'Pedro', 'Podesta'),
(3, 'Viviana', 'Canosa'),
(4, 'Alasola', 'Buenacara'),
(5, 'Pedro', 'Almibar'),
(6, 'Johan', 'Mayer'),
(7, 'Luis', 'Caldera'),
(8, 'Tommy', 'Hilghfigher')'''
cursor.execute(query2)
connection.commit()

query3 = '''SELECT * FROM Alumnos WHERE nombre = "Luis"'''
cursor.execute(query3)
alumno_mostrar = cursor.fetchall()
connection.commit()
print("El alumno buscado es:", alumno_mostrar[0][1], alumno_mostrar[0][2])

cursor.close()
connection.close()

