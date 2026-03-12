# Importación de funciones necesarias desde el archivo funciones.py
from funciones import retirar_Dinero_Rapido, Validacion_de_clave, Cambio_clave, Mostrardatos, ActualizarDatos,consultar_saldo, nombre_user, Consulta_Movimientos, retiro,pagos, transferencia, Depositar

# Importación de constantes de colores para imprimir texto con estilo en consola
from Colores import RESET, NEGRO,ROJO,VERDE, AMARILLO, AZUL, MAGENTA, CYAN, BLANCO, GRIS, ROJO_BRILLANTE, VERDE_BRILLANTE,AMARILLO_BRILLANTE,AZUL_BRILLANTE,MAGENTA_BRILLANTE,CYAN_BRILLANTE,BLANCO_BRILLANTE,NEGRITA,SUBRAYADO,INVERTIDO

# Variable global que guardará el id del usuario que usa el cajero
id_usuario_cajero = ""

# Función principal del cajero
def cajero(id_Usuario):

    # Se guarda el id del usuario recibido en la variable del cajero
    id_usuario_cajero = id_Usuario

    # Se obtiene el nombre del usuario usando la función nombre_user
    nombre = nombre_user(id_Usuario)

    # Variable de control para mantener activo el menú del cajero
    Confir_2 = True

    # Bucle principal del cajero
    while Confir_2:

            # Espacio en pantalla
            print("")

            # Mensaje de bienvenida con el nombre del usuario
            print (VERDE+f"Bienvenido {nombre}"+VERDE)

            # Texto del menú
            print (AZUL+"Selecciona una de las opciones"+AZUL)
            print("")

            # Opciones disponibles en el cajero
            print ("1. Gestion de clave               5. Retiro rapido cuenta principal") 
            print ("2. Consulta de movimientos        6. Retiro")
            print ("3. pagos                          7. Consulta Saldo")
            print ("4. otras operaciones              8. transferencia")
            print ("9. Depositar                      10. Salir")
            print("")

            # Se pide al usuario seleccionar una opción
            Pregunta_1 = input(AZUL+"¿Cual operaciones desea realizar el usuario?: "+AZUL)

            # =========================
            # OPCION 1 - CAMBIO DE CLAVE
            # =========================
            if Pregunta_1 == "1":

                # Solicita la clave actual
                clave= input(AMARILLO+"clave: "+AMARILLO)

                # Verifica si la clave es correcta
                if Validacion_de_clave(id_usuario_cajero,clave):

                    # Solicita nueva clave
                    clave_Nueva = input(AZUL+"Clave nueva: "+AZUL)

                    # Confirmación de nueva clave
                    clave_Nueva_2 = input(AZUL+"Confirmar clave: "+AZUL)

                    # Llama a la función para cambiar la clave
                    Cambio_clave(id_usuario_cajero,clave_Nueva, clave_Nueva_2)

                else:
                    # Mensaje si la clave es incorrecta
                    print(ROJO+"clave incorrecta"+ROJO)

            # =========================
            # OPCION 2 - CONSULTAR MOVIMIENTOS
            # =========================
            elif Pregunta_1 == "2":
                Consulta_Movimientos(id_usuario_cajero)

            # =========================
            # OPCION 3 - PAGOS
            # =========================
            elif Pregunta_1 == "3":

                confir_pagos = True

                while confir_pagos:

                    # Llama a la función pagos
                    var_pagos = pagos(id_usuario_cajero)

                    # Si la función devuelve algo lo imprime
                    if var_pagos:
                        print("")
                        print(var_pagos)
                        print("")
                        confir_pagos = True
                    else:
                        # Si devuelve False sale del bucle
                        confir_pagos = False

            # =========================
            # OPCION 4 - OTRAS OPERACIONES
            # =========================
            elif Pregunta_1 == "4":

                confir_otras_ope = True

                while confir_otras_ope:

                    # Submenú
                    print(AZUL+"1. Mostrar datos Usuario"+AZUL)                    
                    print(AZUL+"2. Actualizar datos"+AZUL)
                    print(AZUL+"3. Regresar"+AZUL)

                    Menu_otrasope =input(": ")

                    # Mostrar datos del usuario
                    if Menu_otrasope == "1":
                        Mostrardatos(id_usuario_cajero)

                    # Actualizar datos
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

                    # Regresar al menú principal
                    elif Menu_otrasope == "3":
                        confir_otras_ope = False

                    else:
                        print(ROJO+"Opcion no valida"+ROJO)

            # =========================
            # OPCION 5 - RETIRO RAPIDO
            # =========================
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

            # =========================
            # OPCION 6 - RETIRO NORMAL
            # =========================
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

            # =========================
            # OPCION 7 - CONSULTAR SALDO
            # =========================
            elif Pregunta_1 == "7":

                print("")
                consultar_saldo(id_usuario_cajero)
                print("")

            # =========================
            # OPCION 8 - TRANSFERENCIA
            # =========================
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

            # =========================
            # OPCION 9 - DEPOSITAR
            # =========================
            elif Pregunta_1 == "9":

                print("")
                print(Depositar(id_usuario_cajero))
                print("")

            # =========================
            # OPCION 10 - SALIR DEL CAJERO
            # =========================
            elif Pregunta_1 == "10":

                print(ROJO+"===================================================="+ROJO)
                print(ROJO+"=Gracias por usar el cajero automatio vuelva pronto="+ROJO)
                print(ROJO+"===================================================="+ROJO)

                # Sale de la función cajero
                return False

            # =========================
            # OPCION INVALIDA
            # =========================
            else:

                print(ROJO+"=================="+ROJO)
                print(ROJO+"=Opción No válida="+ROJO)
                print(ROJO+"=================="+ROJO)