import random

def generateAcumulatedGaps( probability ):
    last = 0
    result = []
    for p in probability:
        result.append([last, last+p])
        last = last+p
        
    return result

def simulateSimbol( symbols, gaps ):
    rdm = random.uniform(0, 1)
    i = 0
    while (i < len(gaps) and not (gaps[i][0] <= rdm and rdm <= gaps[i][1])):
        i += 1
        
    return symbols[i]

def simulateFuente( symbols, probability, iterations):
    gaps = generateAcumulatedGaps(probability)
    fuente = []

    while (iterations):
        fuente.append( simulateSimbol(symbols, gaps) )
        iterations -= 1
    
    return fuente

distri = [
    ['A', 'a', 'b', 'c', 'z', 'az', 'lorem'], 
    [0.125, 0.25, 0.1875, 0.125, 0.125, 0.125, 0.0625]
]

result = simulateFuente(distri[0], distri[1], 30)
print(result)