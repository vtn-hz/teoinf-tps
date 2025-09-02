
def generateExtensions(alf: list, prob: list, n: int):
    # ... 

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

def main():
    S = ['1', '2', '3', '4', '5', '6']
    Sp = [1/6]*6
    n = int( input('n: ') )

    result = []

    print( generateExtensions(S, Sp, result, [], 0, n) )
    print("\n")



main()