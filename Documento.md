# 🏧 Sistema de Cajero Automático

## 📌 ¿Qué debe hacer el programa en general?

El programa debe:

1. Permitir iniciar sesión (número de cuenta + clave).
2. Mostrar un menú con las 8 opciones.
3. Ejecutar la operación elegida.
4. Actualizar los datos (saldo, movimientos, clave).
5. Permitir volver al menú hasta que el usuario salga.

---

## 🔐 1️⃣ Gestión de clave

### Debe permitir:

- Cambiar la clave actual.
- Verificar la clave anterior antes de cambiarla.
- Confirmar la nueva clave.

### 🔹 Lógica:

- Pedir clave actual.
- Si es correcta → pedir nueva clave.
- Confirmar nueva clave.
- Guardar nueva clave.

---

## 📜 2️⃣ Consulta de movimientos

Debe mostrar:

Lista de transacciones realizadas:

- Retiros.
- Depósitos.
- Pagos.
- Transferencias.

---

## 🧾 3️⃣ Pagos

Simula pago de servicios.

### Debe:

- Pedir valor a pagar.
- Verificar saldo suficiente.
- Restar dinero.
- Registrar movimiento.

### Opcional:

- Pedir tipo de servicio:
  - Agua.
  - Luz.
  - Internet.

---

## ⚙️ 4️⃣ Otras operaciones

Aquí normalmente van:

- Cambio de cuenta principal.
- Actualizar datos.
- Consultar tipo de cuenta.

Si no está especificado, puedes usarla para:

- Mostrar información del usuario.
- Mostrar número de cuenta.
- Mostrar nombre del titular.

---

## ⚡ 5️⃣ Retiro rápido (cuenta principal)

Debe:

- Mostrar valores predeterminados:
  - $20.000
  - $50.000
  - $100.000
- El usuario elige uno.
- Verificar saldo.
- Descontar dinero.
- Registrar movimiento.

Es diferente al retiro normal porque:

> No pide valor manual, solo opciones rápidas.

---

## 💰 7️⃣ Consulta

Normalmente es:

### 👉 Consulta de saldo

Debe:

- Mostrar saldo disponible.

---

## 🔁 8️⃣ Transferencia

Debe:

- Pedir número de cuenta destino.
- Verificar que exista.
- Pedir valor.
- Verificar saldo suficiente.
- Descontar saldo.
- Sumar saldo a la cuenta destino.
- Registrar movimiento en ambas cuentas.