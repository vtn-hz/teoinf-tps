import math

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

    i = 0
    lastV = V
    V = operate(M, V)

    while getMaxGap(V, lastV) > tolerancia:
        lastV = V
        V = normalize(operate(M, V))
        i+=1
        
    
    return V


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

def main():
    matriz = [
        [1/2, 0, 0, 1/2],
        [1/2, 0, 0, 0],
        [0, 1/2, 0, 0],
        [0, 1/2, 1, 1/2],
    ]

    matriz = [
        [1/3, 0, 1, 1/2, 0],
        [1/3, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [1/3, 0, 0, 0, 1/2],
        [0, 0, 0, 1/2, 1/2]
    ]


    V = getVEstacionario(matriz)
    hmarkov = calculateHMarkov(matriz, V)

    print(V)
    print(hmarkov)
if __name__ == "__main__":
    main()
