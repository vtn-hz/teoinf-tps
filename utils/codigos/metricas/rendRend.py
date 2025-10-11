exec(open("./utils/fuente_nula/calculateH.py").read())
exec(open("./utils/codigos/metadataCodigo.py").read())

def rendimientoCodigo( C: list, P: list):
    H = calculateH(P)
    Lmed = getLengthMedCodigo(C, P)

    return H / Lmed


def redundanciaCodigo( C: list, P: list):
    return 1 - rendimientoCodigo(C, P)