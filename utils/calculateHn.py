import math

def calculateI(pi: float) -> float:
    return math.log2(1/pi); 

def calculateH(P: list) -> float:
    return sum([
        pi*calculateI(pi) 
        for pi in P
    ])

def calculateHn(P: list, n: int) -> float:
    return n*sum([
        pi*calculateI(pi) 
        for pi in P
    ])

