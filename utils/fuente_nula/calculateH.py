exec(open("./utils/fuente_nula/calculateI.py").read())

# entropía: H = Σ pi * I(pi)
def calculateH(P: list) -> float:
    return sum([
        pi*calculateI(pi) 
        for pi in P
    ])
