from utils.fuente_nula.calculateH import calculateH
from utils.fuente_nula.calculateI import calculateI


def main():
    P = [0.5 , 0.2, 0.3]

    print( [calculateI(pi) for  pi in P] )
    print( calculateH(P) )

main()