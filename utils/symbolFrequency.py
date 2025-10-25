

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
    occurrences = dict( sorted(getOcurrences( source ).items()) )
    return { si:cant/len(source) for si, cant in occurrences.items() }
