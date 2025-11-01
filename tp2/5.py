from utils.fuente_nula.calculateH import calculateH
from utils.fuente_nula.alfabetoS import buildS, getSymbolOcurrences

def main():
    source = input("fuente: ")

    S = buildS(source)

    print( S )
    print( calculateH( list(S.values()) ) )

main()