import math

def calculateI(pi: float) -> float:
    return math.log2(1/pi); 

def calculateH(P: list) -> float:
    return sum([
        pi*calculateI(pi) 
        for pi in P
    ])

def getBinaryP( w: float ) -> list:
    return [w, 1 - w]

def main():
    w = float(input("w: "))
    P = getBinaryP( w )
    

    print( [calculateI(pi) for  pi in P] )
    print( calculateH(P) )

main()