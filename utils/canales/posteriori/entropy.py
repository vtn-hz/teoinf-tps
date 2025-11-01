from utils.fuente_nula.calculateH import calculateH
from utils.canales.posteriori.probs import getPosterioriMatrix, getProbsOutSymbols


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



def calculateHPosterioriTotal( Pa :list, channel: list[list] ) -> list:
    return calculateH( getProbsOutSymbols(Pa, channel) )

