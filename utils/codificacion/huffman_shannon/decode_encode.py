def build_C(alf, C):
    """Construye el diccionario símbolo -> código"""
    return dict(zip(alf, C))

def build_byteArray(bits: list) -> bytearray:
    padding = (8 - (len(bits) % 8)) % 8
    bits += [0] * padding

    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for bit in bits[i:i+8]:
            byte = (byte << 1) | bit
        byte_array.append(byte)

    
    byte_array.append(padding)
    return byte_array

def solve_byteArray(bytes: bytearray) -> list:
    if not bytes:
        return []

    padding = bytes[-1]
    data_bytes = bytes[:-1]

    bits = []
    for byte in data_bytes:
        bits.extend([(byte >> i) & 1 for i in range(7, -1, -1)])

    return bits[:-padding]

# ==============================================================
# CODIFICADORES
# ==============================================================

def codificar_dict(message: str, C: dict) -> bytearray:
    """Codifica un mensaje en un bytearray usando un mapa símbolo->código.
    El último byte almacena la cantidad de bits de padding agregados.
    """
    bits = ''.join(C[ch] for ch in message)
    bits = [int(b) for b in bits]

    # print("Códigos posibles:")
    # for simbolo, codigo in C.items():
    #    print(f"  {simbolo!r}: {codigo}")

    # print("\nBits del mensaje:")
    # print(bits)

    return build_byteArray(bits)




def codificar(message: str, alf: list, C: list) -> bytearray:
    """Codifica usando listas paralelas alf y C"""
    C = build_C(alf, C)
    return codificar_dict(message, C)


# ==============================================================
# DECODIFICADORES
# ==============================================================

def decodificar_dict(data: bytearray, C: dict) -> str:
    """Decodifica un bytearray a texto usando un mapa código->simbolo"""

    bits = solve_byteArray( data )
    message = ""
    buffer = ""

    for bit in bits:
        buffer += str(bit)
        if buffer in C:
            message += C[ buffer ]
            buffer = ""

    return message


def decodificar(data: bytearray, C: list, alf: list) -> str:
    """Decodifica usando listas paralelas alf y C"""
    C = build_C(C, alf)
    return decodificar_dict(data, C)
