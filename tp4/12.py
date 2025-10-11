exec(open("./utils/fuente_nula/calculateH.py").read())
exec(open("./utils/codigos/algorithm/shannonfano.py").read())
exec(open("./utils/codigos/algorithm/huffman.py").read())

exec(open("./utils/codigos/metricas/rendRend.py").read())
exec(open("./utils/codigos/metadataCodigo.py").read())


def printTable(P, C1, C2):
    print(f"{'Símbolo':<10} {'Prob':<10} {'Huffman':<15} {'Len':<5} {'Shannon-Fano':<15} {'Len':<5}")
    print("-" * 70)
    for i, (p, c1i, c2i) in enumerate(zip(P, C1, C2), start=1):
        print(f"{'S'+str(i):<10} {p:<10.3f} {c1i:<15} {len(c1i):<5} {c2i:<15} {len(c2i):<5}")


def drawTree(codes):
    """
    Dibuja un árbol binario ASCII a partir de una lista de códigos binarios.
    El 0 va a la izquierda y el 1 a la derecha.
    """

    tree = {}
    for code in codes:
        node = tree
        for bit in code:
            node = node.setdefault(bit, {})
        node["*"] = code  # marca hoja

    print("\nÁrbol del código:\n")

    def _draw(node, prefix=""):
        if "*" in node:
            print(prefix + "── " + node["*"])
            return
        if "0" in node:
            print(prefix + "├──0")
            _draw(node["0"], prefix + "│   ")
        if "1" in node:
            print(prefix + "└──1")
            _draw(node["1"], prefix + "    ")

    _draw(tree)

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
    P = [0.385, 0.154, 0.128, 0.154, 0.179]

    H = calculateH(P)
    print(f"Entropía de la fuente (H): {H:.4f}\n")

    C1 = huffman(P)
    C2 = shannonfano(P)

    printTable(P, C1, C2)
    printMetrics(C1, C2, P)
    
    print("\n\n--- Árbol Huffman ---")
    drawTree(C1)

    print("\n--- Árbol Shannon-Fano ---")
    drawTree(C2)


# === Ejecución ===
main()
