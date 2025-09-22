def getErrorTolerancia() -> float:
    return 0.001

def getVEstacionarioInit() -> tuple:
    return (1/3, 1/3, 1/3) 

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
    V = getVEstacionarioInit()

    lastV = V
    V = getOperatedVEstacionario(M, V)

    while getMaxVEstacionarioDelta(V, lastV) > getErrorTolerancia():
        lastV = V
        V = getNormalizedVEstacionario(
            getOperatedVEstacionario(M, V)
        )
    
    return V