import math

CANAL_1 = [
    [0.9, 0.1, 0.0],
    [0.0, 0.9, 0.1],
    [0.1, 0.0, 0.9]
]

PROB_PRIORI_1 = [0.4, 0.35, 0.25]

CANAL_2 = [
    [0.8, 0.15, 0.05],
    [0.1, 0.8, 0.1],
    [0.05, 0.15, 0.8]
]

SIMBOLOS_A = ['a1', 'a2', 'a3']
SIMBOLOS_B = ['b1', 'b2', 'b3']
SIMBOLOS_C = ['c1', 'c2', 'c3']

def calculateI(pi):
    if pi <= 0:
        return 0
    return math.log2(1 / pi)

def calculateH(P):
    return sum((pi * calculateI(pi) for pi in P if pi > 0))

def getMatrixZeros(filas, columnas):
    return [[0.0 for _ in range(columnas)] for _ in range(filas)]

def getMatrixProduct(A, B):
    if len(A[0]) != len(B):
        raise Exception('Las matrices no son compatibles para multiplicación')
    result = getMatrixZeros(len(A), len(B[0]))
    for i in range(len(A)):
        for k in range(len(B[0])):
            amount = 0.0
            for j in range(len(B)):
                amount += A[i][j] * B[j][k]
            result[i][k] = amount
    return result

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

def informacionMutuaABSimple(Pa, channel):
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    outProbs = getProbsOutSymbols(Pa, channel)
    result = 0.0
    for i in range(len(simulaneusEvent)):
        for j in range(len(simulaneusEvent[0])):
            if simulaneusEvent[i][j] > 0 and outProbs[j] > 0 and Pa[i] > 0:
                result += simulaneusEvent[i][j] * math.log2(simulaneusEvent[i][j] / (Pa[i] * outProbs[j]))
    return result

def isCanalNoRuido(channel):
    for j in range(len(channel[0])):
        amount = 0
        for i in range(len(channel)):
            amount += int(channel[i][j] != 0)
            if amount > 1:
                return False
    return True

def isCanalDeterminante(channel):
    for i in range(len(channel)):
        amount = 0
        for j in range(len(channel[0])):
            amount += int(channel[i][j] != 0)
            if amount > 1:
                return False
        if amount == 0:
            return False
    return True

def isCanalUniforme(channel):
    for i in range(1, len(channel)):
        probs = list(channel[0])
        for j in range(len(channel[0])):
            pij = channel[i][j]
            if pij in probs:
                probs.remove(pij)
        if probs:
            return False
    return True

def calculateCapacidadNoRuido(channel):
    return math.log2(len(channel))

def calculateCapacidadDeterminante(channel):
    return math.log2(len(channel[0]))

def calculateCapacidadUniforme(channel):
    log2NroSalida = math.log2(len(channel[0]))
    amount = 0.0
    for pij in channel[0]:
        if pij != 0:
            amount += pij * math.log2(1 / pij)
    return log2NroSalida - amount

def calcularCapacidad(channel):
    if isCanalNoRuido(channel):
        return calculateCapacidadNoRuido(channel)
    if isCanalDeterminante(channel):
        return calculateCapacidadDeterminante(channel)
    if isCanalUniforme(channel):
        return calculateCapacidadUniforme(channel)
    raise NotImplementedError('Canal general: use optimización numérica')

def generarComposedChannel(channelA, channelB):
    return getMatrixProduct(channelA, channelB)

def analizar_canal(nombre, matriz, prob_priori, simbolos_entrada, simbolos_salida):
    print(f"\n   {nombre}")
    print(f"   {'-' * len(nombre)}")
    
    H_entrada = calculateHPriori(prob_priori)
    prob_salida = getProbsOutSymbols(prob_priori, matriz)
    H_salida = calculateHPriori(prob_salida)
    ruido = calculateRuido(prob_priori, matriz)
    perdida = calculatePerdida(prob_priori, matriz)
    I_mutua = informacionMutuaABSimple(prob_priori, matriz)
    
    print(f"   Entropía entrada H(X) = {H_entrada:.4f} bits")
    print(f"   Entropía salida H(Y) = {H_salida:.4f} bits")
    print(f"   Ruido H(X|Y) = {ruido:.4f} bits")
    print(f"   Pérdida H(Y|X) = {perdida:.4f} bits")
    print(f"   Información mutua I(X;Y) = {I_mutua:.4f} bits")
    
    try:
        capacidad = calcularCapacidad(matriz)
        print(f"   Capacidad C = {capacidad:.4f} bits")
    except NotImplementedError:
        print(f"   Capacidad: No calculable (canal general)")
    
    return {
        'H_entrada': H_entrada,
        'H_salida': H_salida,
        'ruido': ruido,
        'perdida': perdida,
        'I_mutua': I_mutua
    }

def main():
    print('=' * 70)
    print('UNIDAD 6: COMPOSICIÓN DE CANALES')
    print('=' * 70)
    
    print(f"\n1. PRIMER CANAL A→B")
    print(f"\n   Matriz P(B|A):")
    print(f"        ", end="")
    for s in SIMBOLOS_B:
        print(f"{s:>10}", end="")
    print()
    for i, fila in enumerate(CANAL_1):
        print(f"   {SIMBOLOS_A[i]:<4} ", end="")
        for val in fila:
            print(f"{val:>10.4f}", end="")
        print()
    
    print(f"\n   Probabilidades a priori P(A):")
    for simbolo, prob in zip(SIMBOLOS_A, PROB_PRIORI_1):
        print(f"     P({simbolo}) = {prob:.4f}")
    
    print(f"\n2. SEGUNDO CANAL B→C")
    print(f"\n   Matriz P(C|B):")
    print(f"        ", end="")
    for s in SIMBOLOS_C:
        print(f"{s:>10}", end="")
    print()
    for i, fila in enumerate(CANAL_2):
        print(f"   {SIMBOLOS_B[i]:<4} ", end="")
        for val in fila:
            print(f"{val:>10.4f}", end="")
        print()
    
    prob_priori_2 = getProbsOutSymbols(PROB_PRIORI_1, CANAL_1)
    print(f"\n   Probabilidades a priori P(B) (salida del canal 1):")
    for simbolo, prob in zip(SIMBOLOS_B, prob_priori_2):
        print(f"     P({simbolo}) = {prob:.4f}")
    
    print(f"\n3. MÉTRICAS DE LOS CANALES INDIVIDUALES")
    metricas_1 = analizar_canal(
        "Canal 1 (A→B)", 
        CANAL_1, 
        PROB_PRIORI_1, 
        SIMBOLOS_A, 
        SIMBOLOS_B
    )
    
    metricas_2 = analizar_canal(
        "Canal 2 (B→C)", 
        CANAL_2, 
        prob_priori_2, 
        SIMBOLOS_B, 
        SIMBOLOS_C
    )
    
    print(f"\n4. CANAL COMPUESTO A→C")
    print(f"\n   El canal compuesto se obtiene por multiplicación matricial:")
    print(f"   P(C|A) = P(B|A) × P(C|B)")
    print()
    
    canal_compuesto = generarComposedChannel(CANAL_1, CANAL_2)
    
    print(f"   Matriz P(C|A):")
    print(f"        ", end="")
    for s in SIMBOLOS_C:
        print(f"{s:>10}", end="")
    print()
    for i, fila in enumerate(canal_compuesto):
        print(f"   {SIMBOLOS_A[i]:<4} ", end="")
        for val in fila:
            print(f"{val:>10.4f}", end="")
        print()
    
    print(f"\n5. MÉTRICAS DEL CANAL COMPUESTO")
    metricas_comp = analizar_canal(
        "Canal Compuesto (A→C)", 
        canal_compuesto, 
        PROB_PRIORI_1, 
        SIMBOLOS_A, 
        SIMBOLOS_C
    )
    
    print(f"\n6. RELACIONES MATEMÁTICAS")
    print(f"\n   Propiedad fundamental de canales en serie:")
    print(f"   I(A;C) ≤ min(I(A;B), I(B;C))")
    print()
    print(f"   I(A;B) = {metricas_1['I_mutua']:.4f} bits")
    print(f"   I(B;C) = {metricas_2['I_mutua']:.4f} bits")
    print(f"   I(A;C) = {metricas_comp['I_mutua']:.4f} bits")
    print()
    min_mutua = min(metricas_1['I_mutua'], metricas_2['I_mutua'])
    cumple = metricas_comp['I_mutua'] <= min_mutua + 0.0001
    print(f"   {metricas_comp['I_mutua']:.4f} ≤ {min_mutua:.4f}: {'✓ CUMPLE' if cumple else '✗ NO CUMPLE'}")
    
    print(f"\n   Comparación de ruido:")
    print(f"   Canal 1: H(A|B) = {metricas_1['ruido']:.4f} bits")
    print(f"   Canal 2: H(B|C) = {metricas_2['ruido']:.4f} bits")
    print(f"   Compuesto: H(A|C) = {metricas_comp['ruido']:.4f} bits")
    
    print(f"\n   Comparación de pérdida:")
    print(f"   Canal 1: H(B|A) = {metricas_1['perdida']:.4f} bits")
    print(f"   Canal 2: H(C|B) = {metricas_2['perdida']:.4f} bits")
    print(f"   Compuesto: H(C|A) = {metricas_comp['perdida']:.4f} bits")
    
    print(f"\n7. RESUMEN")
    print(f"\n   {'Canal':<20} {'I(X;Y)':<12} {'Ruido':<12} {'Pérdida':<12}")
    print(f"   {'-'*56}")
    print(f"   {'A→B':<20} {metricas_1['I_mutua']:<12.4f} {metricas_1['ruido']:<12.4f} {metricas_1['perdida']:<12.4f}")
    print(f"   {'B→C':<20} {metricas_2['I_mutua']:<12.4f} {metricas_2['ruido']:<12.4f} {metricas_2['perdida']:<12.4f}")
    print(f"   {'A→C (Compuesto)':<20} {metricas_comp['I_mutua']:<12.4f} {metricas_comp['ruido']:<12.4f} {metricas_comp['perdida']:<12.4f}")
    
    print(f"\n" + "=" * 70)
    print("FIN DEL ANÁLISIS")
    print("=" * 70)

if __name__ == "__main__":
    main()
