class User:
    Incremento = 0
    def __init__(self, nombre, contrasena, correo, numero):
        self.nombre = nombre
        self.contrasena = contrasena
        self.correo = correo
        self.numero = numero
        self.acceso = False

    # Clase base que representa un usuario con datos básicos y estado de acceso

def InterfazU(name, userID, cursorDB, conexion):
    # Interfaz de usuario: opciones para comprar, ver carrito o salir
    from Database_Controllers.cartController import compra, venta
    from Utils.menu import menu
    
    print("\n¡Hola de nuevo", name[0], "!\n ¿Qué desea hacer hoy?\n 1.- Comprar producto\n 2.- Mostrar Carrito\n 3.- Salir al menú")
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