import random

def montecarloIntervals( P: list ) -> list:
    last = 0
    result = []

    for pi in P:
        result.append((last, last+pi))
        last = last+pi
        
    return result

def randomIndexByInterval(intervals: list[tuple]):
    rdm = random.uniform(0, 1)
    i = 0
    while i < len(intervals) and not (intervals[i][0] <= rdm and rdm <= intervals[i][1]):
        i += 1

    return min(i, len(intervals)-1)

def getTraspuesta(M: list[list]) -> list[list]:
    return [list(row) for row in zip(*M)]

def getHighestAvgIndex(M):
    maxAvg = [
        sum(m_row) / len(m_row)
        for m_row in M
    ]

    return maxAvg.index(max(maxAvg))

def simulateFuente( M, S, n:int) -> str:
    if n <= 0:
        return ''

    prev_i = getHighestAvgIndex(M)
    montercarlos = [
        montecarloIntervals(row) 
        for row in getTraspuesta(M)
    ]

    fuente = S[prev_i]
    for _ in range(n-1):
        current_j = randomIndexByInterval(montercarlos[prev_i])
        fuente += S[current_j]
        prev_i = current_j
    
    return fuente
    

def main():
    M = [# A    B   C
        [0.5, 0.6666666666666666, 0.5], 
        [0.25, 0.3333333333333333, 0.0], 
        [0.25, 0.0, 0.5]
    ]

    S = ['A', 'B', 'C']

    print(simulateFuente(M, S, 30))

main()