import math

from utils.canales.posteriori.entropy import calculateHPosteriori
from utils.canales.posteriori.probs import getProbsOutSymbols, getMatrixSimultaneusEvent, getPosterioriMatrix
from utils.matrix import getMatrixTraspuesta


def calculateHPosterioriMediaAB( Pa :list, channel: list[list] ) -> float:
    Hpost = calculateHPosteriori(Pa, channel)
    Pout = getProbsOutSymbols(Pa,channel)

    result = 0
    for pi, hb in zip(Pout, Hpost):
        result += pi * hb
    
    return result

def calculateHPosterioriMediaABSimple( Pa :list, channel: list[list] ) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    antiChannel = getPosterioriMatrix(Pa, channel)


    result = 0
    for i in range( len(channel) ):
        for j in range( len(channel[0]) ):
            if antiChannel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1/antiChannel[i][j])
    
    return result

def calculateRuido(Pa :list, channel: list[list] ) -> float:
    return calculateHPosterioriMediaABSimple(Pa, channel)

def calculateHPosterioriMediaBA( Pa :list, channel: list[list] ) -> float:
    antiChannel = getPosterioriMatrix(Pa, channel)
    Pout = getProbsOutSymbols(Pa,channel)

    Hpost = calculateHPosteriori(Pout, getMatrixTraspuesta(antiChannel))
    
    result = 0
    for pi, hb in zip(Pa, Hpost):
        result += pi * hb
    
    return result

def calculateHPosterioriMediaBASimple( Pa :list, channel: list[list] ) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)

    result = 0
    for i in range( len(channel) ):
        for j in range( len(channel[0]) ):
            if channel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1/channel[i][j])
    
    return result

def calculatePerdida(Pa: list, channel: list[list]):
    return calculateHPosterioriMediaBASimple(Pa, channel)
