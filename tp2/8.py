from utils.fuente_nula.calculateH import calculateH
from utils.fuente_nula.calculateI import calculateI

# fuente binaria
def getBinaryP( w: float ) -> list:
    return [w, 1 - w]

def main():
    w = float(input("w: "))
    P = getBinaryP( w )
    

    print( [calculateI(pi) for  pi in P] )
    print( calculateH(P) )

main()