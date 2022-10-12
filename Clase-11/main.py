import getpass
import sqlite3

def main():
    pass
    username = input("Nombre de usuario:")
    password = getpass.getpass("Contraseña:")

    if verifica_credenciales():
        print("Login correcto")
    else:
        print("Login incorrecto")

def verifica_credenciales(username, password):
    conn = sqlite3.connect("miaplicacion.db")
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    print("query a ejecutar:", query)

    rows = cursor.execute(query)
    data = rows.fetchone()
    print("data es:", type(data))

    cursor.close()
    conn.close()



#if __name__ == '__main__':
    #main()


def main2():
    crear_usuario(4, "pepe", "superclave")

def crear_usuario(identificador, usuario, clave):
    conn = sqlite3.connect("miaplicacion.db", isolation_level=None)
    cursor = conn.cursor()

    query = '''INSERT INTO users (id, username, password) VALUES(?, ?, ?)'''
    print("query a ejecutar:", query)

    rows = cursor.execute(query, (identificador, usuario, clave))
    print(type(rows))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main2__':
    main2()