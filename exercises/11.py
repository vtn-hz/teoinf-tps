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

def generateExtensions(S: dict, n: int) -> dict:
    if n == 1:
        return S
    
    currentS = {}
    prevS = generateExtensions(S, n-1)
    
    for qi, pqi in prevS.items():
        for si, pi in S.items():
            currentS[ qi + si ] = pqi * pi
    return currentS


def main():
    S = [ item.strip() for item in (input("S: ")).split(",")]
    P = eval( input("P: ") )
    n = int(input("n: "))
    
    Sn = generateExtensions( dict(zip(S,P)), n )

    print( calculateH(list(Sn.values())) )
    print( calculateHn(list(P), n) )

    Sn = generateExtensions( dict(zip(S,P)), n + 1 )

    print( calculateH(list(Sn.values())) )
    print( calculateHn(list(P), n + 1) )

main()