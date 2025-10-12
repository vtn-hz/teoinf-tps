exec(open("./utils/codigos/algorithm/shannonfano.py").read())
exec(open("./utils/codigos/algorithm/huffman.py").read())

exec(open("./utils/codigos/metricas/rendRend.py").read())
exec(open("./utils/codificacion/metricas.py").read())

exec(open("./utils/codificacion/huffman_shannon/decode_encode.py").read())
exec(open("./utils/codificacion/memory_decode_encode.py").read())

def printMetricas( message: str, C: list, P: list  , encoded:bytearray ):
    print(f"Tasa compresion: { tasaCompresion(message, encoded) } | Rendimiento: { rendimientoCodigo(C, P) } | Redundancia: { redundanciaCodigo(C, P) }")

def main() -> None:
    alfabeto = [
        " ", ",", ".", ":", ";", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
        "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

    probs = [
        0.175990, 0.014093, 0.015034, 0.000542, 0.002109, 0.111066, 0.015368, 0.030176,
        0.038747, 0.101604, 0.004873, 0.008762, 0.007953, 0.049740, 0.003706, 0.000034,
        0.048149, 0.021041, 0.050490, 0.002018, 0.073793, 0.019583, 0.010246, 0.051446,
        0.058406, 0.031093, 0.033240, 0.008930, 0.000012, 0.000706, 0.007851, 0.003199,
    ]
    
    C_huffman = huffman( probs )
    C_shannon = shannonfano( probs )

    print('-- Modo --')
    mode = input(' save (s) / recover (r) ')
    if mode == 's':
        message = input('message: ')
        encode1 =  codificar( message, alfabeto, C_huffman )
        encode2 =  codificar( message, alfabeto, C_shannon )

        saveComprimido( encode1, "ej17_huffman" )
        saveComprimido( encode2, "ej17_shannon" )


        print("- ej17_huffman -")
        printMetricas( message, C_huffman, probs, encode1 )
        print("- ej17_shannon -")
        printMetricas( message, C_shannon, probs, encode2 )
    else:
        filename = input("filename: ")
        Ctype = input("codified by: ")

        C = C_huffman if Ctype == "huffman" else C_shannon
        encoded = recoverComprimido( filename )
        message = decodificar( encoded, C, alfabeto )

        print("message: " + message)
        printMetricas( message, C, probs, encoded )


main()
