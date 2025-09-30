import math

# -------- modulo vector estacionario -------
def getErrorTolerancia() -> float:
    return 0.00000001

def getVEstacionarioInit( n: int ) -> tuple:
    items = [1/n]*n
    
    return ( items ) 

'''
@param: M: matriz de transición (lista de listas)
@param: V: vector estacionario a calcular (tupla)
'''
def getOperatedVEstacionario(M: list[list], V: tuple) -> tuple:
    return tuple([
        sum([ vi*mij for vi, mij in zip(mi, V)])
        for mi in M       
    ])

def getNormalizedVEstacionario(V: tuple) -> tuple: 
    return tuple( vi /sum(V) for vi in V)


'''
@param: V1: vector estacionario inicial (tupla)
@param: V2: vector estacionario operado (tupla)
@return: máximo delta entre ambos vectores
'''
def getMaxVEstacionarioDelta(V1: tuple, V2: tuple) -> float:
    return max([
        abs(vi - vii)
        for vi, vii in zip(V1, V2)
    ])


'''
@param: M: matriz de transición (lista de listas)
@return: vector estacionario (tupla)
'''
def calculateVEstacionario(M: list[list]) -> tuple:
    V = getVEstacionarioInit( len(M) )

    lastV = V
    V = getOperatedVEstacionario(M, V)

    while getMaxVEstacionarioDelta(V, lastV) > getErrorTolerancia():
        lastV = V
        V = getNormalizedVEstacionario(
            getOperatedVEstacionario(M, V)
        )
    
    return V

# -------- modulo vector estacionario -------

# -------- modulo matrix transicion -------

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

# -------- modulo matrix transicion -------
# unidades de información: bits (base 2)
def calculateI(pi: float) -> float:
    return math.log2(1/pi); 

def getMatrixTraspuesta(M: list[list]) -> list[list]:
    result = []
    for i in range(len(M[0])):
        result.append([])  
        for j in range(len(M)):
            result[i].append(M[j][i])  
    return result

def calculateHFuenteMarkoviana(M :list[list], V: tuple) -> float:
    Mt = getMatrixTraspuesta(M)
    
    result = 0
    for vi, caseA in zip(V, Mt):
        result += vi*sum([
            caseB*calculateI( caseB ) 
            if caseB > 0
            else 0
            for caseB in caseA 
        ])

    return result

def main():
    data = input("data: ")

    M = generateMatrixTransicion(data)
    V = calculateVEstacionario( M )

    print( sortedItems(data) )
    print(V)
    print( [ round(vi,2) for vi in V ])
    print( sum(V) )

    print(calculateHFuenteMarkoviana(M, V))



main()