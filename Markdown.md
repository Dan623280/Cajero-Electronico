## <font color="red">Documento del Sistema de Cajero Electronico</font>

#### Este proyecto es para simular un Cajero-Electronico tiene todas sus funciones como un cajero original

------------------------
## <font color="red">1. Importacion de funciones </font> 

Primero, el programa importa varias funciones desde un archivo llamado `funciones.py`. Estas funciones se encargan de realizar las operaciones del cajero.

        from funciones import retirar_Dinero_Rapido, Validacion_de_clave, Cambio_clave, Mostrardatos, ActualizarDatos,consultar_saldo, nombre_user, Consulta_Movimientos, retiro,pagos, transferencia, depositar

#### <font color="blue">Explicacion</font>

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

* Depositar:  depositar dinero.

-------------------------
## <font color="red">2. Variable global :rocket:</font>

    id_usuario_cajero = ""

#### <font color="blue">Explicacion</font>

Esta variable guarda el __*ID del usuario que esta usando el cajero.*__

---------------------------

## <font color="red">3. Funcion principal del Cajero :fire:</font> 

    def cajero(id_Usuario):

#### <font color="blue">Explicacion</font>

Esta funcion controla __todo el funcionamiento del cajereo automatico.__
Recibe como parametro el __ID del usuario que inicia sesion.__

----------------------

## <font color="red">4. Asignacion de datos del usuario</font> 

    id_usuario_cajero = id_Usuario
    nombre = nombre_user(id_Usuario)

#### <font color="blue">Explicacion</font>

* Se guarda el ID del usuario.
* Se obtiene el nombrwe del usuario para mostrarlo en pantalla.

---------------------

## <font color="red">5.Bucle principal de menu</font> 


    Confir_2 = True
    while Confir_2:

#### <font color="blue">Explicacion</font>

Este `while` mantiene el __cajero funcionando hasta que el usuario decida salir.__

---------------------

## <font color="red">6.Mostrar menu de opciones</font> 

    print (f"Bienvenido {nombre}") 
    print ("Selecciona una de las opciones")

Luego se muestran las opciones del cajero:

    1. Gestion de clave
    2. Consulta de movimientos
    3. Pagos
    4. Otras operaciones
    5. Retiro rápido
    6. Retiro
    7. Consulta saldo
    8. Transferencia
    9. Depositar
    10. Salir

El usuario selecciona una opcion:

    Pregunta_1 = int(input("¿Cual operaciones desea realizar el usuario?: "))

--------------------

## <font color="red">7.Gestion de clave</font> 

Si el usuario selecciona __opcion 1__:

    if pregunta_1 == 1:

#### <font color="green">Proceso</font> 
1. El usuario ingreso su clave.
2. El sistema la valida.
3. Si es correcta, puedo cambiarla.


        clave= input("clave: ")
        if Validacion_de_clave(id_usuario_cajero,clave):

## <font color="red">8.Consulta de movimientosG</font>   

Si el usuario elige lo la opcion __2:__ 

    elif Pregunta_1 == 2:
        Consulta_Movimientos(id_usuario_cajero)

#### <font color="blue">Explicacion</font> 
Muestra todas las transacciones realizadas en la cuenta.

--------------------

## <font color="red">9. Pagos</font>
Si el usuario selecciona la opcion __3__:

    elif pregunta_1  == 3:

Se ejecuta la funcion de pagos dentro de un bucle que permite repetir la operacion.

--------------------------

## <font color="red">10. Otras operaciones</font>
Si el usuario selecciona la opcion **4**, aparece un submenu:

    1. Mostrar datos del usuario
    2. Actualizar datos
    3. Regresar

#### Funciones disponibles
###### Mostrar datos

    Mostrardatos(id_usuario_cajero)

###### Actualizar datos

    ActualizarDatos(id_usuario_cajero)

## <font color="red">11. Retiro rapido</font> 
Si el usuario selecciona __opcion 5__:

    retirar_Dinero_Rapido(id_usuario_cajero)

Permite retirar dinero con montos predeterminados.

----------------------------

## <font color="red">12. Retiro normal</font> 
opcion __6__:

    retiro(id_usuario_cajero)

Permite retirar dinero ingresando manualmente el monto.

---------------------------

## <font color="red">13. Consulta de saldo</font>
Opcion __7__:

    consultar_saldo(id_usuario_cajero)

Muestra el saldo actual del usuario.

----------------------------

## <font color="red">14. Transferencias</font>
Opcion __8__:

    transferencia(id_usuario_cajero)

Permite enviar dinero a otra cuenta.

-----------------------------

## <font color="red">15. depositar</font>
Si el usuario selecciona __9__:

    Depositar(id_usuario_cajero)

Permite __agregar dinero a la cuenta__.

-------------------------------

## <font color="red">16. Salir del sistema</font>
Si el usuario selecciona __10__:

    elif Pregunta_1 == "10":


El sistema muestra un mensaje de despedida y termina el programa.

    Gracias por usar el cajero automático vuelva pronto

##### Luego termina el programa con:

    return False

##### Muestra:

    Opción No válida


## <font color="red">Como funciona todo el sistema</font>
### este es el Flujo completo:


    Login usuario
        ↓
    Se ejecuta cajero(id_usuario)
        ↓
    Se muestra el menú
        ↓
    Usuario elige opción
        ↓
    Se ejecuta función correspondiente
        ↓
    Regresa al menú
        ↓
    Hasta que el usuario presione 10



# ahora vamos con las funciones.
## tambien explicadas paso a paso

#### 1. Importaciones

    from Dicionario import usuarios
    import random
    from colorama import init, Fore, Style
    init(autoreset=True)

##### Que hace cada cosa:
__usuarios__

* importa el diccionario donde estan guardados todos los clientes.

__random__
* Se usa para generar numero aleatorios (nuevo numero de cuenta).

__colorama__

#### 2. Obtener nombre del usuario

    def nombre_user(id):
        nombre = usuarios[id]["nombre"]
        return nombre

##### Que hace
Busca el nombre del usuario usando su __ID__.

Ejemplo:

    nombre_user("1")

    Resultado:

    Juan

## 3.Validar numero de cuenta

    def Validacion_numero(N_cuenta):

Recorre todos los usuarios.

    for id, datos in usuarios.items():

Si encuentra el numero de cuenta:

    if datos["Numero_Cuenta"] == N_cuenta:
        return(id)

Devuelve el __ID del usuario__.
esto se usa para __transferencias__.

## 4. Obtener datos del usuario

    def Datos_user(id):
        datos = usuarios.get(id)
        return datos

Devuelve todos los datos del usuario.

Ejemplo:

    {
    nombre
    saldo
    numero cuenta
    clave
    movimientos
    }

## 5. Validar si el usuario esta activo

    def validar_user_activo(id):

Si el usuario esta acitvo 

    usuarios[id]["Validacion"] == "Activo"
    
    Devuelve:

    Activo

    Si no:

    Inactivo

-------------------------

## 6. Bloquear usuario 

    def bloquear(id):

Cambia el estado del usuario:

    usuarios[id]["Validacion"] = "Inactivo"

Luego devuelve:

    Usuario Bloqueado

--------------------------------

## 7. Validad clave

    def Validacion_de_clave(id,clave):

Compara la clave ingresada con la guardada.
Si coincide:

    True

Si no coincide:

    False

----------------------------

## 8. Cambiar clave

    def Cambio_clave(id,C_nueva, C_nueva_2):

Primero verifica si ambas claves son iguales.

    clave nueva
    confirmar clave

Si coinciden:

    se guarda la neva clave

Si no coinciden:

    Validacion incorrecta

------------------------------

## 9 Historial de movimientos

    def Consulta_Movimientos(id):

Imprime:

    ===== HISTORIAL =====

Luego recorre la lista:

    usuarios[id]["movimientos"]

Ejemplo de miviemientos:

    Pago de Agua: 20000
    retiro: 50000
    Transferencia: 30000

-------------------------

## 10. Pagos

    def pagos(id):

Muestra opciones:

    1 Agua
    2 Luz
    3 Gas
    4 Regresar

Luego pide el valor.

#### Validaciones

###### 1 valor negativo
    Valor invalido
###### 2 saldo insuficiente
    Saldo insuficiente
###### 3 pago exitoso
Actualiza saldo:

    saldo = saldo - valor

Guarda movimientos:

    Pago de Agua: 20000

-------------------------------

## 11. Mostrar datos del usuario

    def Mostrardatos(id):

Muestra: 

    nombre
    numero cuenta
    saldo
    clave

----------------------------

## 12. Actualizar datos

    def ActualizarDatos(id):

Opciones:

    1 cambiar nombre
    2 cambiar numero cuenta
    3 regresar

#### __Cambiar nombre__
Actualiza:

    usuarios[id]["nombre"]

-----------------------

#### __Cambia numero de cuenta__

Si confirma: 

    numero = random.randint(1000000000, 9999999999)

Genera un nuevo numero.

## 13. Retiro rapido 

    def retirar_Dinero_Rapido(id):

Si hay saldo suficiente:

    saldo = saldo - monto

Guarda movimiento:

    retiro: 20000

## 14. Retiro normal 

    def retiro(id):

El usuario escribe el monto.

Validaciones:

1️⃣ valor negativo
2️⃣ saldo insuficiente

Si todo esta bien:

    saldo = saldo - valor

movimiento guardado.

## 15. Consultar saldo

    def consultar_saldo(id):

Solo imprime:

    saldo actual

## 16. Tranferencia

    def transferencia(id):

Pasos:

1️⃣ usuario escribe monto

2️⃣ se valida saldo

3️⃣ pide número de cuenta destino

4️⃣ se valida la cuenta

    id_transferir = Validacion_numero(numero_de_cuenta)

5️⃣ si existe:

* resta saldo al emisor

* suma saldo al receptor

6️⃣ guarda movimientos

Salida:

    Transferencia - Salida
    Transferencia - Entrada

## 17. Depositar dinero 

    def Depositar(id):

Pide monto.

Si es valido:

    saldo = saldo + valor

Mensaje:

    valor depositado Correctamente

## <font color="red">🧠 Cómo funciona todo el sistema</font>

Este es el flujo:

    Login usuario
        ↓
    cajero()
        ↓
    menú
        ↓
    llama funciones
        ↓
    modifica usuarios


# Resumen del código main.py

Este programa controla el acceso seguro al cajero automático validando usuario y clave, y bloquea el usuario tras 3 intentos fallidos.

-------------------

### Paso a paso

## 1. Variables iniciales

* `autenticacion = True` — controla el ciclo principal para pedir usuario y clave.

* `id_Usuario = ""` — para guardar el identificador interno del usuario.

* `Contador = 0`— cuenta los intentos fallidos de contraseña.

## 2. Bucle principal (`while autenticacion`)

* Muestra el mensaje de bienvenida.

* Pide al usuario:

    * Número de usuario `(N_Usuario)`

    * Clave `(Clave)`

## 3. Validar número de usuario

Llama a `Validacion_numero(N_Usuario)` para obtener el `id` interno.

Si el número es válido, sigue, si no muestra “Usuario incorrecto”.

## 4. Verificar si el usuario está activo

* Llama a `validar_user_activo(id_Usuario)`.

* Si está “Activo” permite continuar.

* Si está “Inactivo” muestra mensaje de bloqueo.

## 5. Validar clave

* Llama a `Validacion_de_clave(id_Usuario, Clave)`.

* Si clave es correcta, entra al menú del cajero (`cajero(id_Usuario)`).

* Si clave es incorrecta:

  * Incrementa el contador de intentos fallidos.

  * Muestra mensaje “Clave incorrecta”.

  * Si se llega a 3 intentos, bloquea el usuario con `Bloquear(id_Usuario)`.

## 6. Dentro del menú del cajero

* Ejecuta la función `cajero(id_Usuario)`.

* Si la función devuelve `False` (usuario eligió salir), termina el ciclo del cajero y muestra “Salida Exitosa”.

* Si devuelve otro valor (mensaje), lo muestra.


En resumen de eso 

* _Pides usuario y clave._

* _Compruebas que el usuario exista y esté activo._

* _Verificas la clave._

* _Permites usar el cajero si todo está bien._

* _Bloqueas el usuario tras 3 fallos de clave._

* _Das mensajes claros para cada situación._