# Incluir el archivo multiparidad.py
from utils.errores.multiparidad import encodeMultiparidad, decodeMultiparidad

# Definir las matrices como listas de cadenas
ejercicio_25_matrices_pdf = {
    # 25.a: Mensaje recuperado: CASA [2]
    "a": [
        '00100001',
        '10000111',
        '10000010',
        '10100110',
        '10000010'
    ],
    
    # 25.b: Mensaje recuperado: LUNA [2]
    "b": [
        '00101101',
        '10011001',
        '10001010',
        '10011100',
        '10000010'
    ],
    
    # 25.c: Mensaje recuperado: AMOR [2]
    "c": [
        '00101010',
        '10000010',
        '10011010',
        '10011111',
        '10100101'
    ],
    
    # 25.d: Mensaje recuperado: HOLA [2]
    "d": [
        '00010100',
        '10010000',
        '10011110',
        '10011001',
        '10000010'
    ],
    
    # 25.e: Mensaje no recuperable (—) [2]
    "e": [
        '00110101',
        '10011010',
        '10101011',
        '10100100',
        '10000010'
    ],
    
    # 25.f: Mensaje no recuperable (—) [2]
    "f": [
        '00001001',
        '10101001',
        '10100101',
        '10001011',
        '10100110'
    ],
    
    # 25.g: Mensaje no recuperable (—) [2]
    "g": [
        '00011101',
        '10010011',
        '10011101',
        '10001100',
        '10011111'
    ],
    
    # 25.h: Mensaje no recuperable (—) [2]
    "h": [
        '00111110',
        '10000111',
        '10010000',
        '10000010',
        '10101010'
    ]
}

# Convertir las matrices en bytearrays y decodificar
for key, matrix in ejercicio_25_matrices_pdf.items():
    try:
        # Convertir cada fila de la matriz en una lista de enteros
        binary_matrix = [[int(bit) for bit in row] for row in matrix]
        
        # Convertir la matriz en un bytearray
        byte_array = bytearray()
        for row in binary_matrix:
            byte = 0
            for bit in row:
                byte = (byte << 1) | bit
            byte_array.append(byte)
        
        # Llamar a decodeMultiparidad
        print('--------------')
        print(f"Decodificando {key}")
        decoded_message = decodeMultiparidad(byte_array)
        print(f"Mensaje decodificado para {key}: {decoded_message}")
    except Exception as e:
        print(f"Error al decodificar {key}: {e}")