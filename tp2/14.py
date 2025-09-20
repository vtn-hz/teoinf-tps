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
    return 0.001

def operate(M: list[list], V: tuple) -> tuple:
    return tuple([
        sum([ vi*mij for vi, mij in zip(M[0], V)]),
        sum([ vi*mij for vi, mij in zip(M[1], V)]),
        sum([ vi*mij for vi, mij in zip(M[2], V)]),
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
    M = [
        [0.58, 0.43, 0.3],
        [0.17, 0.53, 0.1],
        [0.25, 0.14, 0.6]
    ]

    V = getVEstacionario(M)

    print( V )
    print( operate(M, V) )
    print( calculateHMarkov(M, V) )
    
main()