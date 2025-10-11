def initializeShannonFano ( P: list ) -> list:
    return sorted([ [pi, i] for i, pi in enumerate(P) ], key=lambda item: item[0], reverse=True)


def propagateSubfix( result: list, P: list[list], fix: str ) -> list:
    for pi, i in P:
        result[i] +=  fix 

def shannonfanoAlgorithm ( result: list, Pindex: list  ):
    if len(Pindex) <= 1:
        return

    # calculate split
    total = sum( [ pi for pi, i in Pindex ]) / 2 

    acum = 0
    lastDif = 1 
    splitLocation = -1


    for i, pi in enumerate(Pindex):
        acum += pi[0]

        if acum >= total:
            if min(lastDif, abs(total - acum)) == lastDif:
                splitLocation = i
            else:
                splitLocation = i + 1
            
            firstPart = Pindex[:splitLocation]
            secondPart = Pindex[splitLocation:]

            propagateSubfix( result, firstPart, '1' )
            propagateSubfix( result, secondPart, '0' )

            shannonfanoAlgorithm( result, firstPart)
            shannonfanoAlgorithm( result, secondPart)

            return
                
        lastDif = total - acum

# def shannonfano( S: list, P: list ) -> list:
#     result = [''] * len(S)
#     Pindex = initializeShannonFano(P)
#     shannonfanoAlgorithm(result, Pindex)
#     return result

def shannonfano(P: list) -> list:
    result = [''] * len(P)
    Pindex = initializeShannonFano(P)
    shannonfanoAlgorithm(result, Pindex)
    return result