from funciones import retirar_Dinero_Rapido, Datos_user, Validacion_de_clave, Cambio_clave, Mostrardatos, ActualizarDatos,consultar_saldo, nombre_user, Consulta_Movimientos
id_usuario_cajero = ""

def cajero(id_Usuario):
    id_usuario_cajero = id_Usuario
    nombre = nombre_user(id_Usuario)
    Confir_2 = True
    while Confir_2:
            
            #Menu
            print(f"""
                Bienvenido {nombre} 
                Selecciona una de las opciones
                
                1. Gestion de clave 
                2. Consulta de movimientos 
                3. pagos 
                4. otras operaciones 
                5. Retiro rapido cuenta principal 
                6. Retiro 
                7. Consulta Saldo
                8. transferencio
                9. Salir

            """)
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
                                print (Var_actualizar)
                                confir_Menu = True
                            else:
                                confir_Menu = False
                    elif Menu_otrasope == 3:
                        confir_otras_ope = False
                    else:
                        print("Opcion no valida")
                        
                    
            elif Pregunta_1 == 5:
                confir_retirar = True
                while confir_retirar:
                    var_retirar = retirar_Dinero_Rapido(id_usuario_cajero)
                    if var_retirar:
                        print(var_retirar)
                        confir_retirar = True
                    else:
                        confir_retirar = False
            elif Pregunta_1 == 7:
                consultar_saldo(id_usuario_cajero)
            elif Pregunta_1 == 9:
                Confir_2 = False      
            else:
                print("""
                    Opción No válida
                    """)

cajero("1001")