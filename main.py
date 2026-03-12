# Importa funciones necesarias desde el archivo funciones.py
# Estas funciones permiten validar número de cuenta, validar clave,
# verificar si el usuario está activo y bloquear usuarios
from funciones import Validacion_numero, Validacion_de_clave, validar_user_activo, Bloquear

# Importa el diccionario donde están guardados los usuarios
from Dicionario import usuarios

# Importa la función cajero que contiene el menú principal del cajero automático
from cajero import cajero

# Importa variables de colores para mostrar texto con estilos en la consola
from Colores import RESET, NEGRO,ROJO,VERDE, AMARILLO, AZUL, MAGENTA, CYAN, BLANCO, GRIS, ROJO_BRILLANTE, VERDE_BRILLANTE,AMARILLO_BRILLANTE,AZUL_BRILLANTE,MAGENTA_BRILLANTE,CYAN_BRILLANTE,BLANCO_BRILLANTE,NEGRITA,SUBRAYADO,INVERTIDO


# Variable que controla el ciclo de autenticación del sistema
autenticacion = True

# Variable donde se guardará el id del usuario autenticado
id_Usuario = ""

# Contador para los intentos fallidos de clave
Contador = 0


# Bucle principal del sistema de autenticación
while autenticacion:

    # Mensaje de bienvenida al banco
    print(VERDE+"""
      Bienvenido a Nuestro Banco TechBank Riwi Digital
      """+VERDE)

    # Solicita el número de usuario (número de cuenta)
    N_Usuario = input(AMARILLO+"Numero de Usuario: "+AMARILLO)

    # Solicita la clave
    Clave = input(AMARILLO+"Clave: "+AMARILLO)

    # Valida si el número de usuario existe en el sistema
    Var_Validacion_numero = Validacion_numero(N_Usuario)

    # Si el número de usuario existe
    if Var_Validacion_numero:

        # Guarda el id del usuario encontrado
        id_Usuario = Var_Validacion_numero

        # Verifica si el usuario está activo o bloqueado
        Var_validar_user_activo = validar_user_activo(id_Usuario)

        # Si el usuario está activo
        if Var_validar_user_activo == "Activo":

            # Valida si la clave ingresada es correcta
            Var_Validacion_Clave = Validacion_de_clave(id_Usuario,Clave)

            if Var_Validacion_Clave == True:

                # Mantiene la autenticación activa
                autenticacion = True

                # Variable para controlar la salida del cajero
                Salir = True

                # Bucle del menú del cajero
                while Salir:

                    # Ejecuta la función cajero con el id del usuario
                    Var_cajero = cajero(id_Usuario)

                    # Si el cajero devuelve False significa que el usuario salió
                    if Var_cajero == False:

                        Salir = False

                        print("")
                        print(VERDE+"Salida Exitosa"+VERDE)
                        print("")

                    else:
                        # Si devuelve algún mensaje se imprime
                        print(Var_cajero)

            else:
                # Si la clave es incorrecta se aumenta el contador de intentos
                Contador = Contador + 1

                print(ROJO+"------------------"+ROJO)
                print(ROJO+"-Clave incorrecta-"+ROJO)
                print(ROJO+"------------------"+ROJO)

                # Si el usuario falla 3 veces se bloquea la cuenta
                if Contador == 3:

                    VarBloquear = Bloquear(id_Usuario)

                    print("")
                    print(ROJO+VarBloquear+ROJO)
                    print("")

        else:
            # Mensaje si el usuario está bloqueado o inactivo
            print(ROJO+"--------------------------------------------------------"+ROJO)
            print(ROJO+"-Usuario inactivo Comuniquese con los servicios de riwi-"+ROJO)
            print(ROJO+"--------------------------------------------------------"+ROJO)

    else:
        # Mensaje si el número de usuario no existe
        print(ROJO+"--------------------"+ROJO)
        print(ROJO+"-Usuario incorrecto-"+ROJO)
        print(ROJO+"--------------------"+ROJO)