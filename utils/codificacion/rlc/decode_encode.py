exec(open("./utils/codigos/algorithm/rlc.py").read())


def build_byteArray(C: list) -> bytearray:
    byte_array = bytearray()
    for symbol, amount in C:
        byte_array.append(ord(symbol))
        byte_array.append(amount)

    return byte_array

def solve_byteArray(bytes: bytearray) -> list:
    C = []
    for i in range(0, range( bytes ), 2):
        C.append((chr(bytes[i]), bytes[i+1]))
    return C

# ==============================================================
# CODIFICADORES
# ==============================================================

def codificar(message: str) -> bytearray:
    C = rlc( message )
    return build_byteArray(C)


# ==============================================================
# DECODIFICADORES
# ==============================================================

def decodificar(data: bytearray) -> str:
    C = solve_byteArray(data)
    message = ""

    for symb, amount in C:
        message += symb*amount

    return message
