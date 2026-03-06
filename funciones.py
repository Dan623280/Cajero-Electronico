from Dicionario import usuarios
import random
from colorama import init, Fore, Style
init(autoreset=True)
#--------------------------------
#Nombre
#------------------------------------
# RESET
RESET = "\033[0m"

# COLORES BÁSICOS
NEGRO = "\033[30m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BLANCO = "\033[37m"

# COLORES BRILLANTES
GRIS = "\033[90m"
ROJO_BRILLANTE = "\033[91m"
VERDE_BRILLANTE = "\033[92m"
AMARILLO_BRILLANTE = "\033[93m"
AZUL_BRILLANTE = "\033[94m"
MAGENTA_BRILLANTE = "\033[95m"
CYAN_BRILLANTE = "\033[96m"
BLANCO_BRILLANTE = "\033[97m"

# ESTILOS DE TEXTO
NEGRITA = "\033[1m"
SUBRAYADO = "\033[4m"
INVERTIDO = "\033[7m"

def nombre_user(id):
    
    nombre = usuarios[id]["nombre"]
    return nombre
#------------------------
#Validacion
#------------------------------
def Validacion_Usuario(N_Cuenta,Clave):
    for id, datos in usuarios.items():
        if datos["Numero_Cuenta"] == N_Cuenta and datos["Clave"] == Clave:
            return(id)
def Validacion_numero(N_cuenta):
    for id, datos in usuarios.items():
        if datos["Numero_Cuenta"] == N_cuenta:
            return(id)

def Datos_user(id):
    datos = usuarios.get(id)
    return datos

#----------------------------------------------------
# 1. Gestion Clave
#--------------------------------------------------------------------

def Validacion_de_clave(id,clave):
    if usuarios[id][AMARILLO_BRILLANTE+"Clave"+RESET] == clave:
        return True
    else:
        return False
    

def Cambio_clave(id,C_nueva, C_nueva_2):
    if C_nueva == C_nueva_2:
        usuarios[id]["Clave"] = C_nueva
        print(VERDE+"¡clave cambiada correctamente!"+VERDE)
    else:
        print(ROJO+"Validacion incorrecta"+ROJO)
#---------------------------------------------------
#2. Consulta de movimientos
#----------------------------------------------------

def Consulta_Movimientos(id):
    print(Fore.YELLOW + "\n===== HISTORIAL =====")
    for operacion in usuarios[id]["movimientos"]:
        print(Fore.YELLOW + operacion)

#---------------------------------------------------
#3. Pagos
#----------------------------------------------------

def pagos(id):
    print(MAGENTA+"1. Pagar Agua: "+MAGENTA)
    print(MAGENTA+"2. Pagar Luz: "+MAGENTA)
    print(MAGENTA+"3. Pagar Gas: "+MAGENTA)
    print(MAGENTA+"4. Regresar"+MAGENTA)
    opcion = int(input(MAGENTA+"elegir valor: "+MAGENTA))
    
    if opcion == 1:
        Valor = int(input(AZUL+"Coloque Valor a pagar: "+AZUL))
        Resultado = usuarios[id]["saldo"] - Valor
        if Resultado < 0:
            mensaje=AMARILLO+"Saldo insuficiente Para Hacer retiro"+AMARILLO
            return mensaje
        else:
            usuarios[id]["saldo"] = Resultado
            mensaje = f"Este Es el nuevo Saldo {usuarios[id]["saldo"]}"
            usuarios[id]["movimientos"].append(f"Pago de Agua: {Valor}")
            return mensaje
    elif opcion == 2:
        Valor = int(input(AZUL+"Coloque Valor a pagar: "+AZUL))
        Resultado = usuarios[id]["saldo"] - Valor
        if Resultado < 0:
            mensaje=ROJO+"Saldo insuficiente Para Hacer retiro"+ROJO
            return mensaje
        else:
            usuarios[id]["saldo"] = Resultado
            mensaje = f"Este Es el nuevo Saldo {usuarios[id]["saldo"]}"
            usuarios[id]["movimientos"].append(f"Pago de Luz: {Valor}")
            return mensaje
    elif opcion == 3:
        Valor = int(input(AZUL+"Coloque Valor a pagar: "+AZUL))
        Resultado = usuarios[id]["saldo"] - Valor
        if Resultado < 0:
            mensaje=AMARILLO+"Saldo insuficiente Para Hacer retiro"+AMARILLO
            return mensaje
        else:
            usuarios[id]["saldo"] = Resultado
            mensaje = f"Este Es el nuevo Saldo {usuarios[id]["saldo"]}"
            usuarios[id]["movimientos"].append(f"Pago de Gas: {Valor}")
            return mensaje
    elif opcion == 4:
        return False
    else:
        mensaje =AMARILLO+"Opcion no valida"+AMARILLO
        return mensaje
         
#----------------------------------------------------------------
# 4. Otras Opciones
#--------------------------------------------------------------
def Mostrardatos(id):
    print(f"Este es el usuario: {usuarios[id]["nombre"]}")
    print(f"Este es el  numero de Cuenta: {usuarios[id]["Numero_Cuenta"]}")
    print(f"Este es el  Saldo: {usuarios[id]["saldo"]}")
    print(f"Clave: {usuarios[id]["Clave"]}")

def ActualizarDatos(id):
    mensaje =""
    print("")
    print(AZUL+"Seleccione una Operacion"+AZUL)
    print("")                    
    print(AMARILLO+"1. Actualizar nombre"+AMARILLO)
    print(AMARILLO+"2. Actualizar Numero"+AMARILLO)
    print(AMARILLO+"3. Regresar"+AMARILLO)
    
    Menu_Actualizar=int(input(": "))
    if Menu_Actualizar== 1:
        n_nombre = input(AMARILLO+"Colocar Nuevo Nombre: "+AMARILLO)
        usuarios[id]["nombre"] = n_nombre
        mensaje = f"Tu nombre ahora es: {usuarios[id]["nombre"]}"
        return mensaje
    elif Menu_Actualizar== 2:
        Confirmar = input(AZUL+"Despues de esta operacion se cambiara la clave, escriba [Y] para confirmar y [N] para no realizar la operacion: "+AZUL)
        if Confirmar == "Y":
            numero = random.randint(1000000000, 9999999999)
            usuarios[id]["Numero_Cuenta"] = str(numero)
            mensaje = (f"{usuarios[id]["nombre"]} Tu numero ahora es {usuarios[id]["Numero_Cuenta"]}")
            return mensaje
        elif Confirmar == "N":
            mensaje = (ROJO+"operacion Cancelada"+ROJO)
            return mensaje
        else:
            mensaje = (ROJO+"Operacion No valida"+ROJO)
            return mensaje
    elif Menu_Actualizar== 3:
        return False
    else:
        mensaje = (ROJO+"opcion no valida"+ROJO)
        return mensaje

#------------------------------------
# 5. Retiro rapido
#--------------------------------------

def retirar_Dinero_Rapido(id):
    print(AZUL+"Escoja el Monto a retirar"+AZUL)
    print("1. 20.000")
    print("2. 30.000")
    print("3. 50.000")
    print("4. 100.000")
    print("5. Regresar")
    mensaje = ""
    Valor = int(input(AZUL+"Seleccione Una Opcion: "+AZUL))
    
    if Valor == 1:
        Resultado = usuarios[id]["saldo"] - 20000
        if Resultado < 0:
            print(ROJO+"Saldo insuficiente Para Hacer retiro Rapido"+ROJO)
            return False
        else:
            usuarios[id]["saldo"] = Resultado
            mensaje = f"Este Es el nuevo Saldo {Resultado}"
            usuarios[id]["movimientos"].append(f"retiro: {20000}")
            return mensaje
    elif Valor == 2:
        Resultado = usuarios[id]["saldo"] - 30000
        if Resultado < 0:
            print(AMARILLO+"Saldo insuficiente Para Hacer retiro Rapido"+AMARILLO)
            return False
        else:
            usuarios[id]["saldo"] = Resultado
            mensaje = f"{AMARILLO}Este Es el nuevo Saldo {Resultado}{RESET}"
            usuarios[id]["movimientos"].append(f"retiro: {30000}")
            return mensaje
    elif Valor == 3:
        Resultado = usuarios[id]["saldo"] - 50000
        if Resultado < 0:
            print(AMARILLO+"Saldo insuficiente Para Hacer retiro Rapido"+AMARILLO)
            return False
        else:
            usuarios[id]["saldo"] = Resultado
            mensaje = f"{AMARILLO}Este Es el nuevo Saldo {Resultado}{RESET}"
            usuarios[id]["movimientos"].append(f"retiro: {50000}")
            return mensaje
    elif Valor == 4:
        Resultado = usuarios[id]["saldo"] - 100000
        if Resultado < 0:
            print(AMARILLO+"Saldo insuficiente Para Hacer retiro Rapido"+AMARILLO)
            return False
        else:
            usuarios[id]["saldo"] = Resultado
            mensaje = f"Este Es el nuevo Saldo {Resultado}"
            usuarios[id]["movimientos"].append(f"retiro: {100000}")
            return mensaje
    elif Valor == 5:
        return False
    else:
        mensaje = ROJO+"Opcion no valida"+ROJO
        return mensaje
#-----------------------------------
#6. retiro
#---------------------------------

def retiro(id):
    Valor = int(input(AZUL+"Coloque Valor a Retirar: "+AZUL))
    Resultado = usuarios[id]["saldo"] - Valor
    
    if Resultado < 0:
        print(AMARILLO+"Saldo insuficiente Para Hacer retiro"+AMARILLO)
        return False
    else:
        usuarios[id]["saldo"] = Resultado
        mensaje = f"Este Es el nuevo Saldo {usuarios[id]["saldo"]}"
        usuarios[id]["movimientos"].append(f"retiro: {Valor}")
        return mensaje

#-----------------------------------
#7. Comsultar saldo
#--------------------------------------

def consultar_saldo(id):
    print(f"Este es el saldo {usuarios[id]["saldo"]}")
    
#------------------------------------------
#8. Transferencia
#---------------------------------------------

def transferencia(id):
    Valor = int(input(AZUL+"Coloque Valor a transferir: "+AZUL))
    Resultado = usuarios[id]["saldo"] - Valor
    if Resultado < 0:
        mensaje=ROJO+"Saldo insuficiente Para Hacer retiro" +ROJO
        return mensaje
    else:
        numero_de_cuenta = input(AZUL+"coloque el numero de cuenta a Transferir: "+AZUL)
        id_transferir = Validacion_numero(numero_de_cuenta)
        if id_transferir:
            usuarios[id]["saldo"] = Resultado
            Resultado_2 = usuarios[id_transferir]["saldo"] + Valor
            usuarios[id_transferir]["saldo"] = Resultado_2
            mensaje = f"{VERDE}¡Transferencia exitosa!{RESET}"
            usuarios[id]["movimientos"].append(f"Transferencia - Salida : {Valor}  :  {numero_de_cuenta} ")
            usuarios[id_transferir]["movimientos"].append(f"Transferencia - Entrada : {Valor}  :  {usuarios[id]["Numero_Cuenta"]} ")
            return mensaje
