exec(open("./utils/canales/posteriori/entropy_media.py").read())
exec(open("./utils/canales/posteriori/probs.py").read())

exec(open("./utils/canales/priori/entropy.py").read())

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