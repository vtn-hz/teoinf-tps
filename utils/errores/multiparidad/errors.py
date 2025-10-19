
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
