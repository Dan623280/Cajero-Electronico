from Dicionario import usuarios

def Validacion_Usuario(N_Cuenta,Clave):
    for id, datos in usuarios.items():
        if datos["Numero_Cuenta"] == N_Cuenta and datos["Clave"] == Clave:
            return(id)


def retirar_Dinero(S_inicial, monto_Reitrar):
    print("Saldo retirado")
    print("")
    S_inicial = S_inicial - monto_Reitrar 
    
    print(f"Este es el nuevo saldo: {S_inicial}")
    return S_inicial
