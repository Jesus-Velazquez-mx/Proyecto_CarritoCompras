class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

def Inventario(name, cursorDB, userID, conexion):
    from Database_Controllers.adminController import Interfaz
    
    try:
        print("\n[-----------Inventario de Productos-----------]\n")
        cursorDB.execute("SELECT * FROM PRODUCTOS")
        productos = cursorDB.fetchall()
        for producto in productos:
            print("ID:", producto[0])
            print("Nombre:", producto[1])
            print("Precio:", producto[2])
            print("Cantidad:", producto[3])
            print("Categoría:", producto[4])
            print("----------------------------------------------")
        opcion:str = input("\n 1.- Eliminar producto\n 2.- Añadir producto\n 3.- Volver\n")
        if opcion == "1":
            select:str = input("\nIngrese el ID del producto a eliminar:\n")
            cursorDB.execute("DELETE FROM PRODUCTOS WHERE ID = ?", (select))
            conexion.commit()
            print("\nProducto eliminado con éxito\n")
            Inventario(name, cursorDB, userID, conexion)
        elif opcion == "2":
            nombre:str = input("\nIngrese el nombre del producto a añadir:\n")
            precio:str = input("\nIngrese su precio:\n")
            unidades:str = input("\nIngrese la cantidad a añadir:\n")
            print("\nIngrese el ID de la categoría a la que pertenece  (ID):\n")
            cursorDB.execute("SELECT ID, NOMBRE FROM CATEGORIA")
            categorias = cursorDB.fetchall()
            for categoria in categorias:
                print("ID:", categoria[0], " NOMBRE: ", categoria[1])
            id_categoria:int = int(input("\n"))
            cursorDB.execute("INSERT INTO PRODUCTOS VALUES (?,?,?,?,?)", (None, nombre, precio, unidades, id_categoria))
            conexion.commit()
            print("\nProducto añadido con éxito\n")
            Inventario(name, cursorDB, userID, conexion)
        elif opcion == "3":
            Interfaz(name, userID, cursorDB, conexion)
        else:
            print("\nOpción inválida crrrrrack, vuelve a intentarlo")
            Inventario(name, cursorDB, userID, conexion)
    except Exception as e:
        print("Error: Conexión incorrecta con la data beis", e)

def Categorias(name, userID, cursorDB, conexion):
    from Database_Controllers.adminController import Interfaz
    
    try:
        print("[-----------------Categorías-----------------]")
        cursorDB.execute("SELECT * FROM CATEGORIA")
        categorias = cursorDB.fetchall()
        for categoria in categorias:
            print("ID:", categoria[0])
            print("Nombre:", categoria[1])
            print("Descripción:", categoria[2])
            print("----------------------------------------------")
        opcion = input("\n 1.- Eliminar categoría\n 2.- Añadir categoría\n 3.- Volver\n")
        if opcion == "1":
            select = input("\nIngrese el ID de la categoría a eliminar:\n ")
            cursorDB.execute("DELETE FROM CATEGORIA WHERE ID = ?", (select))
            conexion.commit()
            print("Categoría eliminada con éxito")
            Categorias(name, userID, cursorDB, conexion) 
        elif opcion == "2":
            nombre = input("\nIngrese el nombre de la categoría a añadir:\n")
            descripcion = input("\nIngrese su Descripción: \n")
            cursorDB.execute("INSERT INTO CATEGORIA VALUES (?,?,?)", (None, nombre, descripcion))
            conexion.commit()
            print("\nCategoría añadida con éxito añadido con éxito\n")
            Categorias(name, userID, cursorDB, conexion)  
        elif opcion == "3":
            Interfaz(name, userID, cursorDB, conexion)  
            print("\nOpción inválida crrrrrack, vuelve a intentarlo")
    except Exception as e:
        print("Error en la databeis:", e)