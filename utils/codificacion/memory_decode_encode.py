import os

def saveComprimido(bits: bytearray, filename: str, path="compressed_messages/"):
    os.makedirs(path, exist_ok=True)

    fullpath = os.path.join(path, filename)

    with open(fullpath, "wb") as f:
        f.write(bits)

def recoverComprimido(filename: str, path="compressed_messages/") -> bytearray:
    """Recupera un archivo comprimido y lo devuelve como bytearray.
    Lanza FileNotFoundError si el archivo no existe.
    """
    fullpath = os.path.join(path, filename)

    if not os.path.exists(fullpath):
        raise FileNotFoundError(f"No se encontró el archivo comprimido: '{fullpath}'")

    with open(fullpath, "rb") as f:
        data = f.read()

    return bytearray(data)
