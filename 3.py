import math

def calculateI(p):
    return math.log2(1/p); 

def getIDistribution(P):
    return [calculateI(item) for item in P]

def calculateH(P):
    return sum ([ 
        Pi * Ii
        for Pi, Ii in  
        zip(P, getIDistribution(P))
    ]); 

"""
def calculateH(P):
    H = 0
    i = 0

    for item in getIDistribution(p):
        H += P[i] * item
        i += 1;

"""

# P(1) = 1/9, P(2) = 1/6, P(3) = 1/9, P(4) = 1/9, P(5) = 1/6, P(6) = 1/3

l = [1/9, 1/6, 1/9, 1/9, 1/6, 1/3]
print(l)
print( getIDistribution(l) )
print( calculateH(l) )
