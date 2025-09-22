exec(open("./utils/montecarlo.py").read())
exec(open("./utils/matrix.py").read())

'''
Para iniciar, se elige el simbolo con mayor probabilidad de ocurrencia
y luego se elige el siguiente simbolo segun la fila de la matriz de
transicion correspondiente al simbolo anterior.

@param M: Matriz de transicion
@return: Indice de la fila con mayor promedio
'''
def getHighestAvgIndex(M: list[list]) -> int:
    maxAvg = [
        sum(m_row) / len(m_row)
        for m_row in M
    ]

    return maxAvg.index( max(maxAvg) )

def getMontecarlosByColumns(M: list[list]) -> list[list[tuple]]:
    return [
        getMontecarloIntervals(row) 
        for row in getMatrixTraspuesta(M)
    ]

def simulateFuente( M: list[list], S: list , n:int) -> str:
    if n <= 0:
        return ''

    prevIndex = getHighestAvgIndex(M)
    montercarlosByColumn = getMontecarlosByColumns(M)

    fuente = S[prevIndex]
    for _ in range(n-1):
        currentIndex = getRandomIndexByInterval( montercarlosByColumn[prevIndex] )
        fuente += S[currentIndex]
        prevIndex = currentIndex
    
    return fuente
