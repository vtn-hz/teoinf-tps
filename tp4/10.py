from utils.fuente_nula.alfabetoS import buildS, getSymbolOcurrences
from utils.codigos.algorithm.shannonfano import shannonfano
from utils.codigos.algorithm.huffman import huffman


# === Función para imprimir tabla ===
def printTable(S, C1, C2):
    print(f"{'Símbolo':<10} {'Prob':<10} {'Huffman':<15} {'Len':<5} {'Shannon-Fano':<15} {'Len':<5}")
    print("-" * 65)
    for (symbol, prob), c1i, c2i in zip(S.items(), C1, C2):
        print(f"{symbol:<10} {round(prob, 2):<10} {str(c1i):<15} {len(c1i):<5} {str(c2i):<15} {len(c2i):<5}")


# === Función principal ===
def main() -> None:
    msg1 = 'ABCDABCBDCBAAABBBCBCBABADBCBABCBDBCCCAAABB'
    msg2 = 'AOEAOEOOOOEOAOEOOEOOEOAOAOEOEUUUIEOEOEO'

    # Construcción de distribuciones
    S1 = buildS(msg1)
    S2 = buildS(msg2)

    # Generación de códigos
    C1 = huffman(list(S1.values()))
    C2 = shannonfano(list(S1.values()))

    # Impresión de resultados
    printTable(S1, C1, C2)

    print()

    # Generación de códigos
    C1 = huffman(list(S2.values()))
    C2 = shannonfano(list(S2.values()))

    # Impresión de resultados
    printTable(S2, C1, C2)


# === Ejecución del programa ===
main()
