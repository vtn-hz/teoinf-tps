exec(open("./utils/canales/posteriori/entropy_media.py").read())
exec(open("./utils/canales/posteriori/probs.py").read())

exec(open("./utils/canales/priori/entropy.py").read())

def informacionMutuaAB( Pa :list, channel: list[list] ) -> float:
    return calculateHPriori(Pa) -  calculateHPosterioriMediaAB(Pa, channel)


def informacionMutuaBA( Pa :list, channel: list[list] ) -> float:
    outP = getProbsOutSymbols(Pa, channel)
    outChannel = getMatrixTraspuesta(getPosterioriMatrix(Pa, channel))

    Hb = calculateH( outP )
    return Hb - calculateHPosterioriMediaAB(outP, outChannel)
    