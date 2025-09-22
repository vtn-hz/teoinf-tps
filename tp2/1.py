exec(open("./utils/fuente_nula/calculateH.py").read())


def main():
    P = [0.5 , 0.2, 0.3]

    print( [calculateI(pi) for  pi in P] )
    print( calculateH(P) )

main()