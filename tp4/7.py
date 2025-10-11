exec(open("./utils/codigos/teoremaShannon.py").read())
exec(open("./utils/codigos/metricas/rendRend.py").read())

exec(open("utils/fuente_nula/extensiones/extensionP.py").read())

def main() -> None:
    S = [ "A", "B", "C" ]
    C1 = ["11", "010", "00"]
    C2 = ["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111"]
    P1 = [0.5, 0.2, 0.3]

    n = rendimientoCodigo(C1, P1)
    R = redundanciaCodigo(C1, P1)
    print(n)
    print(R)
    print('---')
    n = rendimientoCodigo(C2, generateExtensionsP(P1, 2))
    R = redundanciaCodigo(C2, generateExtensionsP(P1, 2))
    print(n)
    print(R)

main()
