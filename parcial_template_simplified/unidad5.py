import math

MATRIZ_CANAL = [
    [0.6, 0.3, 0.1],
    [0.1, 0.8, 0.1],
    [0.2, 0.2, 0.6]
]

PROB_PRIORI = [0.5, 0.3, 0.2]

SIMBOLOS_ENTRADA = ['a1', 'a2', 'a3']
SIMBOLOS_SALIDA = ['b1', 'b2', 'b3']

def calculateI(pi):
    if pi <= 0:
        return 0
    return math.log2(1 / pi)

def calculateH(P):
    return sum((pi * calculateI(pi) for pi in P if pi > 0))

def getMatrixZeros(filas, columnas):
    return [[0.0 for _ in range(columnas)] for _ in range(filas)]

def getProbsOutSymbols(Pinitial, channel):
    result = [0.0] * len(channel[0])
    for j in range(len(channel[0])):
        for i in range(len(channel)):
            result[j] += channel[i][j] * Pinitial[i]
    return result

def getPosterioriMatrix(Pinitial, channel):
    result = getMatrixZeros(len(channel), len(channel[0]))
    outsSymbProbs = getProbsOutSymbols(Pinitial, channel)
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if outsSymbProbs[j] != 0:
                result[i][j] = channel[i][j] * Pinitial[i] / outsSymbProbs[j]
    return result

def getMatrixSimultaneusEvent(Pinitial, channel):
    rows = len(channel)
    cols = len(channel[0])
    result = getMatrixZeros(rows, cols)
    for i in range(rows):
        for j in range(cols):
            result[i][j] = Pinitial[i] * channel[i][j]
    return result

def calculateHPriori(Pa):
    return calculateH(Pa)

def calculateHPosteriori(Pa, channel):
    afterchannel = getPosterioriMatrix(Pa, channel)
    result = []
    for j in range(len(afterchannel[0])):
        collectedPbs = []
        for i in range(len(afterchannel)):
            if afterchannel[i][j] > 0:
                collectedPbs.append(afterchannel[i][j])
        result.append(calculateH(collectedPbs))
    return result

def calculateHPosterioriTotal(Pa, channel):
    return calculateH(getProbsOutSymbols(Pa, channel))

def calculateRuido(Pa, channel):
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    antiChannel = getPosterioriMatrix(Pa, channel)
    result = 0.0
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if antiChannel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1 / antiChannel[i][j])
    return result

def calculatePerdida(Pa, channel):
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    result = 0.0
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if channel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1 / channel[i][j])
    return result

def calculateHCanal(Pa, channel):
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    result = 0.0
    for row in simulaneusEvent:
        for item in row:
            if item > 0:
                result += item * calculateI(item)
    return result

def informacionMutuaABSimple(Pa, channel):
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    outProbs = getProbsOutSymbols(Pa, channel)
    result = 0.0
    for i in range(len(simulaneusEvent)):
        for j in range(len(simulaneusEvent[0])):
            if simulaneusEvent[i][j] > 0 and outProbs[j] > 0 and Pa[i] > 0:
                result += simulaneusEvent[i][j] * math.log2(simulaneusEvent[i][j] / (Pa[i] * outProbs[j]))
    return result

def main():
    print('=' * 70)
    print('UNIDAD 5: ANÁLISIS DE CANAL')
    print('=' * 70)
    
    print(f"\n1. MATRIZ DE CANAL P(B|A)")
    print(f"   (Filas: símbolos de entrada, Columnas: símbolos de salida)")
    print()
    print(f"        ", end="")
    for s in SIMBOLOS_SALIDA:
        print(f"{s:>10}", end="")
    print()
    for i, fila in enumerate(MATRIZ_CANAL):
        print(f"   {SIMBOLOS_ENTRADA[i]:<4} ", end="")
        for val in fila:
            print(f"{val:>10.4f}", end="")
        print()
    
    print(f"\n2. PROBABILIDADES A PRIORI P(A)")
    for i, (simbolo, prob) in enumerate(zip(SIMBOLOS_ENTRADA, PROB_PRIORI)):
        print(f"   P({simbolo}) = {prob:.4f}")
    
    print(f"\n3. PROBABILIDADES DE SALIDA P(B)")
    prob_salida = getProbsOutSymbols(PROB_PRIORI, MATRIZ_CANAL)
    for simbolo, prob in zip(SIMBOLOS_SALIDA, prob_salida):
        print(f"   P({simbolo}) = {prob:.4f}")
    print(f"\n   Fórmula: P(bj) = Σi P(bj|ai) * P(ai)")
    
    print(f"\n4. MATRIZ A POSTERIORI P(A|B)")
    print(f"   (Probabilidades de entrada dado que se observó una salida)")
    print()
    matriz_posteriori = getPosterioriMatrix(PROB_PRIORI, MATRIZ_CANAL)
    print(f"        ", end="")
    for s in SIMBOLOS_SALIDA:
        print(f"{s:>10}", end="")
    print()
    for i, fila in enumerate(matriz_posteriori):
        print(f"   {SIMBOLOS_ENTRADA[i]:<4} ", end="")
        for val in fila:
            print(f"{val:>10.4f}", end="")
        print()
    print(f"\n   Fórmula (Teorema de Bayes): P(ai|bj) = P(bj|ai) * P(ai) / P(bj)")
    
    print(f"\n5. MATRIZ CONJUNTA P(A,B)")
    print(f"   (Probabilidades de ocurrencia simultánea)")
    print()
    matriz_conjunta = getMatrixSimultaneusEvent(PROB_PRIORI, MATRIZ_CANAL)
    print(f"        ", end="")
    for s in SIMBOLOS_SALIDA:
        print(f"{s:>10}", end="")
    print()
    for i, fila in enumerate(matriz_conjunta):
        print(f"   {SIMBOLOS_ENTRADA[i]:<4} ", end="")
        for val in fila:
            print(f"{val:>10.4f}", end="")
        print()
    print(f"\n   Fórmula: P(ai, bj) = P(bj|ai) * P(ai)")
    suma_conjunta = sum(sum(fila) for fila in matriz_conjunta)
    print(f"   Verificación: Σ P(A,B) = {suma_conjunta:.4f} (debe ser 1.0)")
    
    print(f"\n6. ENTROPÍAS")
    
    H_A = calculateHPriori(PROB_PRIORI)
    print(f"   H(A) = {H_A:.4f} bits  (entropía de entrada)")
    
    H_B = calculateHPosterioriTotal(PROB_PRIORI, MATRIZ_CANAL)
    print(f"   H(B) = {H_B:.4f} bits  (entropía de salida)")
    
    H_A_given_B = calculateRuido(PROB_PRIORI, MATRIZ_CANAL)
    print(f"   H(A|B) = {H_A_given_B:.4f} bits  (equivocación/ruido)")
    
    H_B_given_A = calculatePerdida(PROB_PRIORI, MATRIZ_CANAL)
    print(f"   H(B|A) = {H_B_given_A:.4f} bits  (pérdida)")
    
    H_AB = calculateHCanal(PROB_PRIORI, MATRIZ_CANAL)
    print(f"   H(A,B) = {H_AB:.4f} bits  (entropía conjunta)")
    
    H_A_given_bj = calculateHPosteriori(PROB_PRIORI, MATRIZ_CANAL)
    print(f"\n   Entropías condicionales H(A|B=bj):")
    for simbolo, h_val in zip(SIMBOLOS_SALIDA, H_A_given_bj):
        print(f"     H(A|{simbolo}) = {h_val:.4f} bits")
    
    print(f"\n7. INFORMACIÓN MUTUA")
    I_AB = informacionMutuaABSimple(PROB_PRIORI, MATRIZ_CANAL)
    print(f"   I(A;B) = {I_AB:.4f} bits")
    print(f"\n   Fórmula: I(A;B) = H(A) - H(A|B) = H(B) - H(B|A)")
    print(f"           I(A;B) = {H_A:.4f} - {H_A_given_B:.4f} = {I_AB:.4f}")
    print(f"           I(A;B) = {H_B:.4f} - {H_B_given_A:.4f} = {I_AB:.4f}")
    
    print(f"\n8. RELACIONES MATEMÁTICAS")
    
    rel1_izq = H_AB
    rel1_der = H_A + H_B_given_A
    print(f"   H(A,B) = H(A) + H(B|A)")
    print(f"   {rel1_izq:.4f} = {H_A:.4f} + {H_B_given_A:.4f} = {rel1_der:.4f}")
    print(f"   Diferencia: {abs(rel1_izq - rel1_der):.6f}")
    
    rel2_izq = H_AB
    rel2_der = H_B + H_A_given_B
    print(f"\n   H(A,B) = H(B) + H(A|B)")
    print(f"   {rel2_izq:.4f} = {H_B:.4f} + {H_A_given_B:.4f} = {rel2_der:.4f}")
    print(f"   Diferencia: {abs(rel2_izq - rel2_der):.6f}")
    
    rel3_izq = I_AB
    rel3_der = H_A - H_A_given_B
    print(f"\n   I(A;B) = H(A) - H(A|B)")
    print(f"   {rel3_izq:.4f} = {H_A:.4f} - {H_A_given_B:.4f} = {rel3_der:.4f}")
    print(f"   Diferencia: {abs(rel3_izq - rel3_der):.6f}")
    
    rel4_izq = I_AB
    rel4_der = H_B - H_B_given_A
    print(f"\n   I(A;B) = H(B) - H(B|A)")
    print(f"   {rel4_izq:.4f} = {H_B:.4f} - {H_B_given_A:.4f} = {rel4_der:.4f}")
    print(f"   Diferencia: {abs(rel4_izq - rel4_der):.6f}")
    
    print(f"\n" + "=" * 70)
    print("FIN DEL ANÁLISIS")
    print("=" * 70)

if __name__ == "__main__":
    main()
