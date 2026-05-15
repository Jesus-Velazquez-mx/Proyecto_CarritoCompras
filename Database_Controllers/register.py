import bcrypt
import pwinput

def _obtener_datos_base():
    name = input("\nIngrese su nombre completo: ")
    password = pwinput.pwinput("Ingrese una contraseña (¡Recuérdala siempre! ;D): ", mask='*')
    passwordC = pwinput.pwinput("Confirma tu contraseña: ", mask='*')
    
    while password != passwordC:
        print("\n¡Uups!, parece que las contraseñas no coinciden, vuelve a intentarlo\n")
        password = pwinput.pwinput("Ingrese una contraseña (¡Recuérdala siempre! ;D): ", mask='*')
        passwordC = pwinput.pwinput("Confirma tu contraseña: ", mask='*')
        
    pwd = password.encode('utf-8')
    encrypt1 = bcrypt.gensalt()
    contraEncriptada = bcrypt.hashpw(pwd, encrypt1)     
    
    mail = input("Ingrese su correo electrónico: ")
    numeroT = input("Ingrese su número de teléfono: ")
    
    return name, contraEncriptada, mail, numeroT

def register_user(cursorDB, conexion):
    from Database_Controllers.login import login
    
    print("[-------¡Holaaaa!, Bienvenid@ nuevo usuario a nuestra app MercadoVentas-------]") 
    name, contraEncriptada, mail, numeroT = _obtener_datos_base()
    
    cursorDB.execute("INSERT INTO USUARIOS VALUES (?,?,?,?,?)", (None, name, contraEncriptada, mail, numeroT))
    conexion.commit()
    print("Usuario registrado exitosamente.")
    login(conexion, cursorDB)

def register_admin(cursorDB, conexion):
    from Database_Controllers.login import login
    
    print("[-------¡Holaaaa!, Bienvenid@ nuevo empleado a nuestra app MercadoVentas-------]")
    name, contraEncriptada, mail, numeroT = _obtener_datos_base()
    
    cursorDB.execute("INSERT INTO EMPLEADOS VALUES (?,?,?,?,?,?)", (None, name, contraEncriptada, mail, numeroT, 0.00))
    conexion.commit()
    print("Empleado registrado exitosamente.")
    login(conexion, cursorDB)