
from clave import obtener_usuario_por_pin
from cajero import cajero

pin = input("Escriba la clave")

clave = obtener_usuario_por_pin(pin)

if clave == clave[0]:
    cajero()
else:
    print("clave incorrecta")