from utils.fuente_nula.calculateH import calculateH
from utils.codigos.metadataCodigo import getLengthMedCodigo

def rendimientoCodigo( C: list, P: list):
    H = calculateH(P)
    Lmed = getLengthMedCodigo(C, P)

    return H / Lmed


def redundanciaCodigo( C: list, P: list):
    return 1 - rendimientoCodigo(C, P)