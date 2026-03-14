# Cajero Electrónico - TechBank Riwi Digital

Este proyecto es una simulación de un **Cajero Automático (ATM)**
desarrollado en Python que funciona completamente desde la terminal.

La aplicación permite a los usuarios iniciar sesión con su **número de
cuenta y clave**, y realizar diferentes operaciones bancarias como:

-   Consultar saldo
-   Retirar dinero
-   Retiro rápido
-   Depositar dinero
-   Transferir dinero a otras cuentas
-   Pagar servicios (agua, luz o gas)
-   Consultar historial de movimientos
-   Cambiar su clave
-   Actualizar sus datos

El objetivo del programa es simular el funcionamiento básico de un
cajero automático desde la consola.

------------------------------------------------------------------------

# Ubicación del repositorio

El proyecto se encuentra en el siguiente repositorio de GitHub:

https://github.com/Dan623280/Cajero-Electronico

------------------------------------------------------------------------

# Cómo clonar el repositorio

Para descargar el proyecto en tu computador debes abrir la terminal y
ejecutar:

``` bash
git clone https://github.com/Dan623280/Cajero-Electronico.git
```

Luego entra a la carpeta del proyecto:

``` bash
cd Cajero-Electronico
```

------------------------------------------------------------------------

# Cómo ejecutar el programa

El archivo principal del programa es:

    main.py

Para ejecutar el cajero automático usa:

``` bash
python main.py
```

------------------------------------------------------------------------

# Usuarios para iniciar sesión

Puedes usar cualquiera de estos usuarios:

  Numero de cuenta   Clave
  ------------------ -------
  3224716782         1234
  3005716782         5678
  3020715782         9012
  3047197804         3456

Ejemplo de inicio de sesión:

    Numero de Usuario: 3224716782
    Clave: 1234

Si la clave se introduce **incorrectamente tres veces**, el usuario será
**bloqueado automáticamente**.

------------------------------------------------------------------------

# Menú principal del cajero

Después de iniciar sesión correctamente el sistema mostrará el siguiente
menú:

    1. Gestion de clave               5. Retiro rapido cuenta principal
    2. Consulta de movimientos        6. Retiro
    3. pagos                          7. Consulta Saldo
    4. otras operaciones              8. transferencia
    9. Depositar                      10. Salir

------------------------------------------------------------------------

# Cambiar clave

La opción **Gestión de clave** permite cambiar la contraseña del
usuario.

Pasos:

1.  Seleccionar la opción **1**
2.  Ingresar la **clave actual**
3.  Ingresar la **nueva clave**
4.  Confirmar la nueva clave

Si ambas claves coinciden, la clave será actualizada correctamente.

------------------------------------------------------------------------

# Consulta de movimientos

Permite ver el historial de operaciones realizadas en la cuenta:

-   Retiros
-   Transferencias
-   Pagos de servicios

------------------------------------------------------------------------

# Pagos

Permite pagar servicios básicos desde el cajero:

-   Agua
-   Luz
-   Gas

El valor del servicio se descuenta del saldo del usuario.

------------------------------------------------------------------------

# Otras operaciones

Esta opción permite consultar y actualizar los datos del usuario.

Opciones:

    1. Mostrar datos usuario
    2. Actualizar datos
    3. Regresar

------------------------------------------------------------------------

# Actualizar datos

Dentro de esta sección se pueden modificar datos del usuario.

### Cambiar nombre

Permite actualizar el nombre del usuario registrado.

### Cambiar número de cuenta

El sistema genera automáticamente un **nuevo número de cuenta** para el
usuario.

Después de confirmar la operación:

-   Se asigna un nuevo número de cuenta
-   El número anterior deja de funcionar

------------------------------------------------------------------------

# Retiro rápido

Permite retirar dinero con montos predefinidos:

-   20.000
-   30.000
-   50.000
-   100.000

------------------------------------------------------------------------

# Retiro personalizado

Permite retirar cualquier cantidad dentro del límite permitido.

Condiciones:

-   El valor no puede ser negativo
-   El valor no puede superar **1.000.000**
-   Debe existir saldo suficiente

------------------------------------------------------------------------

# Consulta de saldo

Muestra el saldo actual disponible en la cuenta.

------------------------------------------------------------------------

# Transferencias

Permite enviar dinero a otra cuenta dentro del sistema.

Pasos:

1.  Ingresar el valor a transferir
2.  Ingresar el número de cuenta destino
3.  Confirmar la operación

------------------------------------------------------------------------

# Depositar dinero

Permite agregar dinero a la cuenta del usuario.

El sistema suma el valor ingresado al saldo actual.

------------------------------------------------------------------------

# Salir del sistema

La opción **10** permite salir del cajero automático de forma segura.

------------------------------------------------------------------------

# Ejemplo visual de uso

Ejecutar el programa:

``` bash
python main.py
```

Inicio de sesión:

    Bienvenido a Nuestro Banco TechBank Riwi Digital

    Numero de Usuario: 3224716782
    Clave: 1234

Menú del cajero:

    Bienvenido Juan Pérez

    1. Gestion de clave               5. Retiro rapido cuenta principal
    2. Consulta de movimientos        6. Retiro
    3. pagos                          7. Consulta Saldo
    4. otras operaciones              8. transferencia
    9. Depositar                      10. Salir

Ejemplo consultar saldo:

    ¿Cual operaciones desea realizar el usuario?: 7

    Este es el saldo 1000.0

Ejemplo retiro:

    ¿Cual operaciones desea realizar el usuario?: 6

    Coloque Valor a Retirar: 200

    Este Es el nuevo Saldo 800.0

Ejemplo depósito:

    ¿Cual operaciones desea realizar el usuario?: 9

    Coloque Valor a Depositar: 500

    Valor depositado Correctamente

------------------------------------------------------------------------

# Autor

**Daniel Elias Alvarez Diaz**
**Luis mario Suarez Sevilla**
**Isaias Daniel Cañate Diaz**
