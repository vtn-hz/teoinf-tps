import math

# ---  MATRIX ---

def getMatrixTraspuesta(M: list[list]) -> list[list]:
    result = []
    for i in range(len(M[0])):
        result.append([])  
        for j in range(len(M)):
            result[i].append(M[j][i])  
    return result

def getMatrixZeros(filas: int, columnas: int) -> list[list[int]]:
    return [[0 for _ in range(columnas)] for _ in range(filas)]

# ---  MATRIX ----

# --- GENERAR S-NULO ---

def getOcurrences( phrase: str ) -> dict:
    occurrences = {}

    for si in phrase:
        if not (si in occurrences):
            occurrences[si] = 0
        occurrences[si] += 1
    
    return occurrences

'''
@return dictionary: { letra: porcentaje aparicion } 
'''
def buildS ( source: str ) -> dict:
    occurrences = getOcurrences( source )
    return { si:cant/len(source) for si, cant in occurrences.items() }

# --- GENERAR S-NULO ---

# --- MATRIX TRANSICION ----


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

# --- MATRIX TRANSICION ----


# --- ENTROPY ----

def calculateI(pi: float) -> float:
    return math.log2(1/pi); 

def calculateH(P: list) -> float:
    return sum([
        pi*calculateI(pi) 
        for pi in P
    ])

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

# --- ENTROPY ----


# --- EXTENSION ---

def generateExtensionsFromLL(alf: list, prob: list, n: int) -> list:
    if n == 1:
        return alf, prob
    
    P = []
    S = []

    prevS, prevP = generateExtensionsFromLL(alf, prob, n-1)
    
    for i, phrase  in enumerate(prevS):
        for j, symbol in enumerate(alf):
            S.append( phrase + symbol )
            P.append( prevP[i] * prob[j] )
    return S, P 

# --- EXTENSION ---

# --- VECTOR ESTACIONARIO ---

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


# --- VECTOR ESTACIONARIO ---

# --- FUENTE NULA ---

def getMaxProbabilityDelta( P: list ) -> float:
    maxProbabilityDelta = 0

    for pi in P:
        for pj in P:
            probDelta = abs(pi - pj)
            maxProbabilityDelta = max(probDelta, maxProbabilityDelta)

    return maxProbabilityDelta

'''
@param M: Matriz de transicion
@param tolerancia: Tolerancia para considerar fuente nula
'''
def isFuenteNula(M: list[list], tolerancia: float) -> bool:
    
    for P in M:
        if getMaxProbabilityDelta( P ) >= tolerancia:
            return False

    return True

# --- FUENTE NULA ---

def main():
    # --- A ---   
    data = input("data: ")
    S = buildS(data) 

    for si, pi in S.items():
        print("si: ", si, " pi:", pi ) 
    # --- A ---   

    # --- B ---   
    print( sortedItems(data) )
    M = generateMatrixTransicion(data)

    for i in range( len(M) ):
        for j in range ( len(M) ):
            print( round(M[i][j], 2), " ", end="" )
        print("")
    # --- B --- 

    # --- C ---
    print()
    print(" ES FUENTE NULA " if isFuenteNula(M, tolerancia=0.01) else "ES FUENTE NO-NULA")
    print()
    # --- C ---

    if (isFuenteNula(M, 0.01)):

        # --- D ---
        print( 'H: ', calculateH( list(S.values()) ) )
        # --- D ---
        print( '-------' )

        n = 2 

        print(list(S.keys()))
        print(list(S.values()))

        sn, pn = generateExtensionsFromLL( list(S.keys()), list(S.values()), 2)
        Sn = dict( zip(sn, pn) )

        # --- E ---
        sumatory = 0
        for si, pi in Sn.items():
            print("si: ", si, " pi:", pi) 
            print("si: ", si, " pi:", round(pi, 2)) 
            print("-----------------")
            sumatory += pi

        
        print("---", sumatory, "---")

        print( 'H(Sn):',calculateH( list( Sn.values() ) ) )
        print( 'n*H(S):', n*calculateH( list( S.values() ) ) )
        print( 'round(n*H(S)):', round(n*calculateH( list( S.values() ) ), 2) )
    else:
        V = calculateVEstacionario( M )

        # --- D ---
        print( 'H markov: ', calculateHFuenteMarkoviana(M, V) )
        # --- D ---

        print('------')

        # --- F ---
        print('V estacionario: ')
        print( sortedItems(data) )
        print(V)
        print( [ round(vi,2) for vi in V ])
        print( sum(V) )
        print('')
        # --- F ---
        
        

main()