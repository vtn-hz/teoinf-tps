exec(open("./utils/fuente_nula/calculateH.py").read())


def calculateHn(P: list, n: int) -> float:
    return n*calculateH(P)