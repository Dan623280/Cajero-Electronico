from Dicionario import usuarios
import random
from colorama import init, Fore, Style
init(autoreset=True)
#--------------------------------
#Nombre
#------------------------------------
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

def Datos_user(id):
    datos = usuarios.get(id)
    return datos

#----------------------------------------------------
# 1. Gestion Clave
#--------------------------------------------------------------------

def Validacion_de_clave(id,clave):
    if usuarios[id]["Clave"] == clave:
        return True
    else:
        return False
    

def Cambio_clave(id,C_nueva, C_nueva_2):
    if C_nueva == C_nueva_2:
        usuarios[id]["Clave"] = C_nueva
        print("clave cambiada correctamente")
    else:
        print("Validacion incorrecta")
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
    print("1. Pagar Agua: ")
    print("2. Pagar Luz: ")
    print("3. Pagar Gas: ")
    print("4. Regresar")
    opcion = int(input("elegir valor "))
    
    
    
    if opcion == 1:
        Valor = int(input("Coloque Valor a pagar: "))
        Resultado = usuarios[id]["saldo"] - Valor
        if Resultado < 0:
            print("Saldo insuficiente Para Hacer retiro")
            return True
        else:
            usuarios[id]["saldo"] = Resultado
            mensaje = f"Este Es el nuevo Saldo {usuarios[id]["saldo"]}"
            usuarios[id]["movimientos"].append(f"Pago de Agua: {Valor}")
            return mensaje
    elif opcion == 2:
        Valor = int(input("Coloque Valor a pagar: "))
        Resultado = usuarios[id]["saldo"] - Valor
        if Resultado < 0:
            print("Saldo insuficiente Para Hacer retiro")
            return True
        else:
            usuarios[id]["saldo"] = Resultado
            mensaje = f"Este Es el nuevo Saldo {usuarios[id]["saldo"]}"
            usuarios[id]["movimientos"].append(f"Pago de Luz: {Valor}")
            return mensaje
    elif opcion == 3:
        Valor = int(input("Coloque Valor a pagar: "))
        Resultado = usuarios[id]["saldo"] - Valor
        if Resultado < 0:
            print("Saldo insuficiente Para Hacer retiro")
            return True
        else:
            usuarios[id]["saldo"] = Resultado
            mensaje = f"Este Es el nuevo Saldo {usuarios[id]["saldo"]}"
            usuarios[id]["movimientos"].append(f"Pago de Gas: {Valor}")
            return mensaje
    elif opcion == 4:
        return False
    else:
        mensaje = "Opcion no valida"
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
    print("Seleccione una Operacion")
    print("")                    
    print("1. Actualizar nombre")
    print("2. Actualizar Numero")
    print("3. Regresar")
    
    Menu_Actualizar=int(input(": "))
    if Menu_Actualizar== 1:
        n_nombre = input("Colocar Nuevo Nombre: ")
        usuarios[id]["nombre"] = n_nombre
        mensaje = f"Tu nombre ahora es: {usuarios[id]["nombre"]}"
        return mensaje
    elif Menu_Actualizar== 2:
        Confirmar = input("Despues de esta operacion se cambiara la clave, escriba [Y] para confirmar y [N] para no realizar la operacion: ")
        if Confirmar == "Y":
            numero = random.randint(1000000000, 9999999999)
            usuarios[id]["Numero_Cuenta"] = str(numero)
            mensaje = (f"{usuarios[id]["nombre"]} Tu numero ahora es {usuarios[id]["Numero_Cuenta"]}")
            return mensaje
        elif Confirmar == "N":
            mensaje = ("operacion Cancelada")
            return mensaje
        else:
            mensaje = ("Operacion No valida")
            return mensaje
    elif Menu_Actualizar== 3:
        return False
    else:
        mensaje = ("opcion no valida")
        return mensaje

#------------------------------------
# 5. Retiro rapido
#--------------------------------------

def retirar_Dinero_Rapido(id):
    print("Escoja el Monto a retirar")
    print("1. 20.000")
    print("2. 30.000")
    print("3. 50.000")
    print("4. 100.000")
    print("5. Regresar")
    mensaje = ""
    Valor = int(input("Seleccione Una Opcion: "))
    
    
    if Valor == 1:
        Resultado = usuarios[id]["saldo"] - 20000
        if Resultado < 0:
            print("Saldo insuficiente Para Hacer retiro Rapido")
            return False
        else:
            usuarios[id]["saldo"] = Resultado
            mensaje = f"Este Es el nuevo Saldo {Resultado}"
            usuarios[id]["movimientos"].append(f"retiro: {20000}")
            return mensaje
    elif Valor == 2:
        Resultado = usuarios[id]["saldo"] - 30000
        if Resultado < 0:
            print("Saldo insuficiente Para Hacer retiro Rapido")
            return False
        else:
            usuarios[id]["saldo"] = Resultado
            mensaje = f"Este Es el nuevo Saldo {Resultado}"
            usuarios[id]["movimientos"].append(f"retiro: {30000}")
            return mensaje
    elif Valor == 3:
        Resultado = usuarios[id]["saldo"] - 50000
        if Resultado < 0:
            print("Saldo insuficiente Para Hacer retiro Rapido")
            return False
        else:
            usuarios[id]["saldo"] = Resultado
            mensaje = f"Este Es el nuevo Saldo {Resultado}"
            usuarios[id]["movimientos"].append(f"retiro: {50000}")
            return mensaje
    elif Valor == 4:
        Resultado = usuarios[id]["saldo"] - 100000
        if Resultado < 0:
            print("Saldo insuficiente Para Hacer retiro Rapido")
            return False
        else:
            usuarios[id]["saldo"] = Resultado
            mensaje = f"Este Es el nuevo Saldo {Resultado}"
            usuarios[id]["movimientos"].append(f"retiro: {100000}")
            return mensaje
    elif Valor == 5:
        return False
    else:
        mensaje = "Opcion no valida"
        return mensaje
#-----------------------------------
#6. retiro
#---------------------------------

def retiro(id):
    Valor = int(input("Coloque Valor a Retirar: "))
    Resultado = usuarios[id]["saldo"] - Valor
    
    if Resultado < 0:
        print("Saldo insuficiente Para Hacer retiro")
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