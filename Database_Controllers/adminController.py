from Database_Controllers.userController import User

class Admin(User):
    # Subclase de User para representar a un administrador
    def __init__(self, nombre, contrasena, correo, numero):
        super().__init__(nombre, contrasena, correo, numero)

def Interfaz(name, userID, cursorDB, conexion):
    # Interfaz principal para admins: elegir entre inventario, categorías o ventas
    from Database_Controllers.productController import Inventario, Categorias
    from Database_Controllers.cartController import mostrar_todas_ventas
    from Utils.menu import menu
    
    print("\n¡Hola de nuevo", name[0],"!\n¿Qué desea hacer hoy?\n 1.- Gestión de inventarios\n 2.- Ver categorías\n 3.- Registro de ventas\n 4.- Salir al menú")
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