
def initializeHuffman(P: list) -> list:
    result = []
    for i, p in enumerate(P):
        result.append( (p, [i]) )
    return result


def huffmanAlgorithm(result: list, P: list) -> list:

    huffman = initializeHuffman(P)
    huffman.sort(key=lambda x: x[0], reverse=True)

    while len(huffman) > 1:
        (p1, c1) = huffman.pop()
        (p2, c2) = huffman.pop()

        for i in c1:
            result[i] = '0' + result[i]
        for i in c2:
            result[i] = '1' + result[i]

        huffman.append( (p1 + p2, c1 + c2) )
        huffman.sort(key=lambda x: x[0], reverse=True)

    return result

# def huffman(S: list, P: list) -> list:
#     result = [''] * len(S)
#     return huffmanAlgorithm(result, P)

def huffman(P: list) -> list:
    result = [''] * len(P)
    return huffmanAlgorithm(result, P)
    