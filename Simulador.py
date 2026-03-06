
from funciones import Validacion_Usuario
from Dicionario import usuarios
from cajero import cajero

# RESET
RESET="\033[0m"

# COLORES BÁSICOS
NEGRO="\033[30m"
ROJO="\033[31m"
VERDE="\033[32m"
AMARILLO="\033[33m"
AZUL="\033[34m"
MAGENTA="\033[35m"
CYAN="\033[36m"
BLANCO="\033[37m"

# COLORES BRILLANTES
GRIS = "\033[90m"
ROJO_BRILLANTE="\033[91m"
VERDE_BRILLANTE="\033[92m"
AMARILLO_BRILLANTE= "\033[93m"
AZUL_BRILLANTE="\033[94m"
MAGENTA_BRILLANTE="\033[95m"
CYAN_BRILLANTE="\033[96m"
BLANCO_BRILLANTE="\033[97m"

# ESTILOS DE TEXTO
NEGRITA="\033[1m"
SUBRAYADO="\033[4m"
INVERTIDO="\033[7m"

autenticacion = True
id_Usuario=""

while autenticacion:
    print(VERDE + """ 
      --------------Bienvenido a Nuestro Banco TechBank---------------- 
      """ +VERDE)
    N_Usuario=input(AMARILLO+"Numero de Usuario: "+AMARILLO)
    Clave=input(AMARILLO+"Clave: "+AMARILLO)
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
                print(VERDE+"Salida Exitosa"+VERDE)
                print("")
            else:
                print(Var_cajero)
                
    else:
        print(ROJO+"Usuario o contraseña incorrecta"+ROJO)