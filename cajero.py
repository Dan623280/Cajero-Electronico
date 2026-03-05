from funciones import retirar_Dinero_Rapido, Validacion_de_clave, Cambio_clave, Mostrardatos, ActualizarDatos,consultar_saldo, nombre_user, Consulta_Movimientos, retiro,pagos, transferencia
id_usuario_cajero = ""

def cajero(id_Usuario):
    id_usuario_cajero = id_Usuario
    nombre = nombre_user(id_Usuario)
    Confir_2 = True
    while Confir_2:
            #Menu
            print("")
            print (f"Bienvenido {nombre}") 
            print ("Selecciona una de las opciones")
            print ("")
            print ("1. Gestion de clave               5. Retiro rapido cuenta principal") 
            print ("2. Consulta de movimientos        6. Retiro")
            print ("3. pagos                          7. Consulta Saldo")
            print ("4. otras operaciones              8. transferencia")
            print ("9. Salir")
            print("")
            Pregunta_1 = float(input("¿Cual operaciones desea realizar el usuario?: "))

            if Pregunta_1 == 1:
                clave= input("clave: ")
                if Validacion_de_clave(id_usuario_cajero,clave):
                    clave_Nueva = input("Clave nueva: ")
                    clave_Nueva_2 = input("Confirmar clave: ")
                    Cambio_clave(id_usuario_cajero,clave_Nueva, clave_Nueva_2)
                else:
                    print("clave incorrecta")   
            elif Pregunta_1 == 2:
                Consulta_Movimientos(id_usuario_cajero)
            elif Pregunta_1 == 3:
                confir_pagos = True
                while confir_pagos:
                    var_pagos = pagos(id_usuario_cajero)
                    if var_pagos:
                        print("")
                        print(var_pagos)
                        print("")
                        confir_pagos = True
                    else:
                        confir_pagos = False
            elif Pregunta_1 == 4:
                confir_otras_ope = True
                while confir_otras_ope:
                    
                    print("1. Mostrar datos Usuario")                    
                    print("2. Actualizar datos")
                    print("3. Regresar")
                    
                    Menu_otrasope =int(input(": "))
                    if Menu_otrasope == 1:
                        Mostrardatos(id_usuario_cajero)
                    elif Menu_otrasope == 2:
                        confir_Menu = True
                        while confir_Menu:
                            Var_actualizar = ActualizarDatos(id_usuario_cajero)
                            
                            if  Var_actualizar:
                                print("")
                                print (Var_actualizar)
                                print("")
                                confir_Menu = True
                            else:
                                confir_Menu = False
                    elif Menu_otrasope == 3:
                        confir_otras_ope = False
                    else:
                        print("Opcion no valida")
                        
                    
            elif Pregunta_1 == 5:
                confir_retirar_rapido = True
                while confir_retirar_rapido:
                    var_retirar_rapido = retirar_Dinero_Rapido(id_usuario_cajero)
                    if var_retirar_rapido:
                        print("")
                        print(var_retirar_rapido)
                        print("")
                        confir_retirar_rapido = True
                    else:
                        confir_retirar_rapido = False
            elif Pregunta_1 == 6:
                confir_retiro = True
                while confir_retiro:
                    var_retiro = retiro(id_usuario_cajero)
                    if var_retiro:
                        print("")
                        print(var_retiro)
                        print("")
                        confir_retiro = False
                    else:
                        confir_retiro = False
            elif Pregunta_1 == 7:
                consultar_saldo(id_usuario_cajero)
            elif Pregunta_1 == 8:
                confir_transfer = True
                while confir_transfer:
                    var_transferencia = transferencia(id_usuario_cajero)
                    if var_transferencia:
                        print("")
                        print(var_transferencia)
                        print("")
                        confir_transfer = False
                    else:
                        confir_transfer = False
            elif Pregunta_1 == 9:
                print("===================================================")
                print("Gracias por usar el cajero automatio vuelva pronto ")
                print("===================================================")
                return False
            else:
                print("""
                    Opción No válida
                    """)
