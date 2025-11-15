
def getMatrixTraspuesta(M: list[list]) -> list[list]:
    result = []
    for i in range(len(M[0])):
        result.append([])  
        for j in range(len(M)):
            result[i].append(M[j][i])  
    return result

def getMatrixZeros(filas: int, columnas: int) -> list[list[int]]:
    return [[0 for _ in range(columnas)] for _ in range(filas)]

def printMatrix(matrix: list[list]) -> None:
    max_width = max(len(f"{elem:.2f}") for row in matrix for elem in row)
    for row in matrix:
        print(" ".join(f"{elem:>{max_width}.2f}" for elem in row))

def getBinMatrixFromStr(message: str) -> list:
    binary_matrix = []
    for char in message:
        binary_row = list(map(int, format(ord(char), '07b')))
        binary_matrix.append(binary_row)
    return binary_matrix
    
def getIntMatrixFromByteArray( byte_array: bytearray ) -> list:
    matrix = []
    for byte in byte_array:
        row = []
        for i in range(0, 8):
            row.append( (byte >> (7 - i)) & 1 )
        matrix.append(row)
    return matrix

def getMatrixProduct(A: list[list], B: list[list]) -> list:

    # A:{ixj}*B:{jxk} = C{ixk}
    if (len(A[0]) != len(B)):
        raise Exception("Las matrices no son compatibles para la multiplicacion matricial")

    result = getMatrixZeros(len(A), len(B[0]))

    for i in range(len(A)):
        for k in range(len(B[0])):
            amount = 0
            for j in range(len(B)):
                amount += A[i][j] * B[j][k]
            
            result[i][k] = amount
    
    return result


def getDeterminanteRowDuplicated(matrix: list[list], col: int, row: int) -> float:
    result = getMatrixZeros(len(matrix[0]), len(matrix[0]) - 1)
    j = 0
    for i in range(len(matrix[0])):
        if i != row:
            result[i][j] = 1
            j += 1
    
    result[row][col] = 1
    return result

    # ...existing code...

def printMatrixVerbose(matrix: list[list], row_labels: list[str], col_labels: list[str]) -> None:
    """
    Imprime la matriz con etiquetas de filas y columnas.
    - matrix: matriz numérica (list of lists)
    - row_labels: etiquetas para cada fila (len == filas)
    - col_labels: etiquetas para cada columna (len == columnas)
    """
    if not matrix:
        print("(matriz vacía)")
        return
    filas = len(matrix)
    columnas = len(matrix[0])

    if len(row_labels) != filas:
        raise ValueError("row_labels debe tener la misma cantidad de elementos que filas de la matriz.")
    if len(col_labels) != columnas:
        raise ValueError("col_labels debe tener la misma cantidad de elementos que columnas de la matriz.")

    # Ancho para números
    num_width = max(len(f"{elem:.2f}") for row in matrix for elem in row)
    # Ancho para etiquetas de fila
    row_label_width = max(len(lbl) for lbl in row_labels)
    # Anchos por columna (el máximo entre etiqueta y número)
    col_widths = []
    for j in range(columnas):
        max_val_width = max(len(f"{matrix[i][j]:.2f}") for i in range(filas))
        col_widths.append(max(max_val_width, len(col_labels[j]), num_width))

    # Encabezado
    header = " " * (row_label_width) + "  " + " ".join(f"{col_labels[j]:>{col_widths[j]}}" for j in range(columnas))
    print(header)
    # Separador
    print(" " * (row_label_width) + "  " + " ".join("-" * col_widths[j] for j in range(columnas)))

    # Filas
    for i in range(filas):
        fila_str = f"{row_labels[i]:>{row_label_width}}  " + " ".join(f"{matrix[i][j]:>{col_widths[j]}.2f}" for j in range(columnas))
        print(fila_str)
