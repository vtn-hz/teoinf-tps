import math

def getOcurrences( phrase: str ) -> dict:
    occurrences = {}

    for si in phrase:
        if not (si in occurrences):
            occurrences[si] = 0
        occurrences[si] += 1
    
    return occurrences

def buildS ( source: str ) -> dict:
    occurrences = getOcurrences( source )
    return { si:cant/len(source) for si, cant in occurrences.items() }

def calculateI(pi: float) -> float:
    return math.log2(1/pi); 

def calculateH(P: list) -> float:
    return sum([
        pi*calculateI(pi) 
        for pi in P
    ])

def main():
    source = input("fuente: ")

    S = buildS(source)

    print( S )
    print( calculateH( list(S.values()) ) )

main()