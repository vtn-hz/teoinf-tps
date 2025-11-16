import math
from fractions import Fraction
from typing import List, Tuple, Dict, Optional

def getSymbolOcurrences(phrase: str) -> Dict[str, int]:
    occurrences = {}
    for si in phrase:
        occurrences[si] = occurrences.get(si, 0) + 1
    return occurrences

def buildS(source: str) -> Dict[str, float]:
    occurrences = getSymbolOcurrences(source)
    frequencies = {symbol: count / len(source) for symbol, count in occurrences.items()}
    return dict(sorted(frequencies.items(), key=lambda item: item[0]))

def getProbabilidadPriori(message: str) -> Dict[str, float]:
    return buildS(message)

def getPrioriMatrixFull(fnt: List[str], cds: List[str], _input: str, _output: str) -> List[List[float]]:
    result = getMatrixZeros(len(fnt), len(cds))
    for i in range(min(len(_input), len(_output))):
        row = fnt.index(_input[i])
        col = cds.index(_output[i])
        result[row][col] += 1
    for row in result:
        s = sum(row)
        if s > 0:
            for j in range(len(row)):
                row[j] /= s
    return result

def getPrioriMatrixByInputOutput(_input: str, _output: str) -> List[List[float]]:
    inalf = sorted(set(_input))
    outalf = sorted(set(_output))
    return getPrioriMatrixFull(inalf, outalf, _input, _output)

def calculateI(pi: float) -> float:
    if pi <= 0:
        return 0
    return math.log2(1 / pi)

def calculateH(P: List[float]) -> float:
    return sum((pi * calculateI(pi) for pi in P if pi > 0))

def getMatrixZeros(filas: int, columnas: int) -> List[List[float]]:
    return [[0.0 for _ in range(columnas)] for _ in range(filas)]

def getMatrixProduct(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
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

def printMatrix(matrix: List[List[float]]) -> None:
    max_width = max((len(f'{elem:.4f}') for row in matrix for elem in row))
    for row in matrix:
        print(' '.join((f'{elem:>{max_width}.4f}' for elem in row)))

def getProbsOutSymbols(Pinitial: List[float], channel: List[List[float]]) -> List[float]:
    result = [0.0] * len(channel[0])
    for j in range(len(channel[0])):
        for i in range(len(channel)):
            result[j] += channel[i][j] * Pinitial[i]
    return result

def getPosterioriMatrix(Pinitial: List[float], channel: List[List[float]]) -> List[List[float]]:
    result = getMatrixZeros(len(channel), len(channel[0]))
    outsSymbProbs = getProbsOutSymbols(Pinitial, channel)
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if outsSymbProbs[j] != 0:
                result[i][j] = channel[i][j] * Pinitial[i] / outsSymbProbs[j]
    return result

def getMatrixSimultaneusEvent(Pinitial: List[float], channel: List[List[float]]) -> List[List[float]]:
    rows = len(channel)
    cols = len(channel[0])
    result = getMatrixZeros(rows, cols)
    for i in range(rows):
        for j in range(cols):
            result[i][j] = Pinitial[i] * channel[i][j]
    return result

def informacionMutuaABSimple(Pa: List[float], channel: List[List[float]]) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    outProbs = getProbsOutSymbols(Pa, channel)
    result = 0.0
    for i in range(len(simulaneusEvent)):
        for j in range(len(simulaneusEvent[0])):
            if simulaneusEvent[i][j] > 0 and outProbs[j] > 0 and (Pa[i] > 0):
                result += simulaneusEvent[i][j] * math.log2(simulaneusEvent[i][j] / (Pa[i] * outProbs[j]))
    return result

def calculateRuido(Pa: List[float], channel: List[List[float]]) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    antiChannel = getPosterioriMatrix(Pa, channel)
    result = 0.0
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if antiChannel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1 / antiChannel[i][j])
    return result

def calculatePerdida(Pa: List[float], channel: List[List[float]]) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    result = 0.0
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if channel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1 / channel[i][j])
    return result

def isCanalNoRuido(channel: List[List[float]]) -> bool:
    for j in range(len(channel[0])):
        amount = 0
        for i in range(len(channel)):
            if channel[i][j] != 0:
                amount += 1
                if amount > 1:
                    return False
    return True

def isCanalDeterminante(channel: List[List[float]]) -> bool:
    for i in range(len(channel)):
        amount = 0
        for j in range(len(channel[0])):
            if channel[i][j] != 0:
                amount += 1
                if amount > 1:
                    return False
        if amount == 0:
            return False
    return True

def isCanalUniforme(channel: List[List[float]]) -> bool:
    if len(channel) < 2:
        return True
    for i in range(1, len(channel)):
        probs = list(channel[0])
        for j in range(len(channel[0])):
            pij = channel[i][j]
            if pij in probs:
                probs.remove(pij)
        if probs:
            return False
    return True

def isCanalSimetrico(channel: List[List[float]]) -> bool:
    if len(channel) != len(channel[0]):
        return False
    for i in range(len(channel)):
        probs = list(channel[0])
        probsanti = list(channel[0])
        for j in range(len(channel[0])):
            if channel[i][j] in probs:
                probs.remove(channel[i][j])
            if channel[j][i] in probsanti:
                probsanti.remove(channel[j][i])
        if probs or probsanti:
            return False
    return True

def calculateCapacidadNoRuido(channel: List[List[float]]) -> float:
    return math.log2(len(channel))

def calculateCapacidadDeterminante(channel: List[List[float]]) -> float:
    return math.log2(len(channel[0]))

def calculateCapacidadUniforme(channel: List[List[float]]) -> float:
    log2NroSalida = math.log2(len(channel[0]))
    amount = 0.0
    for pij in channel[0]:
        if pij != 0:
            amount += pij * math.log2(1 / pij)
    return log2NroSalida - amount

def calcularCapacidad(channel: List[List[float]]) -> float:
    if isCanalNoRuido(channel):
        return calculateCapacidadNoRuido(channel)
    if isCanalDeterminante(channel):
        return calculateCapacidadDeterminante(channel)
    if isCanalUniforme(channel):
        return calculateCapacidadUniforme(channel)
    raise NotImplementedError('Canal general: use optimización numérica')

def calculateCapacidadBinario(channel: List[List[float]], step: float=0.0001) -> Tuple[float, float]:
    C = -1
    p_opt = 0
    p = 0
    while p <= 1:
        pPrev = [p, 1 - p]
        currentI = informacionMutuaABSimple(pPrev, channel)
        if currentI > C:
            C = currentI
            p_opt = p
        p += step
    return (p_opt, C)

def generarComposedChannel(channelA: List[List[float]], channelB: List[List[float]]) -> List[List[float]]:
    return getMatrixProduct(channelA, channelB)

def isReduccionSuficiente(channel: List[List[float]], col1: int, col2: int) -> bool:
    const = 0
    tolerance = 1e-05
    isCalculated = False
    i = 0
    while i < len(channel) and (not isCalculated):
        if channel[i][col1] == 0 and channel[i][col2] == 0:
            i += 1
            continue
        if channel[i][col2] == 0:
            const = 0
            isCalculated = True
        else:
            const = channel[i][col1] / channel[i][col2]
            isCalculated = True
        i += 1
    for j in range(len(channel)):
        if abs(channel[j][col1] - const * channel[j][col2]) > tolerance:
            return False
    return True

def combinateCols(channel: List[List[float]], col1: int, col2: int) -> List[List[float]]:
    for i in range(len(channel)):
        channel[i][col1] += channel[i][col2]
        del channel[i][col2]
    return channel

def getCanalDeterminante(channel: List[List[float]], col1: int, col2: int) -> List[List[float]]:
    result = getMatrixZeros(len(channel[0]), len(channel[0]) - 1)
    j = 0
    for i in range(len(channel[0])):
        if i != col2:
            result[i][j] = 1
            j += 1
    result[col2][col1] = 1
    return result

def getReducedChannel(channel: List[List[float]]) -> List[List[float]]:
    isReductable = True
    while isReductable:
        col1 = -1
        col2 = -1
        for i in range(len(channel[0])):
            for j in range(i + 1, len(channel[0])):
                if isReduccionSuficiente(channel, i, j):
                    col1 = i
                    col2 = j
                    break
            if col1 != -1:
                break
        if col1 != -1 and col2 != -1:
            determinante = getCanalDeterminante(channel, col1, col2)
            channel = generarComposedChannel(channel, determinante)
        else:
            isReductable = False
    return channel

def probabilidadError(channel: List[List[float]], P: List[float]) -> float:
    if not channel or len(channel) != len(channel[0]):
        raise ValueError('La matriz del canal debe ser cuadrada')
    n = len(channel)
    if len(P) != n:
        raise ValueError('P debe tener tamaño igual al número de filas')
    columnas_tomadas = set()
    asignacion = [-1] * n
    for i in range(n):
        cols_ordenadas = sorted(range(n), key=lambda j: channel[i][j], reverse=True)
        j_elegida = None
        for j in cols_ordenadas:
            if j not in columnas_tomadas:
                j_elegida = j
                break
        if j_elegida is None:
            j_elegida = max(range(n), key=lambda j: channel[i][j])
        asignacion[i] = j_elegida
        columnas_tomadas.add(j_elegida)
    error = 0.0
    for i, j in enumerate(asignacion):
        fila_sum = sum((channel[i][k] for k in range(n)))
        correcto = channel[i][j]
        error += P[i] * (fila_sum - correcto)
    return error

def askMatrix() -> List[List[float]]:
    print('Ingrese la matriz de canal fila por fila, separando los valores con espacios.')
    print('Puede ingresar fracciones (ej: 1/3).')
    print("Ingrese una linea vacia para finalizar la entrada.")
    matrix: List[List[float]] = []
    expected_cols: Optional[int] = None
    while True:
        line = input('> ').strip()
        if line == '':
            break
        try:
            tokens = line.split()
            row = [float(Fraction(tok)) for tok in tokens]
            if expected_cols is None:
                expected_cols = len(row)
            elif len(row) != expected_cols:
                print(f'La fila tiene {len(row)} columnas, se esperaban {expected_cols}. Reingrese la fila.')
                continue
            matrix.append(row)
        except Exception as e:
            print(f'Entrada invalida ({e}). Reingrese la fila. Ej: "0.5 1/3 2/3"')
    return matrix

def askPrioriProbabilities(num_symbols: int) -> List[float]:
    print(f'\nIngrese las probabilidades a priori de los {num_symbols} simbolos de entrada.')
    print('Puede ingresar fracciones (ej: 1/3) o decimales (ej: 0.333).')
    print('Separe los valores con espacios. Las probabilidades deben sumar 1.')
    while True:
        line = input('> ').strip()
        try:
            tokens = line.split()
            if len(tokens) != num_symbols:
                print(f'Se esperaban {num_symbols} probabilidades. Reingrese.')
                continue
            probs = [float(Fraction(tok)) for tok in tokens]
            total = sum(probs)
            if abs(total - 1.0) > 0.0001:
                print(f'Las probabilidades deben sumar 1. Suma actual: {total:.4f}. Reingrese.')
                continue
            if any(p < 0 for p in probs):
                print('Las probabilidades no pueden ser negativas. Reingrese.')
                continue
            return probs
        except Exception as e:
            print(f'Entrada invalida ({e}). Reingrese. Ej: "0.25 0.25 0.5"')

def main():
    print('=' * 80)
    print('UNIDAD 6: PROPIEDADES Y CAPACIDAD DE CANALES')
    print('=' * 80)
    
    print('\nModo de entrada:')
    print('  1. Ingresar probabilidades a priori y matriz de canal directamente')
    print('  2. Ingresar secuencias de entrada y salida del canal')
    print('\nSeleccione el modo (1-2):')
    mode = input('> ').strip()
    
    P_user = None
    channel = None
    
    if mode == '1':
        print('\n' + '=' * 80)
        print('INGRESO DE MATRIZ DE CANAL')
        print('=' * 80)
        channel = askMatrix()
        if not channel:
            print('Error: No se ingreso ninguna matriz. Terminando.')
            return
        
        print('\n' + '=' * 80)
        print('INGRESO DE PROBABILIDADES A PRIORI')
        print('=' * 80)
        P_user = askPrioriProbabilities(len(channel))
    
    elif mode == '2':
        print('\n' + '=' * 80)
        print('INGRESO DE SECUENCIAS')
        print('=' * 80)
        print('Ingrese la secuencia de entrada (simbolos sin espacios):')
        input_seq = input('> ').strip()
        print('Ingrese la secuencia de salida (simbolos sin espacios, misma longitud):')
        output_seq = input('> ').strip()
        
        if len(input_seq) != len(output_seq):
            print(f'Error: Las secuencias deben tener la misma longitud. Entrada: {len(input_seq)}, Salida: {len(output_seq)}')
            return
        
        if not input_seq or not output_seq:
            print('Error: Las secuencias no pueden estar vacias.')
            return
        
        channel = getPrioriMatrixByInputOutput(input_seq, output_seq)
        probs_dict = getProbabilidadPriori(input_seq)
        P_user = [probs_dict[key] for key in sorted(probs_dict.keys())]
    
    else:
        print('Modo invalido. Terminando.')
        return
    
    print(f"\nCanal ingresado correctamente")
    
    if P_user is not None:
        print(f'\nProbabilidades a priori ingresadas: {[round(p, 4) for p in P_user]}')
        print(f'Entropia de la fuente H(A) = {calculateH(P_user):.4f} bits')
    
    print('\n' + '=' * 80)
    print('1. MATRIZ DEL CANAL')
    print('=' * 80)
    print(f"\nMatriz P(B|A) [{len(channel)}×{len(channel[0])}]:")
    printMatrix(channel)
    print('\n' + '=' * 80)
    print('2. PROPIEDADES DEL CANAL')
    print('=' * 80)
    es_noruido = isCanalNoRuido(channel)
    es_determinante = isCanalDeterminante(channel)
    es_uniforme = isCanalUniforme(channel)
    es_simetrico = isCanalSimetrico(channel)
    print(f"\n{'Propiedad':<25} {'Estado':<10}")
    print('-' * 35)
    print(f"{'Sin ruido':<25} {(' SÍ' if es_noruido else ' NO'):<10}")
    print(f"{'Determinístico':<25} {(' SÍ' if es_determinante else ' NO'):<10}")
    print(f"{'Uniforme':<25} {(' SÍ' if es_uniforme else ' NO'):<10}")
    print(f"{'Simétrico':<25} {(' SÍ' if es_simetrico else ' NO'):<10}")
    print('\n' + '=' * 80)
    print('3. CAPACIDAD DEL CANAL')
    print('=' * 80)
    try:
        capacidad = calcularCapacidad(channel)
        print(f'\n Capacidad C = {capacidad:.4f} bits')
        if es_noruido:
            print(f"   Fórmula: C = log₂(|A|) = log₂({len(channel)}) = {capacidad:.4f}")
        elif es_determinante:
            print(f"   Fórmula: C = log₂(|B|) = log₂({len(channel[0])}) = {capacidad:.4f}")
        elif es_uniforme:
            print(f"   Fórmula: C = log₂(|B|) - H(fila)")
            print(f"   C = log₂({len(channel[0])}) - H = {capacidad:.4f}")
    except NotImplementedError:
        print('\n Canal general: calculando capacidad numéricamente...')
        if len(channel) == 2:
            p_opt, capacidad = calculateCapacidadBinario(channel)
            print(f"   Capacidad C = {capacidad:.4f} bits")
            print(f"   Distribución óptima: P(a₁) = {p_opt:.4f}, P(a₂) = {1 - p_opt:.4f}")
        else:
            print('    Optimización numérica no implementada para canales no binarios')
            capacidad = None
    print('\n' + '=' * 80)
    print('4. INFORMACION MUTUA')
    print('=' * 80)
    
    P_calc = P_user if P_user is not None else [1 / len(channel)] * len(channel)
    I_calc = informacionMutuaABSimple(P_calc, channel)
    
    if P_user is not None:
        print(f'\n Con probabilidades ingresadas:')
        print(f"   P(A) = {[round(p, 4) for p in P_calc]}")
        print(f"   I(A;B) = {I_calc:.4f} bits")
    else:
        print(f'\n Con distribución uniforme:')
        print(f"   P(A) = {P_calc}")
        print(f"   I(A;B) = {I_calc:.4f} bits")
    
    if capacidad is not None:
        print(f'\n Comparación con capacidad:')
        print(f"   I(A;B) = {I_calc:.4f} bits")
        print(f"   Capacidad C = {capacidad:.4f} bits")
        print(f"   C - I(A;B) = {capacidad - I_calc:.4f} bits")
    print('\n' + '=' * 80)
    print('5. RUIDO Y PERDIDA DEL CANAL')
    print('=' * 80)
    ruido = calculateRuido(P_calc, channel)
    perdida = calculatePerdida(P_calc, channel)
    print(f'\n Con probabilidades utilizadas:')
    print(f'   H(A|B) = {ruido:.4f} bits (equivocación/ruido)')
    print(f'   H(B|A) = {perdida:.4f} bits (pérdida)')
    print(f'\n Interpretación:')
    if ruido < 0.01:
        print(f'   - Canal practicamente sin ruido')
    else:
        print(f'   - Ruido: {ruido:.4f} bits de incertidumbre sobre entrada')
    if perdida < 0.01:
        print(f'   - Canal practicamente deterministico')
    else:
        print(f'   - Perdida: {perdida:.4f} bits de incertidumbre sobre salida')
    
    print('\nDesea ingresar un segundo canal para composicion en serie? (s/n):')
    compose_choice = input('> ').strip().lower()
    
    if compose_choice == 's':
        print('\n' + '=' * 80)
        print('6. COMPOSICION DE CANALES EN SERIE')
        print('=' * 80)
        print('\nIngrese el segundo canal B→C')
        print(f'El segundo canal debe tener {len(channel[0])} filas (salidas del primer canal)')
        channel2 = askMatrix()
        
        if not channel2:
            print('Error: No se ingreso el segundo canal. Saltando composicion.')
        elif len(channel2) != len(channel[0]):
            print(f'Error: El segundo canal debe tener {len(channel[0])} filas, tiene {len(channel2)}. Saltando composicion.')
        else:
            print('\nSegundo canal B→C:')
            printMatrix(channel2)
            
            channel_comp = generarComposedChannel(channel, channel2)
            print('\nCanal compuesto A→C = A→B × B→C:')
            printMatrix(channel_comp)
            
            print('\nAnalisis del canal compuesto:')
            print('\nPropiedades del canal compuesto:')
            es_noruido_comp = isCanalNoRuido(channel_comp)
            es_determinante_comp = isCanalDeterminante(channel_comp)
            es_uniforme_comp = isCanalUniforme(channel_comp)
            es_simetrico_comp = isCanalSimetrico(channel_comp)
            print(f"  Sin ruido: {('Sí' if es_noruido_comp else 'No')}")
            print(f"  Determinístico: {('Sí' if es_determinante_comp else 'No')}")
            print(f"  Uniforme: {('Sí' if es_uniforme_comp else 'No')}")
            print(f"  Simétrico: {('Sí' if es_simetrico_comp else 'No')}")
            
            try:
                capacidad_comp = calcularCapacidad(channel_comp)
                print(f'\nCapacidad del canal compuesto: C = {capacidad_comp:.4f} bits')
            except NotImplementedError:
                if len(channel_comp) == 2:
                    p_opt_comp, capacidad_comp = calculateCapacidadBinario(channel_comp)
                    print(f'\nCapacidad del canal compuesto: C = {capacidad_comp:.4f} bits')
                else:
                    capacidad_comp = None
                    print('\nCapacidad del canal compuesto: No se puede calcular (canal general no binario)')
            
            P_comp = [1 / len(channel_comp)] * len(channel_comp)
            I_AB = informacionMutuaABSimple(P_calc, channel)
            I_BC = informacionMutuaABSimple([1 / len(channel2)] * len(channel2), channel2)
            I_AC = informacionMutuaABSimple(P_comp, channel_comp)
            
            ruido_comp = calculateRuido(P_comp, channel_comp)
            perdida_comp = calculatePerdida(P_comp, channel_comp)
            
            print(f'\nInformacion mutua:')
            print(f'  I(A;B) = {I_AB:.4f} bits')
            print(f'  I(B;C) = {I_BC:.4f} bits')
            print(f'  I(A;C) = {I_AC:.4f} bits')
            print(f'\nVerificacion: I(A;C) ≤ min(I(A;B), I(B;C))')
            print(f'  {I_AC:.4f} ≤ {min(I_AB, I_BC):.4f}: {I_AC <= min(I_AB, I_BC)}')
            
            print(f'\nRuido y perdida del canal compuesto:')
            print(f'  H(A|C) = {ruido_comp:.4f} bits (equivocación/ruido)')
            print(f'  H(C|A) = {perdida_comp:.4f} bits (pérdida)')
    
    if len(channel) == len(channel[0]):
        print('\n' + '=' * 80)
        print('PROBABILIDAD DE ERROR (REGLA ML)')
        print('=' * 80)
        Pe = probabilidadError(channel, P_calc)
        print(f'\n Con probabilidades utilizadas:')
        print(f'   Probabilidad de error ML: {Pe:.4f}')
        print(f'   Probabilidad de acierto: {1 - Pe:.4f}')
    print('\n' + '=' * 80)
    print('RESUMEN DEL CANAL')
    print('=' * 80)
    print(f"\n Canal ingresado\n   - Dimensión: {len(channel)}×{len(channel[0])}\n   \n Propiedades:\n   - Sin ruido: {('Sí' if es_noruido else 'No')}\n   - Determinístico: {('Sí' if es_determinante else 'No')}\n   - Uniforme: {('Sí' if es_uniforme else 'No')}\n   - Simétrico: {('Sí' if es_simetrico else 'No')}\n   \n Métricas:\n   - I(A;B) = {I_calc:.4f} bits\n   - H(A|B) = {ruido:.4f} bits (ruido)\n   - H(B|A) = {perdida:.4f} bits (pérdida)\n")
    if capacidad is not None:
        print(f'   - Capacidad C = {capacidad:.4f} bits')
    print('\n' + '=' * 80)
    print('Demostracion completada exitosamente')
    print('=' * 80)
if __name__ == '__main__':
    main()