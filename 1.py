import math

def calculateI(p):
    return math.log2(1/p); 

def getIDistribution(P):
    return [calculateI(item) for item in l]

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
l = [0.5 , 0.2, 0.3]

print( getIDistribution(l) )
print( calculateH(l) )