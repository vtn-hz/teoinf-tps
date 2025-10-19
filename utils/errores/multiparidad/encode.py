exec(open("./utils/matrix.py").read())

def addHorizontalParity(matrix: list, par = True) -> list:
    for i in range(len(matrix)):
        bitAmount = 0 if par else 1
        for j in range(len(matrix[i])):
            bitAmount += matrix[i][j]
        matrix[i].append(bitAmount % 2 )

    return matrix

def addVerticalParity(matrix: list, par = True) -> list:
    parityRow = [-1] * len(matrix[0])

    for j in range(len(matrix[0])):
        bitAmount = 0 if par else 1
        for i in range(len(matrix)):
            bitAmount += matrix[i][j]
        parityRow[j] = bitAmount % 2
    matrix.insert(0, parityRow)

    return matrix

def getMatrixMultiparidad(message: str, par = True ) -> list:
    matrix = getBinMatrixFromStr(message)
    matrix = addHorizontalParity(matrix, par)
    matrix = addVerticalParity(matrix, par)
    return matrix

def encodeMultiparidad( message: str, par = True ) -> bytearray:
    matrix = getMatrixMultiparidad(message, par)
    
    byte_array = bytearray()
    for row in matrix:
        byte = 0
        for bit in row:
            byte = (byte << 1) | bit
        byte_array.append(byte)
    
    return byte_array