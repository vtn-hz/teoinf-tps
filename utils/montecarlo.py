import random

def getMontecarloIntervals( P: list ) -> list:
    last = 0
    result = []

    for pi in P:
        result.append((last, last+pi))
        last = last+pi
        
    return result

def getRandomIndexByInterval(montecarloIntervals: list[tuple]):
    rdm = random.uniform(0, 1)
    i = 0
    while i < len(montecarloIntervals) and not (montecarloIntervals[i][0] <= rdm and rdm <= montecarloIntervals[i][1]):
        i += 1

    return min(i, len(montecarloIntervals)-1)
