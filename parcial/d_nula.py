import math

def calculateI(pi: float) -> float:
    return math.log2(1/pi); 

def calculateH(P: list) -> float:
    return sum([
        pi*calculateI(pi) 
        for pi in P
    ])


def main():
    # 1. 0.142857, 0.142857, 0.428571, 0.285714


    data = [ float(pi.strip()) for pi in input("P: ").split(',') ]
    print(data)
    print("H(r=2): ", calculateH( data ))
    

main()