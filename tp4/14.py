from utils.codigos.teoremaShannon import teoremaShannon, teoremaShannonExtending
from utils.codificacion.huffman_shannon.decode_encode import codificar, decodificar, codificar_dict, decodificar_dict


def main() -> None:
    S1 = ['A', 'B', 'C']
    C1 = ["11", "010", "00"]
    P1 = [0.5, 0.2, 0.3]
    
    strs = [ "ABACBAACABABAACBABA", "BACBAAABAAACBABACAB", "CBAABACBABAAACABABA"]

    for item in strs:
        encoded = codificar(item, S1, C1)
        solved = solve_byteArray( encoded )

        print("".join(map(str, list(solved))))
        print( decodificar(encoded, C1, S1) )


main()
