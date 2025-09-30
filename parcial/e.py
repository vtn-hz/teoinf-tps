import math

def getOcurrences( phrase: str ) -> dict:
    occurrences = {}

    for si in phrase:
        if not (si in occurrences):
            occurrences[si] = 0
        occurrences[si] += 1
    
    return occurrences

'''
@return dictionary: { letra: porcentaje aparicion } 
'''
def buildS ( source: str ) -> dict:
    occurrences = getOcurrences( source )
    return { si:cant/len(source) for si, cant in occurrences.items() }

def generateExtensionsFromLL(alf: list, prob: list, n: int) -> list:
    if n == 1:
        return alf, prob
    
    P = []
    S = []

    prevS, prevP = generateExtensionsFromLL(alf, prob, n-1)
    
    for i, phrase  in enumerate(prevS):
        for j, symbol in enumerate(alf):
            S.append( phrase + symbol )
            P.append( prevP[i] * prob[j] )
    return S, P 

def calculateI(pi: float) -> float:
    return math.log2(1/pi); 

def calculateH(P: list) -> float:
    return sum([
        pi*calculateI(pi) 
        for pi in P
    ])

def main():
    data = input("data: ")
    S = buildS(data) 
    n = 2

    sn, pn =  generateExtensionsFromLL( list(S.keys()), list(S.values()), n)
    Sn = dict( zip(sn, pn) )

    sumatory = 0 

    for si, pi in Sn.items():
        print("si: ", si, " pi:", pi) 
        print("si: ", si, " pi:", round(pi, 2)) 
        print("-----------------")
        sumatory += pi

    
    print("---", sumatory, "---")

    print( 'H(Sn):',calculateH( list( Sn.values() ) ) )
    print( 'n*H(S):', n*calculateH( list( S.values() ) ) )
    print( 'round(n*H(S)):', round(n*calculateH( list( S.values() ) ), 2) )
main()