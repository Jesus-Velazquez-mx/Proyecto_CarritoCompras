import bcrypt
import pwinput

def login(conexion, cursorDB): 
    from Database_Controllers.adminController import Interfaz
    from Database_Controllers.userController import InterfazU
    
    print("\n[-------¡Holaaaa!, Bienvenid@ a nuestra app MercadoVentas-------]\n")
    mail = input("Ingrese su correo: ")
    password = pwinput.pwinput("Ingrese su contraseña: ", mask='*')
    
    cursorDB.execute("SELECT CORREO, CONTRASENA FROM USUARIOS WHERE CORREO = ?", (mail,))
    user = cursorDB.fetchone() 
    if user:
        stored_password = user[1]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            cursorDB.execute("SELECT NOMBRE FROM USUARIOS WHERE CORREO = ?", (mail,))
            name = cursorDB.fetchone()
            cursorDB.execute("SELECT ID FROM USUARIOS WHERE CORREO = ?", (mail,))
            userID = cursorDB.fetchone()
            InterfazU(name, userID, cursorDB, conexion)
            return
    cursorDB.execute("SELECT CORREO, CONTRASENA FROM EMPLEADOS WHERE CORREO = ?", (mail,))
    empleado = cursorDB.fetchone()
    if empleado:
        stored_password = empleado[1]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            cursorDB.execute("SELECT NOMBRE FROM EMPLEADOS WHERE CORREO = ?", (mail,))
            name = cursorDB.fetchone()
            cursorDB.execute("SELECT ID FROM EMPLEADOS WHERE CORREO = ?", (mail,))
            userID = cursorDB.fetchone()
            Interfaz(name, userID, cursorDB, conexion)
            return
            
    print("Lo siento, los datos proporcionados no coinciden, favor de intentarlo denuevo")
    login(conexion, cursorDB)