
from funciones import Validacion_Usuario
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
        autenticacion = False
        id_Usuario = validacion_user
        cajero()
    else:
        print("Usuario o contraseña incorrecta")