exec(open("./utils/fuente_nula/calculateH.py").read())
exec(open("./utils/canales/posteriori/probs.py").read())


def calculateHPosteriori( Pa :list, channel: list[list] ) -> list:
    afterchannel = getPosterioriMatrix(Pa, channel)
    result = []
    for j in range( len(afterchannel[0]) ):
        collectedPbs = []
        for i in range( len(afterchannel) ):
            if afterchannel[i][j] > 0:  
                collectedPbs.append( afterchannel[i][j] )
        result.append( calculateH( collectedPbs ) )
    
    return result
