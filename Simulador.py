
S_inicial = 0

Veces = int(input("Cuantas veces quieres realizar esta operacion"))
contador = 0

while contador < Veces:
    Confir_2 = True
    print("""

        Menu

        1.  Consultar Saldo
        2.  Retirar Dinero
        3.  Depósitar Dinero

    """)
    Pregunta_1 = float(input("¿Cuales operaciones desea realizar el usuario?: "))

    if Pregunta_1 == 1:

        print(f"El Saldo Actual es: {S_inicial}")
        contador = contador + 1
    elif Pregunta_1 == 2:
        while Confir_2:
            monto_Reitrar = float(input("Coloque el monto a retirar: "))
            if monto_Reitrar > S_inicial:
                print("Fondos insuficientes")
            elif monto_Reitrar <= S_inicial:
                print("Saldo retirado")
                print("")
                S_inicial = S_inicial - monto_Reitrar 
                print(f"Este es el nuevo saldo: {S_inicial}")
                Confir_2 = False
                contador = contador + 1
            else:
                print("monto no valido Coloquelo de Nuevo")
    elif Pregunta_1 == 3:
        while Confir_2:
            Monto_Depositar = int(input("Colocar monto a depositar: "))
            if Monto_Depositar == False:
                print("Monto Negativo Coloquelo de Nuevo")
            else:
                S_inicial = S_inicial+Monto_Depositar
                print(f"Saldo Depositado Correctamente, Este es el Nuevo Saldo {S_inicial}")
                Confir_2 = False
                contador = contador + 1
    else:
        print("""
              Opción inválida
              """)
        
if contador < Veces:
    print("Gracias por usar el cajero automático")
else:
    print("Hubo un error")