class Carrito:
    def __init__(self):
        self.lista_productos = []

    # Representa un carrito de compras conteniendo una lista de productos

def compra(name, userID, cursorDB, conexion):
    # Permite al usuario navegar categorías, ver productos y añadir al carrito
    from Database_Controllers.userController import InterfazU
    
    try:
        print("\n¿Qué te interesa hoy? He aquí nuestras secciones:\n")
        cursorDB.execute("SELECT ID, NOMBRE FROM CATEGORIA")
        categorias = cursorDB.fetchall()
        print("[------------CATEGORÍAS------------]")
        for categoria in categorias:
            print("______________________________________")
            print(f"ID: {categoria[0]} [",categoria[1],"]")
            print("______________________________________")
        opcion = input("\nSelecciona la categoría que más te interese: ")
        cursorDB.execute("SELECT ID, NOMBRE_ARTICULO, PRECIO, CANTIDAD FROM PRODUCTOS WHERE CATEGORIA_ID = ?", (opcion,))
        productos = cursorDB.fetchall()
        print("[-------------------------------PRODUCTOS------------------------------]")
        for producto in productos:  
            print("________________________________________________________________________")
            print(f"ID: {producto[0]} [",producto[1]," ",producto[2]," ",producto[3],"]")
            print("________________________________________________________________________")
        opcion2:int = int(input("\nSeleccione el producto a comprar (SU ID): \n"))
        opcion3 = input("\n¿Añadir al carrito?: \n 1.- Si\n 2.- No\n")
        if opcion3 == "1":
            unidades = int(input("\n¿Cuántas unidades?:\n"))
            for producto in productos:
                 if producto[0] == opcion2:
                        cantidad_disponible = producto[3]
                        if unidades <= cantidad_disponible:
                            nueva_cantidad = cantidad_disponible - unidades
                            cursorDB.execute("INSERT INTO Carrito_Compras VALUES (?,?,?,?)", [None, userID[0], opcion2, unidades])
                            cursorDB.execute("UPDATE PRODUCTOS SET CANTIDAD = ? WHERE ID = ?", (nueva_cantidad, opcion2))
                            conexion.commit()
                            print("Se ha añadido al carrito.")
                        else:
                            print("\nLo siento, no hay suficiente stock para esa cantidad.\n")
                        break
        else:
            print("Operación cancelada.")
            compra(name, userID, cursorDB, conexion)
        opcion3 = input("Desea seguir comprando? \n 1.- Si\n 2.- No\n")
        if opcion3 == "1":
            compra(name, userID, cursorDB, conexion)
        elif opcion3 == "2":
            InterfazU(name, userID, cursorDB, conexion)
    except Exception as e:
        # Maneja errores durante la operación de compra
        print("Error:", e)
        
def venta(name, userID, cursorDB, conexion):
    # Muestra el carrito del usuario, permite pagar o eliminar artículos
    from Database_Controllers.userController import InterfazU
    
    try:
        print("[---------Carrito de ", name[0],"----------]")
        cursorDB.execute("""
            SELECT Carrito_Compras.ID, PRODUCTOS.NOMBRE_ARTICULO, PRODUCTOS.PRECIO, Carrito_Compras.CANTIDAD, CATEGORIA.NOMBRE
            FROM Carrito_Compras
            INNER JOIN PRODUCTOS ON Carrito_Compras.PRODUCTO_ID = PRODUCTOS.ID
            INNER JOIN CATEGORIA ON PRODUCTOS.CATEGORIA_ID = CATEGORIA.ID
            WHERE Carrito_Compras.USER_ID = ?
            """, (userID[0],)) 
        cosas_carrito = cursorDB.fetchall()
        for cosa in cosas_carrito:
            print("ID: ", cosa[0], "Producto:", cosa[1], "Categoría:", cosa[4])
        opcion:str = input("\n 1.- Proceder al pago\n 2.- Eliminar artículo\n 3.- Regresar\n")
        if opcion == "1":
            total = 0
            for cosa in cosas_carrito:
                nombre_producto = cosa[1]
                precio_unidad = cosa[2]
                cantidad = cosa[3]
                subtotal = precio_unidad * cantidad
                total += subtotal
                print("Producto:", nombre_producto, "Categoría:", cosa[3], "Cantidad:", cantidad, "Precio unitario:", precio_unidad, "Subtotal:", subtotal)
        elif opcion == "2":
            id_articulo = input("\nIngrese el ID del artículo a eliminar: ")
            cursorDB.execute("DELETE FROM Carrito_Compras WHERE USER_ID = ? AND ID = ?", (userID[0], id_articulo))
            conexion.commit()
            print("\nArtículo eliminado del carrito correctamente.")
            venta(name, userID, cursorDB, conexion)
        elif opcion == "3":
            InterfazU(name, userID, cursorDB, conexion)
        else:
            print("\nOpción inválida crrrrrack, vuelve a intentarlo")
            venta(name, userID, cursorDB, conexion)
        print("\nTotal a pagar:", total)
        opcion:str = input("\n¿Desea continuar?\n 1.- Si \n 2.- Regresar\n")
        if opcion == "1":
            cursorDB.execute("DELETE FROM Carrito_Compras WHERE USER_ID = ?", (userID))
            cursorDB.execute("INSERT INTO VENTAS VALUES (?,?,?,?)", (None, userID[0], cosa[0], subtotal))
            conexion.commit()
            print("\nCompra realizada con éxito. Pronto llegará a tu casa porque sé dónde vives guap@\n")
            InterfazU(name, userID, cursorDB, conexion)
    except Exception as e:
        # Maneja errores al mostrar/procesar la venta
        print("Error:", e)

def mostrar_todas_ventas(name, userID, cursorDB, conexion):
    # Muestra todas las ventas (para admins)
    from Database_Controllers.adminController import Interfaz
    
    try:
        cursorDB.execute("""
            SELECT VENTAS.ID, USUARIOS.NOMBRE, PRODUCTOS.NOMBRE_ARTICULO, VENTAS.TOTAL FROM VENTAS
            INNER JOIN USUARIOS ON VENTAS.USUARIO_ID = USUARIOS.ID
            INNER JOIN PRODUCTOS ON VENTAS.PRODUCTO_ID = PRODUCTOS.ID
        """)
        ventas = cursorDB.fetchall()

        for venta in ventas:
            print("[------------------ Todas las Ventas ------------------]")
            for venta in ventas:
                print("ID:", venta[0])
                print("Usuario:", venta[1])
                print("Producto:", venta[2])
                print("Total:", venta[3])
                print("---------------------------------------------------------")
    except Exception as e:
        # Maneja errores al consultar ventas
        print("Error en la base de datos:", e)
    Interfaz(name, userID, cursorDB, conexion)