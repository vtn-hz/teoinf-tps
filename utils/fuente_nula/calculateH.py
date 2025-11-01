from utils.fuente_nula.calculateI import calculateI

# entropía: H = Σ pi * I(pi)
def calculateH(P: list) -> float:
    return sum([
        pi*calculateI(pi) 
        for pi in P
    ])
