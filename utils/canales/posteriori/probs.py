exec(open("./utils/matrix.py").read())

def getProbsOutSymbols( Pinitial: list, channel: list[list]) -> list:
    result = [ 0.0 ] * len(channel[0])

    for j in range(len(channel[0])):
        for i in range(len(channel)):
            result[j] += channel[i][j]*Pinitial[i]

    return result

def getPosterioriMatrix( Pinitial: list, channel: list[list]):
    result = getMatrixZeros( len(channel), len(channel[0]) )
    outsSymbProbs = getProbsOutSymbols( Pinitial, channel )

    for i in range(len(channel)):
        for j in range(len(channel[0])):
            result[i][j] = channel[i][j]

            if outsSymbProbs[j] != 0:
                result[i][j] *= Pinitial[i]/outsSymbProbs[j]
    
    return result

def getMatrixSimultaneusEvent( Pinitial: list, channel: list[list]):
    result = getMatrixZeros( len(channel), len(channel[0]) )

    for i in range(len(channel)):
        for j in range(len(channel[0])):
            result[i][j] = channel[i][j] * Pinitial[i]
    
    return result