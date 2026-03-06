
from funciones import Validacion_numero, Validacion_de_clave, validar_user_activo, Bloquear
from Dicionario import usuarios
from cajero import cajero
autenticacion = True
id_Usuario = ""
Contador = 0
while autenticacion:
    print("""
      Bienvenido a Nuestro Banco TechBank Riwi Digital
      """)
    N_Usuario = input("Numero de Usuario: ")
    Clave = input("Clave: ")
    Var_Validacion_numero = Validacion_numero(N_Usuario)
    if Var_Validacion_numero:
        id_Usuario = Var_Validacion_numero
        Var_validar_user_activo = validar_user_activo(id_Usuario)
        print(Var_validar_user_activo)
        if Var_validar_user_activo == "Activo":     
            Var_Validacion_Clave = Validacion_de_clave(id_Usuario,Clave)

            if Var_Validacion_Clave == True:
                autenticacion = True
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
                Contador = Contador + 1
                print("------------------")
                print("-Clave incorrecta-")
                print("------------------")
                if Contador == 3:
                    VarBloquear = Bloquear(id_Usuario)
                    print("")
                    print(VarBloquear)
                    print("")
        else:
            print("--------------------------------------------------------")
            print("-Usuario inactivo Comuniquese con los servicios de riwi-")
            print("--------------------------------------------------------")
    else:
        print("--------------------")
        print("-Usuario incorrecto-")
        print("--------------------")
        