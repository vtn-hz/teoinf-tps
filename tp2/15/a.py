from utils.fuente_no_nula.fuente_markov.generateMatrixTransicion import generateMatrixTransicion
from utils.fuente_nula.alfabetoS import buildS, getSymbolOcurrences
from utils.fuente_no_nula.fuente_markov.alfabetoS2 import buildS2


def main():
    _str = "AABBAABACAACCCCAA"

    print(buildS(_str))
    print(buildS2(_str))
    print(generateMatrixTransicion(_str))

main()