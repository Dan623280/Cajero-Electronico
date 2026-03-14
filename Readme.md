# Cajero Automatico - TechBank Riwi Digital

Este proyecto es una simulación de un **Cajero Automático (ATM)** desarrollado en **Python**, que funciona completamente desde la terminal.

El sistema permite a los usuarios autenticarse con su **número de cuenta y clave**, y realizar diferentes operaciones bancarias como:

- Consultar saldo
- Retirar dinero
- Retiro rápido
- Transferencias
- Pagos de servicios
- Depósitos
- Cambio de clave
- Consulta de movimientos
- Actualización de datos

Todo el sistema funciona utilizando **diccionarios en memoria** para simular una base de datos de usuarios.

---

# Estructura del proyecto

El proyecto está dividido en varios archivos para organizar mejor el código.


Cajero-Electronico
│
├── main.py
├── cajero.py
├── funciones.py
├── Dicionario.py
└── Colores.py


---

# Archivo principal

El archivo que debe ejecutar el usuario es:


main.py


Ejecutar en la terminal:

```bash
python main.py

Este archivo se encarga de:

Autenticación del usuario

Validación de clave

Bloqueo de cuenta por intentos fallidos

Acceso al menú del cajero automático

Usuarios de prueba

El sistema ya incluye algunos usuarios registrados en el archivo Dicionario.py.

Puedes usar cualquiera de estos para iniciar sesión:

ID	Número de Usuario	Clave	Nombre
1001	3224716782	1234	Juan Pérez
1002	3005716782	5678	María López
1003	3020715782	9012	Carlos Gómez
1004	3047197804	3456	Ana Torres

Ejemplo de inicio de sesión:

Numero de Usuario: 3224716782
Clave: 1234
Funcionalidades del Cajero

Una vez autenticado el usuario, el sistema muestra el siguiente menú:

1. Gestión de clave
2. Consulta de movimientos
3. Pagos
4. Otras operaciones
5. Retiro rápido
6. Retiro
7. Consulta saldo
8. Transferencia
9. Depositar
10. Salir
Descripción de cada archivo
main.py

Controla el flujo principal del programa.

Funciones principales:

Autenticación del usuario

Validación del número de cuenta

Validación de clave

Bloqueo del usuario después de 3 intentos fallidos

Acceso al menú del cajero

cajero.py

Contiene el menú principal del cajero automático.

Desde este archivo se llaman todas las operaciones disponibles para el usuario:

Cambio de clave

Pagos

Transferencias

Retiro rápido

Retiro personalizado

Consulta de saldo

Consulta de movimientos

Depósitos

funciones.py

Contiene toda la lógica del sistema bancario.

Entre sus funciones principales:

Validar número de cuenta

Validar clave

Cambiar clave

Consultar saldo

Registrar movimientos

Realizar transferencias

Realizar pagos

Realizar depósitos

Retirar dinero

También gestiona:

Validación de saldo

Límites de retiro

Registro del historial de movimientos

Dicionario.py

Simula una base de datos de usuarios utilizando un diccionario de Python.

Cada usuario tiene:

Numero_Cuenta
Clave
nombre
saldo
movimientos
Validacion

Ejemplo de usuario:

"1001": {
    "Numero_Cuenta": "3224716782",
    "Clave": "1234",
    "nombre": "Juan Pérez",
    "saldo": 1000.0,
    "movimientos": [],
    "Validacion": "Activo"
}
Colores.py

Contiene constantes para imprimir texto con colores y estilos en la terminal, usando códigos ANSI.

Ejemplo:

ROJO
VERDE
AZUL
AMARILLO
MAGENTA
CYAN
NEGRITA
SUBRAYADO

Esto mejora la visualización del programa en consola.

Características del sistema

✔ Sistema de autenticación
✔ Bloqueo de usuario después de 3 intentos fallidos
✔ Registro de historial de movimientos
✔ Transferencias entre cuentas
✔ Pagos de servicios (agua, luz, gas)
✔ Depósitos
✔ Retiros personalizados
✔ Retiro rápido
✔ Uso de colores en consola
✔ Código modularizado en múltiples archivos

Tecnologías utilizadas

Python

Diccionarios

Programación modular

Control de errores

Librería colorama para colores en consola

Instalar colorama si no está instalada:

pip install colorama
Autor

Proyecto desarrollado como práctica de programación en Python para simular el funcionamiento básico de un cajero automático en consola.
