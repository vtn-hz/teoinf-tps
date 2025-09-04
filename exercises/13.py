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


def main():
    # Matriz de transición
    M = [
        [1/2, 1/3, 0],
        [1/2, 1/3, 1],
        [0,   1/3, 0]
    ]

    # Vector estacionario
    v = (1/3, 1/2, 1/6)

    result = calculateHMarkov(M, v)
    print(result)

main()