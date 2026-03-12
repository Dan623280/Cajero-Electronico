# Importa el diccionario de usuarios donde están almacenados
# los datos de cada cliente del banco
from Dicionario import usuarios

# Importa la librería para generar números aleatorios
import random

# Importa librería para usar colores en la consola
from colorama import init, Fore, Style

# Importa variables de colores personalizadas
from Colores import RESET, NEGRO,ROJO,VERDE, AMARILLO, AZUL, MAGENTA, CYAN, BLANCO, GRIS, ROJO_BRILLANTE, VERDE_BRILLANTE,AMARILLO_BRILLANTE,AZUL_BRILLANTE,MAGENTA_BRILLANTE,CYAN_BRILLANTE,BLANCO_BRILLANTE,NEGRITA,SUBRAYADO,INVERTIDO

# Inicializa colorama para que los colores funcionen automáticamente
init(autoreset=True)


#--------------------------------
# FUNCION PARA OBTENER EL NOMBRE DEL USUARIO
#--------------------------------
def nombre_user(id):
    
    # Busca el nombre del usuario dentro del diccionario
    nombre = usuarios[id]["nombre"]
    
    # Retorna el nombre
    return nombre


#------------------------
# VALIDACIONES
#------------------------------

# Valida si un número de cuenta existe
def Validacion_numero(N_cuenta):

    # Recorre todos los usuarios
    for id, datos in usuarios.items():

        # Si el número de cuenta coincide
        if datos["Numero_Cuenta"] == N_cuenta:

            # retorna el id del usuario
            return(id)


# Devuelve todos los datos del usuario
def Datos_user(id):

    datos = usuarios.get(id)

    return datos


# Verifica si el usuario está activo o bloqueado
def validar_user_activo(id):

    if usuarios[id]["Validacion"] == "Activo":
        return "Activo"
    else:
        return "Inactivo"


# Bloquea un usuario
def Bloquear(id):

    usuarios[id]["Validacion"] = "Inactivo"

    mensaje = AMARILLO+"Usuario Bloqueado"+AMARILLO

    return mensaje


#----------------------------------------------------
# 1. GESTION DE CLAVE
#----------------------------------------------------

# Valida si la clave ingresada es correcta
def Validacion_de_clave(id,clave):

    if usuarios[id]["Clave"] == clave:
        return True
    else:
        return False
    

# Cambia la clave del usuario
def Cambio_clave(id,C_nueva, C_nueva_2):

    # Verifica que las dos claves nuevas coincidan
    if C_nueva == C_nueva_2:

        # Actualiza la clave en el diccionario
        usuarios[id]["Clave"] = C_nueva

        print("clave cambiada correctamente")

    else:

        print(ROJO+"Validacion incorrecta"+ROJO)


#---------------------------------------------------
#2. CONSULTA DE MOVIMIENTOS
#----------------------------------------------------

# Muestra el historial de movimientos del usuario
def Consulta_Movimientos(id):

    print(Fore.YELLOW + "\n===== HISTORIAL =====")

    # Recorre la lista de movimientos
    for operacion in usuarios[id]["movimientos"]:

        print(Fore.YELLOW + operacion)


#---------------------------------------------------
#3. PAGOS
#----------------------------------------------------

def pagos(id):

    # Menú de servicios a pagar
    print(MAGENTA+"1. Pagar Agua: "+MAGENTA)
    print(MAGENTA+"2. Pagar Luz: "+MAGENTA)
    print(MAGENTA+"3. Pagar Gas: "+MAGENTA)
    print(MAGENTA+"4. Regresar"+MAGENTA)

    opcion = input("elegir valor ")
    
    
    # ---------------- PAGO AGUA ----------------
    if opcion == "1":

        try:

            Valor = int(input("Coloque Valor a pagar: "))

            if Valor < 0:

                mensaje = ROJO+"Valor invalido"+ROJO
                return mensaje

            else:

                Resultado = usuarios[id]["saldo"] - Valor

                if Resultado < 0:

                    mensaje=ROJO+"Saldo insuficiente Para Hacer retiro"+ROJO
                    return mensaje

                else:

                    usuarios[id]["saldo"] = Resultado

                    mensaje = f"Este Es el nuevo Saldo {usuarios[id]['saldo']}"

                    # Guarda el movimiento
                    usuarios[id]["movimientos"].append(f"Pago de Agua: {Valor}")

                    return mensaje

        except:

            mensaje=ROJO+"Valor no valido"+ROJO
            return mensaje


    # ---------------- PAGO LUZ ----------------
    elif opcion == "2":

        try:

            Valor = int(input("Coloque Valor a pagar: "))

            if Valor < 0:

                mensaje = ROJO+"Valor invalido"+ROJO
                return mensaje

            else:

                Resultado = usuarios[id]["saldo"] - Valor

                if Resultado < 0:

                    mensaje = ROJO+"Saldo insuficiente Para Hacer retiro"+ROJO                    
                    return mensaje

                else:

                    usuarios[id]["saldo"] = Resultado

                    mensaje = f"Este Es el nuevo Saldo {usuarios[id]['saldo']}"

                    usuarios[id]["movimientos"].append(f"Pago de Luz: {Valor}")

                    return mensaje

        except:

            mensaje= ROJO+"Valor no valido"+ROJO
            return mensaje


    # ---------------- PAGO GAS ----------------
    elif opcion == "3":

        try:

            Valor = int(input("Coloque Valor a pagar: "))

            if Valor < 0:

                mensaje = ROJO+"Valor invalido"+ROJO
                return mensaje

            else:

                Resultado = usuarios[id]["saldo"] - Valor

                if Resultado < 0:

                    mensaje = ROJO+"Saldo insuficiente Para Hacer retiro"+ROJO                   
                    return mensaje

                else:

                    usuarios[id]["saldo"] = Resultado

                    mensaje = f"Este Es el nuevo Saldo {usuarios[id]['saldo']}"

                    usuarios[id]["movimientos"].append(f"Pago de Gas: {Valor}")

                    return mensaje

        except:

            mensaje= ROJO+"Valor no valido"+ROJO
            return mensaje


    # Regresar al menú
    elif opcion == "4":

        return False


    else:

        mensaje = "Opcion no valida"
        return mensaje
         


#--------------------------------------------------------------
# 4. OTRAS OPCIONES
#--------------------------------------------------------------

# Muestra los datos del usuario
def Mostrardatos(id):

    print(f"Este es el usuario: {usuarios[id]['nombre']}")
    print(f"Este es el  numero de Cuenta: {usuarios[id]['Numero_Cuenta']}")
    print(f"Este es el  Saldo: {usuarios[id]['saldo']}")
    print(f"Clave: {usuarios[id]['Clave']}")


# Permite actualizar datos del usuario
def ActualizarDatos(id):

    mensaje =""

    print("")
    print("Seleccione una Operacion")
    print("")                    

    print("1. Actualizar nombre")
    print("2. Actualizar Numero")
    print("3. Regresar")
    
    Menu_Actualizar=input(": ")

    # Cambiar nombre
    if Menu_Actualizar== "1":

        n_nombre = input("Colocar Nuevo Nombre: ")

        usuarios[id]["nombre"] = n_nombre

        mensaje = f"Tu nombre ahora es: {usuarios[id]['nombre']}"

        return mensaje


    # Cambiar número de cuenta
    elif Menu_Actualizar== "2":

        Confirmar = input("Despues de esta operacion se cambiara la clave, escriba [Y] para confirmar y [N] para no realizar la operacion: ")

        if Confirmar == "Y":

            numero = random.randint(1000000000, 9999999999)

            usuarios[id]["Numero_Cuenta"] = str(numero)

            mensaje = (f"{usuarios[id]['nombre']} Tu numero ahora es {usuarios[id]['Numero_Cuenta']}")

            return mensaje

        elif Confirmar == "N":

            mensaje = ("operacion Cancelada")

            return mensaje

        else:

            mensaje = ("Operacion No valida")

            return mensaje

    elif Menu_Actualizar== "3":

        return False

    else:

        mensaje = ("opcion no valida")

        return mensaje


#------------------------------------
# 5. RETIRO RAPIDO
#--------------------------------------

def retirar_Dinero_Rapido(id):

    # Opciones de retiro rápido
    print("Escoja el Monto a retirar")

    print("1. 20.000")
    print("2. 30.000")
    print("3. 50.000")
    print("4. 100.000")
    print("5. Regresar")

    mensaje = ""

    Valor = input("Seleccione Una Opcion: ")

    # Cada opción descuenta dinero del saldo
    # y guarda el movimiento

    if Valor == "1":

        Resultado = usuarios[id]["saldo"] - 20000

        if Resultado < 0:

            print(ROJO+"Saldo insuficiente Para Hacer retiro Rapido")

            return False

        else:

            usuarios[id]["saldo"] = Resultado

            mensaje = f"Este Es el nuevo Saldo {Resultado}"

            usuarios[id]["movimientos"].append(f"retiro: {20000}")

            return mensaje

    elif Valor == "5":

        # Regresar al menú anterior
        return False

    else:

        mensaje = "Opcion no valida"

        return mensaje


#-----------------------------------
#6. RETIRO PERSONALIZADO
#---------------------------------

def retiro(id):

    try:

        Valor = int(input("Coloque Valor a Retirar: "))

        # Validación de valores negativos
        if Valor < 0:

            mensaje = ROJO+"Valor invalido"+ROJO

            return mensaje

        else:

            # Límite máximo de retiro
            if Valor > 1000000:

                mensaje = ROJO + "No puede Hacer Retiros con Valores Mayores a un 1000000"+ROJO

                return mensaje

            else:

                Resultado = usuarios[id]["saldo"] - Valor

                if Resultado < 0:

                    print(ROJO+"Saldo insuficiente Para Hacer retiro"+ROJO)

                    return False

                else:

                    usuarios[id]["saldo"] = Resultado

                    mensaje = f"Este Es el nuevo Saldo {usuarios[id]['saldo']}"

                    usuarios[id]["movimientos"].append(f"retiro: {Valor}")

                    return mensaje

    except:

        mensaje =ROJO+"Valor no valido"+ROJO

        return mensaje


#-----------------------------------
#7. CONSULTAR SALDO
#--------------------------------------

def consultar_saldo(id):

    print(f"Este es el saldo {usuarios[id]['saldo']}")
    

#------------------------------------------
#8. TRANSFERENCIA
#---------------------------------------------

def transferencia(id):

    try:

        Valor = int(input("Coloque Valor a transferir: "))

        if Valor < 0:

            mensaje = ROJO+"Valor invalido"+ROJO

            return mensaje

        else:

            if Valor > 1000000:

                mensaje = ROJO + "No puede Hacer Transferencias con Valores Mayores a un 1000000"+ROJO

                return mensaje

            else:

                Resultado = usuarios[id]["saldo"] - Valor

                if Resultado < 0:

                    mensaje = ROJO+"Saldo insuficiente Para Hacer retiro"+ROJO               
                    return mensaje

                else:

                    # Solicita número de cuenta destino
                    numero_de_cuenta = input("coloque el numero de cuenta a Transferir: ")

                    id_transferir = Validacion_numero(numero_de_cuenta)

                    # Si la cuenta existe
                    if id_transferir:

                        usuarios[id]["saldo"] = Resultado

                        Resultado_2 = usuarios[id_transferir]["saldo"] + Valor

                        usuarios[id_transferir]["saldo"] = Resultado_2

                        mensaje = f"Transferencia exitosa"

                        # Guarda movimientos
                        usuarios[id]["movimientos"].append(f"Transferencia - Salida : {Valor}  :  {numero_de_cuenta} ")

                        usuarios[id_transferir]["movimientos"].append(f"Transferencia - Entrada : {Valor}  :  {usuarios[id]['Numero_Cuenta']} ")

                        return mensaje

                    else:

                        mensaje = f"El numero de cuenta {numero_de_cuenta} no esta Registrado en Nuestro Banco"

                        return mensaje

    except:

        mensaje = ROJO+"Valor no valido"+ROJO

        return mensaje


#------------------------------------------
#9. DEPOSITAR
#------------------------------------------

def Depositar(id):

    try:

        Valor = int(input("Coloque Valor a Depositar: "))

        if Valor < 0:

            mensaje = ROJO+"Valor invalido"+ROJO

            return mensaje

        else:

            if Valor > 1000000:

                mensaje = ROJO + "No puede Hacer Depositos con Valores Mayores a un 1000000"+ROJO

                return mensaje

            else:

                # Suma el dinero al saldo
                usuarios[id]["saldo"] = usuarios[id]["saldo"] + Valor

                return "Valor depositado Correctamente"

    except:

        mensaje = ROJO+"Valor no valido"+ROJO

        return mensaje