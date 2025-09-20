import math

def calculateI(pi: float) -> float:
    return math.log2(1/pi); 

def calculateH(P: list) -> float:
    return sum([
        pi*calculateI(pi) 
        for pi in P
    ])

def main():
    rawData = input("list: ")
    P = eval(rawData)
    

    print( [calculateI(pi) for  pi in P] )
    print( calculateH(P) )

main()