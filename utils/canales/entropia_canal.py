from utils.canales.posteriori.entropy import calculateHPosteriori
from utils.canales.posteriori.probs import getMatrixSimultaneusEvent, getProbsOutSymbols
from utils.fuente_nula.calculateI import calculateI


def calculateHCanal( Pa :list, channel: list[list] ) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    result = 0.0

    for row in simulaneusEvent:
        for item in row:
            if item > 0:
                result += item*calculateI(item)

    return result

def calculateHAfinCanal( Pa :list, channel: list[list] ) -> float:
    return calculateHCanal(Pa, channel)