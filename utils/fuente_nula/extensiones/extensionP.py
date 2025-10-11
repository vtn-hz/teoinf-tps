
def generateExtensionsP(prob: list, n: int) -> list:
    if n == 1:
        return prob
    
    P = []
    prevP = generateExtensionsP(prob, n-1)
    
    for pi  in prob:
        for pj in prevP:
            P.append( pi * pj )
    return P 
