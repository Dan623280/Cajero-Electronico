from funciones import retirar_Dinero
S_inicial = 0
moviientos = list
def cajero():
    
    while True:
            Confir_2 = True
            #mENU
            print("""
                Menu
                1.  Consultar Saldo
                2.  Retirar Dinero
                3.  Depósitar Dinero
                4.  Gestion de clave
                5.  Consulta de movimientos
                6.  pagos
                7.  otras operaciones
                8.  retiro
                9.  transferir
            """)
            Pregunta_1 = float(input("¿Cual operaciones desea realizar el usuario?: "))

            if Pregunta_1 == 1:

                print(f"El Saldo Actual es: {S_inicial}")
            elif Pregunta_1 == 2:
                if S_inicial == 0:
                    Confir_2 = False
                    print("No puede realizar operacion")
                else:
                    Confir_2 = True
                while Confir_2:
                    monto_Reitrar = float(input("Coloque el monto a retirar: "))
                    if monto_Reitrar > S_inicial:
                        print("Fondos insuficientes")
                    elif monto_Reitrar <= S_inicial:
                        S_inicial=retirar_Dinero(S_inicial, monto_Reitrar)
                        Confir_2 = False
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

            elif Pregunta_1 == 4:
                print("escriba que quiere hacer")
                print("1. Cambiar Clave")
                clave = input("colocar clave")
                
                        
            else:
                print("""
                    Opción inválida
                    """)