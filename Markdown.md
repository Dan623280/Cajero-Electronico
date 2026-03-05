# Documentacion del sistema de Cajero-Electronico 

## Proyecto de Cajero-Electronico 

Este proyecto es para simular un Cajero-Electronico tiene todas sus funciones
como un cajero original
------------------------
## 1. Importacion de funciones 

Primero, el programa importa varias funciones desde un archivo llamado `funciones.py`. Estas funciones se encargan de realizar las operaciones del cajero.

        from funciones import retirar_Dinero_Rapido, Validacion_de_clave, Cambio_clave, Mostrardatos, ActualizarDatos,consultar_saldo, nombre_user, Consulta_Movimientos, retiro,pagos, transferencia

#### Explicacion

* retirar_Dinero_Rapido: permite retirar dinero rápidamente.

* Validacion_de_clave: valida si la clave ingresada es correcta.

* Cambio_clave: permite cambiar la clave del usuario.

* Mostrardatos: muestra los datos del usuario.

* ActualizarDatos: permite modificar los datos del usuario.

* consultar_saldo: muestra el saldo de la cuenta.

* nombre_user: obtiene el nombre del usuario.

* Consulta_Movimientos: muestra los movimientos de la cuenta.

* retiro: permite retirar dinero manualmente.

* pagos: permite realizar pagos.

* transferencia: permite transferir dinero a otra cuenta.

-------------------------
## 2. Variable global :rocket:

    id_usuario_cajero = ""

#### Explicacion 

Esta variable guarda el __*ID del usuario que esta usando el cajero.*__

---------------------------

## 3. Funcion principal del Cajero :fire:

    def cajero(id_Usuario):

#### Explicacion 

Esta funcion controla __todo el funcionamiento del cajereo automatico.__
Recibe como parametro el __ID del usuario que inicia sesion.__

----------------------

## 4. Asignacion de datos del usuario

    id_usuario_cajero = id_Usuario
    nombre = nombre_user(id_Usuario)

#### Explicacion 

* Se guarda el ID del usuario.
* Se obtiene el nombrwe del usuario para mostrarlo en pantalla.

---------------------

## 5. Bucle principal de menu

    Confir_2 = True
    while Confir_2:
