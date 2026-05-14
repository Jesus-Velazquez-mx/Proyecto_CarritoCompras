import sqlite3
from Utils.menu import menu

def connect_database():
    conexion = sqlite3.connect('Database/DataBaseMercado.db')
    cursorDB = conexion.cursor()
    return conexion, cursorDB

def close_database(conexion):
    conexion.close()

if __name__ == "__main__":
    conexion, cursorDB = connect_database()
    menu(conexion, cursorDB) 
    close_database(conexion)