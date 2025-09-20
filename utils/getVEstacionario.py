def getVEstacionarioInit() -> tuple:
    return (1/3, 1/3, 1/3) 

def getTolerancia() -> float:
    return 0.001

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