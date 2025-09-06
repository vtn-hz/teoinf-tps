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