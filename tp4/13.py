exec(open("./utils/fuente_nula/calculateH.py").read())

exec(open("./utils/codigos/algorithm/shannonfano.py").read())
exec(open("./utils/codigos/algorithm/huffman.py").read())

exec(open("./utils/codigos/metricas/rendRend.py").read())


exec(open("./utils/codigos/metricas/rendRend.py").read())
exec(open("./utils/fuente_nula/alfabetoS.py").read())


def printTable(P, C1, C2):
    print(f"{'Símbolo':<10} {'Prob':<10} {'Huffman':<15} {'Len':<5} {'Shannon-Fano':<15} {'Len':<5}")
    print("-" * 70)
    for i, (p, c1i, c2i) in enumerate(zip(P, C1, C2), start=1):
        print(f"{'S'+str(i):<10} {p:<10.3f} {c1i:<15} {len(c1i):<5} {c2i:<15} {len(c2i):<5}")


def printMetrics(C1, C2, P):
    """
    Imprime una tabla con las métricas principales:
    - Longitud media
    - Rendimiento
    - Redundancia
    """
    print("\nMétricas:")
    print(f"{'Código':<15}{'Long. media':<15}{'Rendimiento':<15}{'Redundancia':<15}")
    print("-" * 60)

    for nombre, C in [("Huffman", C1), ("Shannon-Fano", C2)]:
        Lmed = getLengthMedCodigo(C, P)
        rend = rendimientoCodigo(C, P)
        redund = redundanciaCodigo(C, P)
        print(f"{nombre:<15}{Lmed:<15.4f}{rend:<15.4f}{redund:<15.4f}")



def main() -> None:
    message = '58784784525368669895745123656253698989656452121702300223659'
    S = buildS( message )
    P = list( S.values() ) 

    H = calculateH(P)
    print(f"Entropía de la fuente (H): {H:.4f}\n")

    C1 = huffman(P)
    C2 = shannonfano(P)

    printTable(P, C1, C2)
    printMetrics(C1, C2, P)

main()
