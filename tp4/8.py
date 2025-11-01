from utils.codigos.metricas.rendRend import rendimientoCodigo, redundanciaCodigo

def main() -> None:
    S = [ "A", "B", "C", "D", "E" ]
    P = [0.2, 0.15, 0.1, 0.3, 0.25]

    print(sum(P))

    C1 = [
        "01", "111", "110",
        "101", "100"
    ]

    C2 = [
        "00", "01", "10",
        "110", "111"
    ]

    C3 = [
        "0110", "010", "0111",
        "1", "00"
    ]

    C4 = [
        "11", "001", "000",
        "10", "01"
    ]

    n = rendimientoCodigo(C1, P)
    R = redundanciaCodigo(C1, P)
    print(n)
    print(R)
    print('---')
    n = rendimientoCodigo(C2, P)
    R = redundanciaCodigo(C2, P)
    print(n)
    print(R)
    print('---')
    n = rendimientoCodigo(C3, P)
    R = redundanciaCodigo(C3, P)
    print(n)
    print(R)
    print('---')
    n = rendimientoCodigo(C4, P)
    R = redundanciaCodigo(C4, P)
    print(n)
    print(R)
    print('---')

main()
