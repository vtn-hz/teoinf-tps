exec(open("./utils/fuente_nula/calculateH.py").read())

def main():
    rawData = input("list: ")
    P = eval(rawData)
    

    print( [calculateI(pi) for  pi in P] )
    print( calculateH(P) )

main()