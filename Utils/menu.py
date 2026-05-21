import sys

def menu(conexion, cursorDB):
    # Muestra el menú principal y dirige a las funciones de login/registro
    from Database_Controllers.login import login
    from Database_Controllers.register import register_user, register_admin
    
    try:
        # Bucle principal del menú con entrada del usuario y rutas
        print("\n[-------¡Holaaaa!, Bienvenid@ a nuestra app MercadoVentas-------]\n")
        print(" 1.- Iniciar sesión\n 2.- Crear una cuenta\n 3.- Salir")
        opcion: str = input()
        
        if opcion == "1":
            login(conexion, cursorDB)
        elif opcion == "2":
            print("\n¿Crear cuenta en el portal de empleados o en el de usuarios?\n 1.- Empleado \n 2.- Usuario")
            opcion1:str = input()
            if opcion1 == "1":
                register_admin(cursorDB, conexion)
            elif opcion1 == "2":
                register_user(cursorDB, conexion)
            else:
                print("\nOpción inválida crrrrrack, vuelve a intentarlo")
                menu(conexion, cursorDB)
        elif opcion == "3":
            sys.exit()
        else:
           print("\nOpción inválida crrrrrack, vuelve a intentarlo")
           menu(conexion, cursorDB) 
    except Exception as e:
        print("Error:", e)