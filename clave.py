def validacion(clave_puesta, clave_usuario):
    if clave_puesta == clave_usuario:
        return True 
    else:
        return False    

def cambio_clave(clave_puesta):
    print("clave camviada correctamente")
    return clave_puesta

def obtener_usuario_por_pin(pin):
    for clave, datos in usuarios.items():
        if datos["pin"] == pin:
            # Devuelve la clave
            return True,clave 
    return False


