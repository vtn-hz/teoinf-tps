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

def getMaxRowGap( row: list) -> float:
    _max = 0
    n = len(row)
    for i in range(n):
        for j in range(i+1, n):
            res = abs(row[i] - row[j])
            _max = res if res > _max else _max

    return _max

def isFuenteNula(M: list[list], T: float) -> bool:  
    result = True
    i = 0

    while result and i < len(M):
        result = getMaxRowGap(list(M[i])) < T
        i += 1

    return result

import math

def getTraspuesta(M: list[list]) -> list[list]:
    return [list(row) for row in zip(*M)]

def calculateI(pi: float) -> float:
    return math.log2(1/pi); 

def calculateHMarkov(M :list[list], V: tuple) -> float:
    M_t = getTraspuesta(M)
    
    result = 0
    for vi, caseA in zip(V, M_t):
        result += vi*sum([
            caseB*calculateI( caseB ) 
            if caseB > 0
            else 0
            for caseB in caseA 
        ])

    return result

def getVEstacionarioInit() -> tuple:
    return (1/3, 1/3, 1/3) 

def getTolerancia() -> float:
    return 0.1

def operate(M: list[list], V: tuple) -> tuple:
    return tuple([
        sum([ vi*mij for vi, mij in zip(row, V)])
        for row in M       
    ])


def normalize(V: tuple) -> tuple:
    s = sum(V)
    return tuple(v/s for v in V)

def getMaxGap(V1: tuple, V2: tuple) -> float:
    return min([
        abs(vi - vii)
        for vi, vii in zip(V1, V2)
    ])

def getVEstacionario(M: list[list]) -> tuple:
    V = getVEstacionarioInit()
    tolerancia = getTolerancia()

    lastV = V
    V = operate(M, V)

    while getMaxGap(V, lastV) > tolerancia:
        lastV = V
        V = normalize(operate(M, V))
    
    return V

def main():
    message = input("mensaje: ")

    M = generateMatrixTransicionN2(message)
    isNula = isFuenteNula(M, 0.1)

    print("Es nula" if isNula else "No es nula")
    print(M)
        
    V = getVEstacionario( M )
    print(V)

    print(calculateHMarkov(M, V))

main()