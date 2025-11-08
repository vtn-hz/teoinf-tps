
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

def printMatrix(M: list[list]):
    for row in M:
        print([f"{val:.4f}" for val in row])

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