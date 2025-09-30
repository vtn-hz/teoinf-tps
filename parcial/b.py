def getMatrixZeros(filas: int, columnas: int) -> list[list[int]]:
    return [[0 for _ in range(columnas)] for _ in range(filas)]

def sortedItems(message: str)  -> set:
     return sorted(set( message ))

def generateMatrixTransicion(message: str) -> list[list]:
    symbols = sortedItems(message)
    n = len(symbols)
    M = getMatrixZeros(n, n)

    sumCols = [0 for _ in range(n)]

    for i in range( len(message) - 1 ):
        col = symbols.index( message[i] )
        row = symbols.index( message[i + 1] )

        M[row][col] += 1
        sumCols[col] += 1

    for j in range(n):
        for i in range(n):
            M[i][j] /= sumCols[j] if sumCols[j] > 0 else 1
    
    return M

def main():
    data = input("data: ")
    print( sortedItems(data) )
    M = generateMatrixTransicion(data)

    print('round: 6')
    for i in range( len(M) ):
        for j in range ( len(M) ):
            print( round(M[i][j], 6), " ", end="" )
        print("")

    print('----------------')
    print('round: 2')
    for i in range( len(M) ):
        for j in range ( len(M) ):
            print( round(M[i][j], 2), " ", end="" )
        print("")

main()