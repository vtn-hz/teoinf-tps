exec(open("./utils/matrix.py").read())


def generateMatrixTransicion(message: str) -> list[list]:
    symbols = sorted(set( message ))
    n = len(symbols)
    M = []

    for i in range( n ):
        total = 0
        M.append([])
        for j in range( n ):
            symbolRepetitions = message.count(symbols[i] + symbols[j])
            total += symbolRepetitions
            
            M[i].append( symbolRepetitions )
               
        for j in range( n ):
            M[i][j] /= total if total != 0 else 1
    
    return getMatrixTraspuesta(M)