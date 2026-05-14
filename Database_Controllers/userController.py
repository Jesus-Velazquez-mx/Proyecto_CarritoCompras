import sqlite3
import bcrypt
from getpass import getpass

class User:
    Incremento = 0
    def __init__(self, nombre, contrasena, correo, numero):
        self.nombre = nombre
        self.contrasena = contrasena
        self.correo = correo
        self.numero = numero
        self.acceso = False

def register_user(cursorDB, conexion):
    print("[-------¡Holaaaa!, Bienvenid@ nuevo usuario a nuestra app MercadoVentas-------]") 
    name = input("\nIngrese su nombre completo: ")
    password = getpass("Ingrese una contraseña (¡Recuérdala siempre! ;D): ")
    passwordC = getpass("Confirma tu contraseña: ")
    while password != passwordC:
        print("\n¡Uups!, parece que las contraseñas no coinciden, vuelve a intentarlo\n")
        password = getpass("Ingrese una contraseña (¡Recuérdala siempre! ;D): ")
        passwordC = getpass("Confirma tu contraseña: ")
    pwd = password.encode('utf-8')
    encrypt1 = bcrypt.gensalt()
    contraEncriptada = bcrypt.hashpw(pwd, encrypt1)     
    mail = input("Ingrese su correo electrónico: ")
    numeroT = input("Ingrese su número de teléfono: ")
    new_user = User(name, contraEncriptada, mail, numeroT)
    cursorDB.execute("INSERT INTO USUARIOS VALUES (?,?,?,?,?)", (None, name, contraEncriptada, mail, numeroT))
    conexion.commit()
    print("Usuario registrado exitosamente.")
    login(conexion, cursorDB) 

def login(conexion, cursorDB): 
    from Database_Controllers.adminController import Interfaz
    
    print("\n[-------¡Holaaaa!, Bienvenid@ a nuestra app MercadoVentas-------]\n")
    mail = input("Ingrese su correo: ")
    password = getpass("Ingrese su contraseña: ")
    cursorDB.execute("SELECT CORREO, CONTRASENA FROM USUARIOS WHERE CORREO = ?", (mail,))
    user = cursorDB.fetchone() 
    if user:
        stored_password = user[1]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            cursorDB.execute("SELECT NOMBRE FROM USUARIOS")
            name = cursorDB.fetchone()
            cursorDB.execute("SELECT ID FROM USUARIOS")
            userID = cursorDB.fetchone()
            InterfazU(name, userID, cursorDB, conexion)
            return
    cursorDB.execute("SELECT CORREO, CONTRASENA FROM EMPLEADOS WHERE CORREO = ?", (mail,))
    empleado = cursorDB.fetchone()
    if empleado:
        stored_password = empleado[1]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            cursorDB.execute("SELECT NOMBRE FROM EMPLEADOS")
            name = cursorDB.fetchone()
            cursorDB.execute("SELECT ID FROM USUARIOS")
            userID = cursorDB.fetchone()
            Interfaz(name, userID, cursorDB, conexion)
            return
    print("Lo siento, los datos proporcionados no coinciden, favor de intentarlo denuevo")
    login(conexion, cursorDB)

def InterfazU(name, userID, cursorDB, conexion):
    from Database_Controllers.cartController import compra, venta
    from Utils.menu import menu
    
    print("\n¡Hola de nuevo ", name[0], "!\n ¿Qué desea hacer hoy?\n 1.- Comprar producto\n 2.- Mostrar Carrito\n 3.- Salir al menú")
    opcion: str = input()
    if opcion == "1":
        compra(name, userID, cursorDB, conexion)
    elif opcion == "2":
        venta(name, userID, cursorDB, conexion)
    elif opcion == "3":
        print("\nSaliendo al menú...")
        menu(conexion, cursorDB)
    else:
        print("\nOpción inválida crrrrrack, vuelve a intentarlo")
        InterfazU(name, userID, cursorDB, conexion)