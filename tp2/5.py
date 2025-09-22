exec(open("./utils/fuente_nula/calculateH.py").read())
exec(open("./utils/fuente_nula/alfabetoS.py").read())

def main():
    source = input("fuente: ")

    S = buildS(source)

    print( S )
    print( calculateH( list(S.values()) ) )

main()