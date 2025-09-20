import math

def calculateI(pi: float) -> float:
    return math.log2(1/pi); 

def calculateH(P: list) -> float:
    return sum([
        pi*calculateI(pi) 
        for pi in P
    ])

def main():
    P = [0.5 , 0.2, 0.3]

    print( [calculateI(pi) for  pi in P] )
    print( calculateH(P) )

main()