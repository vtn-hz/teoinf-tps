exec(open("./utils/canales/posteriori/entropy.py").read())
exec(open("./utils/canales/posteriori/probs.py").read())


def calculateHPosterioriMediaAB( Pa :list, channel: list[list] ) -> float:
    Hpost = calculateHPosteriori(Pa, channel)
    Pout = getProbsOutSymbols(Pa,channel)

    result = 0
    for pi, hb in zip(Pout, Hpost):
        result += pi * hb
    
    return result

def calculateRuido(Pa :list, channel: list[list] ) -> float:
    return calculateHPosterioriMediaAB(Pa, channel)

def calculateHPosterioriMediaBA( Pa :list, channel: list[list] ) -> float:
    antiChannel = getPosterioriMatrix(Pa, channel)
    Pout = getProbsOutSymbols(Pa,channel)

    Hpost = calculateHPosteriori(Pout, getMatrixTraspuesta(antiChannel))
    
    result = 0
    for pi, hb in zip(Pa, Hpost):
        result += pi * hb
    
    return result

def calculatePerdida(Pa: list, channel: list[list]):
    return calculateHPosterioriMediaBA(Pa, channel)
