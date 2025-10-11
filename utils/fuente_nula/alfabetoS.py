

def getSymbolOcurrences( phrase: str ) -> dict:
    occurrences = {}

    for si in phrase:
        if not (si in occurrences):
            occurrences[si] = 0
        occurrences[si] += 1
    
    return occurrences


# @return dictionary: { letra: porcentaje aparicion } 
def buildS(source: str) -> dict:
    occurrences = getSymbolOcurrences(source)
    frequencies = {symbol: count / len(source) for symbol, count in occurrences.items()}
    
    return dict(sorted(frequencies.items(), key=lambda item: item[0]))
