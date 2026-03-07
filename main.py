
from funciones import Validacion_numero, Validacion_de_clave, validar_user_activo, Bloquear
from Dicionario import usuarios
from cajero import cajero
from Colores import RESET, NEGRO,ROJO,VERDE, AMARILLO, AZUL, MAGENTA, CYAN, BLANCO, GRIS, ROJO_BRILLANTE, VERDE_BRILLANTE,AMARILLO_BRILLANTE,AZUL_BRILLANTE,MAGENTA_BRILLANTE,CYAN_BRILLANTE,BLANCO_BRILLANTE,NEGRITA,SUBRAYADO,INVERTIDO
autenticacion = True
id_Usuario = ""
Contador = 0
while autenticacion:
    print(VERDE+"""
      Bienvenido a Nuestro Banco TechBank Riwi Digital
      """+VERDE)
    N_Usuario = input(AMARILLO+"Numero de Usuario: "+AMARILLO)
    Clave = input(AMARILLO+"Clave: "+AMARILLO)
    Var_Validacion_numero = Validacion_numero(N_Usuario)
    if Var_Validacion_numero:
        id_Usuario = Var_Validacion_numero
        Var_validar_user_activo = validar_user_activo(id_Usuario)
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
                        print(VERDE+"Salida Exitosa"+VERDE)
                        print("")
                    else:
                        print(Var_cajero)
            else:
                Contador = Contador + 1
                print(ROJO+"------------------"+ROJO)
                print(ROJO+"-Clave incorrecta-"+ROJO)
                print(ROJO+"------------------"+ROJO)
                if Contador == 3:
                    VarBloquear = Bloquear(id_Usuario)
                    print("")
                    print(ROJO+VarBloquear+ROJO)
                    print("")
        else:
            print(ROJO+"--------------------------------------------------------"+ROJO)
            print(ROJO+"-Usuario inactivo Comuniquese con los servicios de riwi-"+ROJO)
            print(ROJO+"--------------------------------------------------------"+ROJO)
    else:
        print(ROJO+"--------------------"+ROJO)
        print(ROJO+"-Usuario incorrecto-"+ROJO)
        print(ROJO+"--------------------"+ROJO)
        