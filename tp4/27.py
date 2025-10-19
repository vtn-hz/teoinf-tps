exec(open("./utils/errores/multiparidad.py").read())

def printMatrix(matrix: list):
    for row in matrix:
        for bit in row:
            print(bit, end=' ')
        print()

def main(): 
    # queda mal cuando es impar, preguntar
    message = input("Ingrese el mensaje a transmitir: ")
    paridad = input("¿Usar paridad par? (s/n): ").lower() == 's'

    print("\n--- Codificación ---")
    encoded = encodeMultiparidad(message, paridad)
    print("Mensaje codificado (bytearray):", encoded)
    matrix = getIntMatrixFromByteArray(encoded)
    print("Matriz con bits de paridad añadidos:")
    printMatrix(matrix)
    print("\n--- Decodificación ---")
    decoded = decodeMultiparidad(encoded, paridad)
    print("Mensaje decodificado:", decoded)

main()