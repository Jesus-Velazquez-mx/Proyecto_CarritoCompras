import sqlite3
import bcrypt
from getpass import getpass
from Database_Controllers.userController import User

class Admin(User):
    def __init__(self, nombre, contrasena, correo, numero):
        super().__init__(nombre, contrasena, correo, numero)

def register_admin(cursorDB, conexion):
    from Database_Controllers.userController import login
    
    print("[-------¡Holaaaa!, Bienvenid@ nuevo empleado a nuestra app MercadoVentas-------]")
    name = input("\nIngrese su nombre completo: ")
    password = getpass("Ingrese una contraseña (¡Recuérdala siempre! ;D): ")
    passwordC = getpass("Confirma tu contraseña: ") 
    while password != passwordC:
        print("\n¡Uups!, parece que las contraseñas no coinciden, vuelve a intentarlo\n")
        password = getpass("Ingrese una contraseña (¡Recuérdala siempre! ;D): ")
        passwordC = getpass("Confirma tu contraseña: ")    
    pwd = password.encode('utf-8')
    encrypt2 = bcrypt.gensalt()
    contraEncriptada = bcrypt.hashpw(pwd, encrypt2)    
    mail = input("Ingrese su correo electrónico: ")
    numeroT = input("Ingrese su número de teléfono: ")
    cursorDB.execute("INSERT INTO EMPLEADOS VALUES (?,?,?,?,?,?)", (None, name, contraEncriptada, mail, numeroT, 0.00))
    conexion.commit()
    print("Empleado registrado exitosamente.")
    login(conexion, cursorDB)

def Interfaz(name, userID, cursorDB, conexion):
    from Database_Controllers.productController import Inventario, Categorias
    from Database_Controllers.cartController import mostrar_todas_ventas
    from Utils.menu import menu
    
    print("\n¡Hola de nuevo ", name[0],"!\n¿Qué desea hacer hoy?\n 1.- Gestión de inventarios\n 2.- Ver categorías\n 3.- Registro de ventas\n 4.- Salir al menú")
    opcion: str = input()
    if opcion == "1":
        Inventario(name, cursorDB, userID, conexion)
    elif opcion == "2":
        Categorias(name, userID,cursorDB, conexion)
    elif opcion == "3":
        mostrar_todas_ventas(name, userID, cursorDB, conexion)
    elif opcion == "4":
        print("\nSaliendo al menú...")
        menu(conexion, cursorDB)
    else:
        print("\nOpción inválida crrrrrack, vuelve a intentarlo")