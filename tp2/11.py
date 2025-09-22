exec(open("./utils/fuente_nula/extensiones/extensionGenerator.py").read())
exec(open("./utils/fuente_nula/extensiones/calculateHn.py").read())


def main():
    S = [ item.strip() for item in (input("S: ")).split(",")]
    P = eval( input("P: ") )
    n = int(input("n: "))
    
    Sn = generateExtensions( dict(zip(S,P)), n )

    print( calculateH(list(Sn.values())) )
    print( calculateHn(list(P), n) )

    Sn = generateExtensions( dict(zip(S,P)), n + 1 )

    print( calculateH(list(Sn.values())) )
    print( calculateHn(list(P), n + 1) )

main()