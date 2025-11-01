from utils.montecarlo import getMontecarloIntervals, getRandomIndexByInterval

def simulateSymbol( symbols: str, intervals: list[tuple] ) -> str:        
    return symbols[ getRandomIndexByInterval(intervals) ]

def simulateFuente( S: dict, iteration: int) -> str:
    intervals = getMontecarloIntervals( list(S.values()) )
    fuente = []

    while (iteration):
        fuente.append( simulateSymbol( list(S.keys()), intervals ) )
        iteration -= 1
    
    return ''.join(fuente)

