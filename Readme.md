 Cajero Electrónico - TechBank Riwi Digital

Este proyecto es una **simulación de un cajero automático (ATM)** desarrollado en Python que funciona completamente desde la terminal.

El usuario puede iniciar sesión con su **número de cuenta y clave**, y realizar diferentes operaciones bancarias como:

- Consultar saldo
- Retirar dinero
- Retiro rápido
- Depositar dinero
- Transferir dinero a otras cuentas
- Pagar servicios (agua, luz o gas)
- Consultar historial de movimientos
- Cambiar su clave
- Actualizar sus datos

El sistema está diseñado para simular el funcionamiento básico de un cajero automático de forma sencilla desde la consola.

---

# Cómo descargar el proyecto

Primero debes **clonar el repositorio desde GitHub**.

En tu terminal escribe:

```bash
git clone https://github.com/Dan623280/Cajero-Electronico.git

Luego entra a la carpeta del proyecto:

cd Cajero-Electronico
Cómo ejecutar el programa

El archivo principal del programa es:

main.py

Para iniciar el cajero automático ejecuta:

python main.py

El sistema te pedirá número de usuario y clave para iniciar sesión.

Usuarios para iniciar sesión

Puedes usar cualquiera de los siguientes usuarios de prueba:

Número de cuenta	Clave
3224716782	1234
3005716782	5678
3020715782	9012
3047197804	3456

Ejemplo de inicio de sesión:

Numero de Usuario: 3224716782
Clave: 1234

Si la clave se introduce incorrectamente 3 veces, la cuenta será bloqueada automáticamente.

Menú principal del cajero

Después de iniciar sesión correctamente, el cajero mostrará el siguiente menú:

1. Gestion de clave
2. Consulta de movimientos
3. pagos
4. otras operaciones
5. Retiro rapido cuenta principal
6. Retiro
7. Consulta Saldo
8. transferencia
9. Depositar
10. Salir

Cada opción permite realizar diferentes operaciones bancarias.

Cambiar clave (Gestión de clave)

Esta opción permite cambiar la clave de acceso del usuario.

Pasos:

Seleccionar la opción 1

Ingresar la clave actual

Ingresar la nueva clave

Confirmar la nueva clave

Si ambas claves coinciden, la clave será actualizada.

Esto permite al usuario mejorar la seguridad de su cuenta.

Consulta de movimientos

Esta opción muestra el historial de operaciones realizadas, como:

Retiros

Transferencias

Pagos de servicios

Esto permite al usuario ver todas las transacciones realizadas desde su cuenta.

Pagos

Permite pagar servicios básicos directamente desde el cajero.

Opciones disponibles:

Pagar agua

Pagar luz

Pagar gas

El valor pagado se descuenta del saldo disponible.

Otras operaciones

Este menú incluye opciones para consultar y actualizar los datos del usuario.

Opciones disponibles:

1. Mostrar datos usuario
2. Actualizar datos
3. Regresar
Actualizar datos

Dentro de esta sección el usuario puede modificar su información.

Opciones disponibles:

Cambiar nombre

Permite actualizar el nombre del usuario asociado a la cuenta.

Cambiar número de cuenta

El sistema genera automáticamente un nuevo número de cuenta para el usuario.

Después de confirmar la operación:

Se genera un número de cuenta nuevo

El número anterior deja de funcionar

Esto simula la actualización de datos bancarios dentro del sistema.

Retiro rápido

Permite retirar dinero rápidamente con montos predefinidos.

Ejemplos:

20.000

30.000

50.000

100.000

El dinero se descuenta automáticamente del saldo disponible.

Retiro personalizado

Permite ingresar cualquier valor de retiro dentro del límite permitido.

Condiciones:

No puede ser un valor negativo

No puede superar 1.000.000

Debe existir saldo suficiente

Consulta de saldo

Muestra el saldo actual disponible en la cuenta.

Transferencias

Permite enviar dinero a otra cuenta dentro del sistema.

Pasos:

Ingresar el valor a transferir

Ingresar el número de cuenta destino

Confirmar la operación

Si la cuenta existe y hay saldo suficiente, la transferencia se realiza correctamente.

Depositar dinero

Permite agregar dinero a la cuenta.

El sistema suma el valor ingresado al saldo actual del usuario.

Salir del cajero

La opción 10 permite salir del sistema de forma segura.

Características del sistema

Autenticación por número de cuenta y clave

Bloqueo automático después de 3 intentos fallidos

Registro de movimientos

Transferencias entre usuarios

Pagos de servicios

Depósitos

Retiros rápidos y personalizados

Actualización de datos del usuario
