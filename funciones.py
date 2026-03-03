from Dicionario import usuarios

def Validacion_Usuario(N_Cuenta,Clave):
    for id, datos in usuarios.items():
        if datos["Numero_Cuenta"] == N_Cuenta and datos["Clave"] == Clave:
            return(id)

def Datos_user(id):
    datos = usuarios.get(id)
    return datos

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

#----------------------------------------------------------------

def Mostrardatos(id):
    print(f"Este es el usuario: {usuarios[id]["nombre"]}")
    print(f"Este es el  numero de Cuenta: {usuarios[id]["Numero_Cuenta"]}")


def ActualizarDatos(id):






def retirar_Dinero(S_inicial, monto_Reitrar):
    print("Saldo retirado")
    print("")
    S_inicial = S_inicial - monto_Reitrar 
    
    print(f"Este es el nuevo saldo: {S_inicial}")
    return S_inicial

