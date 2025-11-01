from utils.codigos.calculateHr import calculateHr
from utils.codigos.metadataCodigo import getAlfabetoCodigo, getLengthMedCodigo
from utils.fuente_nula.extensiones.extensionGenerator import generateExtensionsFromLL
from utils.fuente_nula.extensiones.extensionP import generateExtensionsP

def teoremaShannon( C: list, P: list, n: int) -> bool:
    r = len( getAlfabetoCodigo(C) )

    if len(P) < len(C):
        P = generateExtensionsP(P, n)
        if len(P) != len(C):
            RaiseError("La cantidad de probabilidades no coincide con la cantidad de palabras del código")
 
    Lmed = getLengthMedCodigo(C, P)
    nHr = calculateHr(P, r)

    return nHr/n <= Lmed/n and Lmed/n <= nHr/n + 1/n


def teoremaShannonExtending( C: list, P: list, n: int) -> bool:
    r = len( getAlfabetoCodigo(C) )
    Hr = calculateHr(P, r) 

    C, P = generateExtensionsFromLL(C, P, n)

    Lmed = getLengthMedCodigo(C, P)
    

    return Hr <= Lmed/n and Lmed/n <= Hr + 1/n
