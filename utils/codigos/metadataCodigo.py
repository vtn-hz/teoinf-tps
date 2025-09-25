
def getAlfabetoCodigo (cods: list) -> list:
    alfCod = set()

    for cod in cods:
        alfCod.update(cod)

    return list(alfCod)

def getLengthsCodigo (cods: list) -> list:
    return [ len(cod) for cod in cods ] 

def getLengthMedCodigo(cods: list, pbs: float) -> float:
    l = getLengthsCodigo( cods )

    return sum([
        li * pbi
        for li, pbi in zip(l, pbs)
    ])
