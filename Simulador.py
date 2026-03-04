
from funciones import Validacion_Usuario
from Dicionario import usuarios
from cajero import cajero
autenticacion = True
id_Usuario = ""

while autenticacion:
    print("""
      Bienvenido a Nuestro Banco
      """)
    N_Usuario = input("Numero de Usuario: ")
    Clave = input("Clave: ")
    validacion_user=Validacion_Usuario(N_Usuario, Clave)

    if validacion_user:
        autenticacion = True
        id_Usuario = validacion_user
        Salir = True
        while Salir:
            Var_cajero = cajero(id_Usuario)
            if Var_cajero == False:
                Salir = False
                print("")
                print("Salida Exitosa")
                print("")
            else:
                print(Var_cajero)
                
    else:
        print("Usuario o contraseña incorrecta")