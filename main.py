import sqlite3
from Utils.menu import menu

def connect_database():
    # Conecta a la base de datos SQLite y devuelve (conexion, cursor)
    conexion = sqlite3.connect('Database/DataBaseMercado.db')
    cursorDB = conexion.cursor()
    return conexion, cursorDB

def close_database(conexion):
    # Cierra la conexión a la base de datos
    conexion.close()

if __name__ == "__main__":
    # Punto de entrada: conectar, mostrar menú y cerrar conexión
    conexion, cursorDB = connect_database()
    menu(conexion, cursorDB) 
    close_database(conexion)