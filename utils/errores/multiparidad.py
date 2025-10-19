
def transformBinMatrix(message: str) -> list:
    binary_matrix = []
    for char in message:
        binary_row = list(map(int, format(ord(char), '07b')))
        binary_matrix.append(binary_row)
    return binary_matrix
    
def getMatrixFromBytes( byte_array: bytearray ) -> list:
    matrix = []
    for byte in byte_array:
        row = []
        for i in range(0, 8):
            row.append( (byte >> (7 - i)) & 1 )
        matrix.append(row)
    return matrix


def addHorizontalParity(matrix: list, par = True) -> list:
    for i in range(len(matrix)):
        bitAmount = 0 if par else 1
        for j in range(len(matrix[i])):
            bitAmount += matrix[i][j]

        parity_bit = bitAmount % 2 
        matrix[i].append(parity_row)
    return matrix

def addVerticalParity(matrix: list, par = True) -> list:
    parityRow = [] * len(matrix[0])

    for j in range(len(matrix[0])):
        bitAmount = 0 if par else 1
        for i in range(len(matrix)):
            bitAmount += matrix[i][j]

        parityRow[j] = bitAmount % 2
    
    matrix.insert(0, parityRow)
    return matrix

def getMatrixMultiparidad(message: str, par = True ) -> list:
    matrix = transformBinMatrix(message)
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

def trackErrorMultiparidad( matrix: list, par = True ) -> list:

    errHorizontal = []
    errVertical = []

    # Verificar paridad horizontal    
    for i in range(len(matrix)):
        bitAmount = 0 if par else 1
        for j in range(len(matrix[i])):
            bitAmount += matrix[i][j]
        if (bitAmount % 2) != 0:
            errHorizontal.append(i)

    # Verificar paridad vertical
    for j in range(len(matrix[0])):
        bitAmount = 0 if par else 1
        for i in range(len(matrix)):
            bitAmount += matrix[i][j]
        if (bitAmount % 2) != 0:
            errVertical.append(j)

    return errHorizontal, errVertical  

def detectarErrorMultiparidad( matrix: list, par = True ) -> bool:
    errHorizontal, errVertical = trackErrorMultiparidad(matrix, par)
    return len(errHorizontal) > 0 or len(errVertical) > 0

def trySolveErrorMultiparidad( matrix: list, par = True ) -> bool:
    errHorizontal, errVertical = trackErrorMultiparidad(matrix, par)

    print('[DEBUG] errHorizontal: ', end='')
    print(errHorizontal)
    print('[DEBUG] errVertical: ', end='')
    print(errVertical)

    if len(errHorizontal) != 1 or len(errVertical) != 1:
        raise Exception("No se puede corregir el error")  
    
    row = errHorizontal[0]
    col = errVertical[0]


    if row == 0 and col == len(matrix[0]) - 1:
        raise Exception("No se puede corregir, error en paridad cruzada")  
    
    # preguntar
    matrix[row][col] ^= 1  

def decodeMultiparidad( byte_array: bytearray, par = True ) -> str:
    matrix = getMatrixFromBytes(byte_array)
    
    print('Matriz recibida:')
    print('rows :', len(matrix))
    print('cols :', len(matrix[0]))
    for row in matrix:
        for bit in row:
            print(bit, end='')
        print()

    if detectarErrorMultiparidad(matrix, par):
        trySolveErrorMultiparidad(matrix, par)


    message = ''
    for i in range(1, len(matrix)):
        char_bits = matrix[i][:-1]  
        char_code = 0
        for bit in char_bits:
            char_code = (char_code << 1) | bit
        message += chr(char_code)
    
    return message