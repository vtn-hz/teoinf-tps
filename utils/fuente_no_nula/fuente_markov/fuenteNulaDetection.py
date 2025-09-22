
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
