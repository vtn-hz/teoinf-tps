from utils.fuente_nula.calculateH import calculateH
from utils.fuente_nula.calculateI import calculateI

def main():
    rawData = input("list: ")
    P = eval(rawData)
    

    print( [calculateI(pi) for  pi in P] )
    print( calculateH(P) )

main()