from funciones import retirar_Dinero_Rapido, Validacion_de_clave, Cambio_clave, Mostrardatos, ActualizarDatos,consultar_saldo, nombre_user, Consulta_Movimientos, retiro,pagos, transferencia, Depositar
from Colores import RESET, NEGRO,ROJO,VERDE, AMARILLO, AZUL, MAGENTA, CYAN, BLANCO, GRIS, ROJO_BRILLANTE, VERDE_BRILLANTE,AMARILLO_BRILLANTE,AZUL_BRILLANTE,MAGENTA_BRILLANTE,CYAN_BRILLANTE,BLANCO_BRILLANTE,NEGRITA,SUBRAYADO,INVERTIDO

id_usuario_cajero = ""

def cajero(id_Usuario):
    id_usuario_cajero = id_Usuario
    nombre = nombre_user(id_Usuario)
    Confir_2 = True
    while Confir_2:
            #Menu
            print("")
            print (VERDE+f"Bienvenido {nombre}"+VERDE) 
            print (AZUL+"Selecciona una de las opciones"+AZUL)
            print ("")
            print ("1. Gestion de clave               5. Retiro rapido cuenta principal") 
            print ("2. Consulta de movimientos        6. Retiro")
            print ("3. pagos                          7. Consulta Saldo")
            print ("4. otras operaciones              8. transferencia")
            print ("9. Depositar                      10. Salir")
            print("")
            Pregunta_1 = input(AZUL+"¿Cual operaciones desea realizar el usuario?: "+AZUL)

            if Pregunta_1 == "1":
                clave= input(AMARILLO+"clave: "+AMARILLO)
                if Validacion_de_clave(id_usuario_cajero,clave):
                    clave_Nueva = input(AZUL+"Clave nueva: "+AZUL)
                    clave_Nueva_2 = input(AZUL+"Confirmar clave: "+AZUL)
                    Cambio_clave(id_usuario_cajero,clave_Nueva, clave_Nueva_2)
                else:
                    print(ROJO+"clave incorrecta"+ROJO)   

            elif Pregunta_1 == "2":
                Consulta_Movimientos(id_usuario_cajero)
            elif Pregunta_1 == "3":
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
            elif Pregunta_1 == "4":
                confir_otras_ope = True
                while confir_otras_ope:
                    
                    print(AZUL+"1. Mostrar datos Usuario"+AZUL)                    
                    print(AZUL+"2. Actualizar datos"+AZUL)
                    print(AZUL+"3. Regresar"+AZUL)
                    
                    Menu_otrasope =input(": ")
                    if Menu_otrasope == "1":
                        Mostrardatos(id_usuario_cajero)
                    elif Menu_otrasope == "2":
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
                    elif Menu_otrasope == "3":
                        confir_otras_ope = False
                    else:
                        print(ROJO+"Opcion no valida"+ROJO)
                        
                    
            elif Pregunta_1 == "5":
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
            elif Pregunta_1 == "6":
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
            elif Pregunta_1 == "7":
                print("")
                consultar_saldo(id_usuario_cajero)
                print("")
            elif Pregunta_1 == "8":
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
            elif Pregunta_1 == "9":
                print("")
                print(Depositar(id_usuario_cajero))
                print("")
            elif Pregunta_1 == "10":
                
                print(ROJO+"===================================================="+ROJO)
                print(ROJO+"=Gracias por usar el cajero automatio vuelva pronto="+ROJO)
                print(ROJO+"===================================================="+ROJO)
                return False
            else:
                print(ROJO+"=================="+ROJO)
                print(ROJO+"=Opción No válida="+ROJO)
                print(ROJO+"=================="+ROJO)
