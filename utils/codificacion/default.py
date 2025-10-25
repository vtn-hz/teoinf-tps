def defaultCodify(S: list, C: list, message: str) -> str:
    # Crear un diccionario para mapear elementos de S a C
    mapping = dict(zip(S, C))
    
    # Reemplazar cada carácter en el mensaje según el mapeo
    result = ''.join(mapping[char] for char in message if char in mapping)
    
    return result