from utils.matrix import *  

def isCanalNoRuido (channel : list[list]) -> bool:
    
    for j in range(len(channel[0])):
        amount = 0
        for i in  range(len(channel)):
            amount += int(channel[i][j] != 0)

            if amount > 1:
                return False
    
    return True

def isCanalDeterminante (channel : list[list]) -> bool:
    
    for i in range(len(channel)):
        amount = 0
        for j in  range(len(channel[0])):
            amount += int(channel[i][j] != 0)

            if amount > 1:
                return False
        
        if amount == 0:
            return False
    
    return True

def isCanalSimetricoMariAesteticCoding(channel : list[list]) -> bool:
    acums = {}

    if len(channel) != len(channel[0]):
        return False

    # initialize acums
    for i in range( len(channel[0]) ):
        acums[ channel[0][i] ] = [i]

    if len(acums) != len( channel[0] ):
        return False
    
    for i in range(1, len(channel) ):
        for j in range( len(channel[0]) ):
            pij = channel[i][j]

            if pij not in acums:
                return False
            
            if j not in acums[ pij ]:
                acums[ pij ].append(j)
            else:
                return False
    
    return True


def isCanalSimetrico(channel : list[list]) -> bool:

    if len(channel) != len(channel[0]):
        return False

    for i in range(len(channel)):
        probs       = list(channel[0])
        probsanti   = list(channel[0]) 
        
        for j in range(len(channel[0])):
            if channel[i][j] in probs:
                probs.remove( channel[i][j] )

            if channel[j][i] in probsanti:
                probsanti.remove( channel[j][i] )
        
        if probs or probsanti:
            return False
            
    return True

def isCanalUniforme(channel : list[list]) -> bool:

    for i in range(1, len(channel) ):
        probs = list( channel[0] )

        for j in range( len(channel[0]) ):
            pij = channel[i][j]

            if(pij in probs ):
                probs.remove( pij )

        if probs:
            return False
    
    return True
