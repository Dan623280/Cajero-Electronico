from funciones import retirar_Dinero, Datos_user, Validacion_de_clave, Cambio_clave, Mostrardatos
id_usuario_cajero = ""

def cajero(id_Usuario):
    id_usuario_cajero = id_Usuario
    Datos = Datos_user(id_usuario_cajero)
    S_inicial = Datos.get("saldo")
    while True:
            Confir_2 = True
            #Menu
            print(f"""
                Bienvenido {Datos.get("nombre")} 
                Selecciona una de las opciones
                
                1. Gestion de clave 
                2. Consulta de movimientos 
                3. pagos 
                4. otras operaciones 
                5. Retiro rapido cuenta principal 
                6. Retiro 
                7. Consulta 
                8. transferencio
                9. Salir

            """)
            Pregunta_1 = float(input("¿Cual operaciones desea realizar el usuario?: "))

            if Pregunta_1 == 1:
                clave= input("clave: ")
                if Validacion_de_clave(id_usuario_cajero,clave):
                    clave_Nueva = input("Colocar clave: ")
                    clave_Nueva_2 = input("Colocar clave: ")
                    Cambio_clave(id_usuario_cajero,clave_Nueva, clave_Nueva_2)
                else:
                    print("clave incorrecta")        
            elif Pregunta_1 == 4:
                confir_otras_ope = True
                while confir_otras_ope:
                    Menu_otrasope =int(input("""
                    1. Mostrar datos Usuario
                    2. Actualizar datos
                    3. Devolver
                    """))
                    if Menu_otrasope == 1:
                        Mostrardatos(id_usuario_cajero)
                    elif Menu_otrasope == 2:
                        
                    

            elif Pregunta_1 == 7:
                print(f"El Saldo Actual es: {S_inicial}")       
            else:
                print("""
                    Opción No válida
                    """)
