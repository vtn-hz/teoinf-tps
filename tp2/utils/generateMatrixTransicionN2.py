def getCharDistinct(message: str) -> list:
    return sorted(set( message ))

def getOcurrences(message: str,  key: str) -> int:
    return message.count(key)

def generateMatrixTransicionN2(message: str) -> list[list]:
    symbols = getCharDistinct(message)
    n = len(symbols)
    M = [[0 for _ in range(n)] for _ in range(n)]

    for i in range( n ):
        total = 0
        for j in range( n ):
            M[j][i] = getOcurrences( message, symbols[i] + symbols[j] )
            total += M[j][i]
        
        for j in range( n ):
            M[j][i] /= total if total != 0 else 1
    
    return M