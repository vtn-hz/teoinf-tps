exec(open("./utils/errores/multiparidad/errors.py").read())
exec(open("./utils/matrix.py").read())



def decodeMultiparidad( byte_array: bytearray, par = True ) -> str:
    matrix = getIntMatrixFromByteArray(byte_array)
    
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
