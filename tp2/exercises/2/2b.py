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

def simulateSymbol( symbols: str, intervals: list[tuple] ) -> str:        
    return symbols[ randomIndexByInterval(intervals) ]

def simulateFuente( S: dict, iteration: int) -> str:
    intervals = montecarloIntervals( list(S.values()) )
    fuente = []

    while (iteration):
        fuente.append( simulateSymbol( list(S.keys()), intervals ) )
        iteration -= 1
    
    return ' '.join(fuente)



def main():
    S = {
        'A': 0.125, 
        'a': 0.25, 
        'b': 0.1875, 
        'c': 0.125, 
        'z': 0.125, 
        'az': 0.125, 
        'lorem': 0.0625
    }

    fuente = simulateFuente(S, 30)
    print(fuente)

main()