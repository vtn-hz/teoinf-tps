
def buildS2( source: str ) -> str:
    symbols = sorted(set( source ))
    S = []
    P = []

    for s1 in symbols:
        currentP = []
        for s2 in symbols:
            S.append( s1 + s2 )
            currentP.append( source.count(s1 + s2) )
        
        for pi in currentP:
            P.append( pi/sum(currentP) if sum(currentP) != 0 else 0 )
    
    return dict(zip(S, P))
    