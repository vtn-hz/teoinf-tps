import math

from utils.canales.posteriori.entropy_media import calculateHPosterioriMediaAB
from utils.canales.posteriori.probs import getProbsOutSymbols, getMatrixSimultaneusEvent, getPosterioriMatrix
from utils.canales.priori.entropy import calculateHPriori
from utils.fuente_nula.calculateH import calculateH
from utils.matrix import getMatrixTraspuesta

def informacionMutuaAB( Pa :list, channel: list[list] ) -> float:
    return calculateHPriori(Pa) -  calculateHPosterioriMediaAB(Pa, channel)

def informacionMutuaABSimple(Pa: list, channel: list[list]) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    outProbs = getProbsOutSymbols(Pa, channel)

    result = 0.0
    for i in range(len(simulaneusEvent)):
        for j in range(len(simulaneusEvent[0])):
            if simulaneusEvent[i][j] > 0 and outProbs[j] > 0 and Pa[i] > 0:
                result += simulaneusEvent[i][j] * math.log2(simulaneusEvent[i][j] / (Pa[i] * outProbs[j]))

    return result

def informacionMutuaBA( Pa :list, channel: list[list] ) -> float:
    outP = getProbsOutSymbols(Pa, channel)
    outChannel = getMatrixTraspuesta(getPosterioriMatrix(Pa, channel))

    Hb = calculateH( outP )
    return Hb - calculateHPosterioriMediaAB(outP, outChannel)
    

def informacionMutuaBASimple(Pa: list, channel: list[list]) -> float:
    # Calcular P(B) y P(A|B)
    antiChannel = getPosterioriMatrix(Pa, channel)  # P(A|B)
    outProbs = getProbsOutSymbols(Pa, channel)      # P(bj)

    simulaneusEvent = getMatrixSimultaneusEvent(outProbs, antiChannel, isByRow=False)

    result = 0.0
    for i in range(len(simulaneusEvent)):
        for j in range(len(simulaneusEvent[0])):
            if simulaneusEvent[i][j] > 0 and outProbs[j] > 0 and Pa[i] > 0:
                result += simulaneusEvent[i][j] * math.log2(simulaneusEvent[i][j] / (outProbs[j] * Pa[i]))

    return result