import math

def calculateI(pi):
    if pi <= 0:
        raise ValueError('La probabilidad debe ser mayor que 0')
    return math.log2(1 / pi)

def calculateH(P):
    return sum((pi * calculateI(pi) for pi in P if pi > 0))

def getSymbolOcurrences(phrase):
    occurrences = {}
    for si in phrase:
        occurrences[si] = occurrences.get(si, 0) + 1
    return occurrences

def buildS(source):
    occurrences = getSymbolOcurrences(source)
    frequencies = {symbol: count / len(source) for symbol, count in occurrences.items()}
    return dict(sorted(frequencies.items(), key=lambda item: item[0]))

def initializeHuffman(P):
    result = []
    for i, p in enumerate(P):
        result.append((p, [i]))
    return result

def huffmanAlgorithm(result, P):
    huffman = initializeHuffman(P)
    huffman.sort(key=lambda x: x[0], reverse=True)
    while len(huffman) > 1:
        p1, c1 = huffman.pop()
        p2, c2 = huffman.pop()
        for i in c1:
            result[i] = '0' + result[i]
        for i in c2:
            result[i] = '1' + result[i]
        huffman.append((p1 + p2, c1 + c2))
        huffman.sort(key=lambda x: x[0], reverse=True)
    return result

def huffman(P):
    result = [''] * len(P)
    return huffmanAlgorithm(result, P)

def initializeShannonFano(P):
    return sorted([[pi, i] for i, pi in enumerate(P)], key=lambda item: item[0], reverse=True)

def propagateSubfix(result, P, fix):
    for pi, i in P:
        result[i] += fix

def shannonfanoAlgorithm(result, Pindex):
    if len(Pindex) <= 1:
        return
    total = sum((pi for pi, i in Pindex)) / 2
    acum = 0
    lastDif = float('inf')
    splitLocation = 0
    for idx, (pi, i) in enumerate(Pindex):
        acum += pi
        if acum >= total:
            if min(lastDif, abs(total - acum)) == lastDif:
                splitLocation = idx
            else:
                splitLocation = idx + 1
            firstPart = Pindex[:splitLocation]
            secondPart = Pindex[splitLocation:]
            propagateSubfix(result, firstPart, '1')
            propagateSubfix(result, secondPart, '0')
            shannonfanoAlgorithm(result, firstPart)
            shannonfanoAlgorithm(result, secondPart)
            return
        lastDif = abs(total - acum)

def shannonfano(P):
    result = [''] * len(P)
    Pindex = initializeShannonFano(P)
    shannonfanoAlgorithm(result, Pindex)
    return result

def getLengthsCodigo(cods):
    return [len(cod) for cod in cods]

def getLengthMedCodigo(cods, pbs):
    l = getLengthsCodigo(cods)
    return sum((li * pbi for li, pbi in zip(l, pbs)))

def rendimientoCodigo(C, P):
    H = calculateH(P)
    Lmed = getLengthMedCodigo(C, P)
    return H / Lmed

def redundanciaCodigo(C, P):
    return 1 - rendimientoCodigo(C, P)

def hamming(C):
    if len(C) <= 1:
        raise Exception("No hay cantidad de códigos suficientes")
    
    _min = []
    for i in range(len(C)):
        for j in range(i + 1, len(C)):
            dif_amount = sum(1 for k in range(len(C[i])) if C[i][k] != C[j][k])
            _min.append(dif_amount)
    
    return min(_min)

def erroresDetectables(C):
    return hamming(C) - 1

def erroresCorregibles(C):
    return (hamming(C) - 1) // 2

def getBinMatrixFromStr(message):
    binary_matrix = []
    for char in message:
        binary_row = list(map(int, format(ord(char), '07b')))
        binary_matrix.append(binary_row)
    return binary_matrix

def addHorizontalParity(matrix, par=True):
    for i in range(len(matrix)):
        bitAmount = 0 if par else 1
        for j in range(len(matrix[i])):
            bitAmount += matrix[i][j]
        matrix[i].append(bitAmount % 2)
    return matrix

def addVerticalParity(matrix, par=True):
    parityRow = [-1] * len(matrix[0])
    for j in range(len(matrix[0])):
        bitAmount = 0 if par else 1
        for i in range(len(matrix)):
            bitAmount += matrix[i][j]
        parityRow[j] = bitAmount % 2
    matrix.insert(0, parityRow)
    return matrix

def getMatrixMultiparidad(message, par=True):
    matrix = getBinMatrixFromStr(message)
    matrix = addHorizontalParity(matrix, par)
    matrix = addVerticalParity(matrix, par)
    return matrix

def printMatrix(matrix):
    for row in matrix:
        print('   ', end='')
        for bit in row:
            print(bit, end='')
        print()

def main():
    MENSAJE = "ABRACADABRA"

    print('=' * 70)
    print('UNIDAD 4: ANÁLISIS DE CÓDIGOS')
    print('=' * 70)
    
    print(f"\n1. MENSAJE A ANALIZAR")
    print(f"   Mensaje: '{MENSAJE}'")
    print(f"   Longitud: {len(MENSAJE)} símbolos")
    
    S = buildS(MENSAJE)
    simbolos = list(S.keys())
    probabilidades = list(S.values())
    
    print(f"\n2. ALFABETO Y PROBABILIDADES")
    print(f"   Alfabeto: {simbolos}")
    for simbolo, prob in S.items():
        ocurrencias = int(prob * len(MENSAJE))
        print(f"   P({simbolo}) = {prob:.4f} ({ocurrencias} ocurrencias)")
    
    H = calculateH(probabilidades)
    print(f"\n3. ENTROPÍA")
    print(f"   H(X) = {H:.4f} bits/símbolo")
    
    print(f"\n4. CÓDIGOS GENERADOS")
    C_huffman = huffman(probabilidades)
    C_shannon = shannonfano(probabilidades)
    
    print(f"\n   {'Símbolo':<10} {'P(X)':<12} {'Huffman':<15} {'Shannon-Fano':<15}")
    print(f"   {'-'*52}")
    for simbolo, prob, huff, shan in zip(simbolos, probabilidades, C_huffman, C_shannon):
        print(f"   {simbolo:<10} {prob:<12.4f} {huff:<15} {shan:<15}")
    
    print(f"\n5. MÉTRICAS DE CÓDIGOS")
    
    L_huffman = getLengthMedCodigo(C_huffman, probabilidades)
    rend_huffman = rendimientoCodigo(C_huffman, probabilidades)
    red_huffman = redundanciaCodigo(C_huffman, probabilidades)
    
    L_shannon = getLengthMedCodigo(C_shannon, probabilidades)
    rend_shannon = rendimientoCodigo(C_shannon, probabilidades)
    red_shannon = redundanciaCodigo(C_shannon, probabilidades)
    
    print(f"\n   {'Código':<20} {'Long. Media':<15} {'Rendimiento':<15} {'Redundancia':<15}")
    print(f"   {'-'*65}")
    print(f"   {'Huffman':<20} {L_huffman:<15.4f} {rend_huffman:<15.4f} {red_huffman:<15.4f}")
    print(f"   {'Shannon-Fano':<20} {L_shannon:<15.4f} {rend_shannon:<15.4f} {red_shannon:<15.4f}")
    
    print(f"\n6. RELACIONES MATEMÁTICAS")
    print(f"   Teorema de Shannon: H(X) ≤ L < H(X) + 1")
    print(f"   ")
    print(f"   Huffman:")
    print(f"     {H:.4f} ≤ {L_huffman:.4f} < {H + 1:.4f}")
    cumple_huff = H <= L_huffman < H + 1
    print(f"     Cumple: {'✓ SÍ' if cumple_huff else '✗ NO'}")
    print(f"   ")
    print(f"   Shannon-Fano:")
    print(f"     {H:.4f} ≤ {L_shannon:.4f} < {H + 1:.4f}")
    cumple_shan = H <= L_shannon < H + 1
    print(f"     Cumple: {'✓ SÍ' if cumple_shan else '✗ NO'}")
    
    print(f"\n   Rendimiento η = H(X) / L")
    print(f"     Huffman:      η = {H:.4f} / {L_huffman:.4f} = {rend_huffman:.4f}")
    print(f"     Shannon-Fano: η = {H:.4f} / {L_shannon:.4f} = {rend_shannon:.4f}")
    
    print(f"\n   Redundancia R = 1 - η")
    print(f"     Huffman:      R = 1 - {rend_huffman:.4f} = {red_huffman:.4f}")
    print(f"     Shannon-Fano: R = 1 - {rend_shannon:.4f} = {red_shannon:.4f}")
    
    print(f"\n7. CONTROL DE ERRORES")
    print(f"   Para códigos de longitud fija (ajustados con padding):")
    print(f"   ")
    
    max_len = max(len(c) for c in C_huffman)
    C_huffman_padded = [c.ljust(max_len, '0') for c in C_huffman]
    C_shannon_padded = [c.ljust(max_len, '0') for c in C_shannon]
    
    print(f"   Huffman (padded):")
    for simbolo, cod in zip(simbolos, C_huffman_padded):
        print(f"     {simbolo}: {cod}")
    
    try:
        d_huffman = hamming(C_huffman_padded)
        err_det_huffman = erroresDetectables(C_huffman_padded)
        err_corr_huffman = erroresCorregibles(C_huffman_padded)
        
        print(f"   ")
        print(f"   Distancia de Hamming (d):     {d_huffman}")
        print(f"   Errores detectables (d-1):    {err_det_huffman}")
        print(f"   Errores corregibles ⌊(d-1)/2⌋: {err_corr_huffman}")
    except Exception as e:
        print(f"   Error al calcular: {e}")
    
    print(f"   ")
    print(f"   Shannon-Fano (padded):")
    for simbolo, cod in zip(simbolos, C_shannon_padded):
        print(f"     {simbolo}: {cod}")
    
    try:
        d_shannon = hamming(C_shannon_padded)
        err_det_shannon = erroresDetectables(C_shannon_padded)
        err_corr_shannon = erroresCorregibles(C_shannon_padded)
        
        print(f"   ")
        print(f"   Distancia de Hamming (d):     {d_shannon}")
        print(f"   Errores detectables (d-1):    {err_det_shannon}")
        print(f"   Errores corregibles ⌊(d-1)/2⌋: {err_corr_shannon}")
    except Exception as e:
        print(f"   Error al calcular: {e}")
    
    print(f"\n8. MATRIZ DE PARIDAD (MULTIPARIDAD)")
    print(f"   Generando matriz de paridad para el mensaje...")
    print(f"   ")
    
    try:
        matriz_paridad = getMatrixMultiparidad(MENSAJE, par=True)
        print(f"   Matriz de paridad (paridad par):")
        print(f"   Filas: {len(matriz_paridad)}, Columnas: {len(matriz_paridad[0])}")
        print(f"   ")
        printMatrix(matriz_paridad)
        print(f"   ")
        print(f"   Primera fila: paridad vertical")
        print(f"   Última columna: paridad horizontal")
        print(f"   Esquina superior derecha: paridad cruzada")
    except Exception as e:
        print(f"   Error al generar matriz: {e}")
    
    print(f"\n" + "=" * 70)
    print("FIN DEL ANÁLISIS")
    print("=" * 70)

if __name__ == "__main__":
    main()
