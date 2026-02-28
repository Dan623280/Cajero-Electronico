def validacion(clave_puesta, clave_usuario):
    if clave_puesta == clave_usuario:
        return True 
    else:
        return False    

def cambio_clave(clave_puesta):
    print("clave camviada correctamente")
    return clave_puesta

usuarios = {
    "1001": {"nombre": "Juan Pérez", "pin": "1234", "saldo": 1500.0},
    "1002": {"nombre": "María López", "pin": "5678", "saldo": 2500.0},
    "1003": {"nombre": "Carlos Gómez", "pin": "9012", "saldo": 3200.0},
    "1004": {"nombre": "Ana Torres", "pin": "3456", "saldo": 1000.0}
}


def obtener_usuario_por_pin(pin):
    for clave, datos in usuarios.items():
        if datos["pin"] == pin:
            # Devuelve la clave
            return True,clave 
    return False


