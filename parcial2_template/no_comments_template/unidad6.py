import math
import os
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
    if len(channel) == 2:
        p_opt, C = calculateCapacidadBinario(channel)
        return C
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

def printChannelMetrics(label: str, channel: List[List[float]], P: List[float]) -> None:
    print(f'\n=== Canal {label} ===')
    print(f'Dimension: {len(channel)}x{len(channel[0])}')
    print(f'Matriz:')
    printMatrix(channel)
    print(f'Probabilidades a priori: {[round(p, 4) for p in P]}')
    
    es_noruido = isCanalNoRuido(channel)
    es_determinante = isCanalDeterminante(channel)
    es_uniforme = isCanalUniforme(channel)
    es_simetrico = isCanalSimetrico(channel)
    
    print(f'\nPropiedades:')
    print(f'  Sin ruido: {"Si" if es_noruido else "No"}')
    print(f'  Deterministico: {"Si" if es_determinante else "No"}')
    print(f'  Uniforme: {"Si" if es_uniforme else "No"}')
    print(f'  Simetrico: {"Si" if es_simetrico else "No"}')
    
    try:
        capacidad = calcularCapacidad(channel)
        print(f'\nCapacidad: C = {capacidad:.4f} bits')
    except NotImplementedError:
        if len(channel) == 2:
            p_opt, capacidad = calculateCapacidadBinario(channel)
            print(f'\nCapacidad: C = {capacidad:.4f} bits')
            print(f'Distribucion optima: P(a1) = {p_opt:.4f}, P(a2) = {1 - p_opt:.4f}')
        else:
            capacidad = None
            print(f'\nCapacidad: No calculable (canal general no binario)')
    
    I_calc = informacionMutuaABSimple(P, channel)
    ruido = calculateRuido(P, channel)
    perdida = calculatePerdida(P, channel)
    
    print(f'\nMetricas:')
    print(f'  I(A;B) = {I_calc:.4f} bits')
    print(f'  H(A|B) = {ruido:.4f} bits (ruido)')
    print(f'  H(B|A) = {perdida:.4f} bits (perdida)')
    
    if capacidad is not None:
        print(f'  C - I(A;B) = {capacidad - I_calc:.4f} bits')

def main():
    channels = {}
    priors = {}
    channel_labels = []
    
    while True:
        os.system('clear')
        print('=' * 80)
        print('UNIDAD 6: MENU INTERACTIVO DE CANALES')
        print('=' * 80)
        
        if channels:
            print('\nCanales actuales:')
            for label in channel_labels:
                ch = channels[label]
                print(f'  {label}: {len(ch)}x{len(ch[0])} - P(entrada) = {[round(p, 2) for p in priors[label]]}')
        else:
            print('\nNo hay canales ingresados')
        
        print('\nMenu:')
        print('  1. Agregar canal')
        print('  2. Reducir canal')
        print('  3. Ver metricas de un canal')
        print('  4. Combinar canales en serie')
        print('  0. Salir')
        
        try:
            option = input('\nSeleccione opcion: ').strip()
            
            if option == '0':
                print('Saliendo...')
                break
            
            elif option == '1':
                print('\n--- Agregar Canal ---')
                print('1. Ingresar matriz y probabilidades directamente')
                print('2. Ingresar secuencias de entrada y salida')
                mode = input('Seleccione modo (1-2): ').strip()
                
                channel = None
                P_user = None
                
                if mode == '1':
                    print('\nIngrese matriz de canal:')
                    channel = askMatrix()
                    if not channel:
                        print('Error: matriz invalida')
                        input('Presione Enter para continuar...')
                        continue
                    
                    if not channel_labels:
                        P_user = askPrioriProbabilities(len(channel))
                    else:
                        last_label = channel_labels[-1]
                        last_channel = channels[last_label]
                        last_priors = priors[last_label]
                        
                        if len(last_channel[0]) != len(channel):
                            print(f'Error: salidas del canal {last_label} ({len(last_channel[0])}) no coinciden con entradas del nuevo canal ({len(channel)})')
                            input('Presione Enter para continuar...')
                            continue
                        
                        P_user = getProbsOutSymbols(last_priors, last_channel)
                        print(f'\nUsando probabilidades de salida del canal {last_label} como entrada:')
                        print(f'P(entrada) = {[round(p, 4) for p in P_user]}')
                
                elif mode == '2':
                    print('Ingrese secuencia de entrada:')
                    input_seq = input('> ').strip()
                    print('Ingrese secuencia de salida:')
                    output_seq = input('> ').strip()
                    
                    if len(input_seq) != len(output_seq):
                        print('Error: secuencias deben tener misma longitud')
                        input('Presione Enter para continuar...')
                        continue
                    
                    if not input_seq or not output_seq:
                        print('Error: secuencias no pueden estar vacias')
                        input('Presione Enter para continuar...')
                        continue
                    
                    channel = getPrioriMatrixByInputOutput(input_seq, output_seq)
                    
                    if not channel_labels:
                        probs_dict = getProbabilidadPriori(input_seq)
                        P_user = [probs_dict[key] for key in sorted(probs_dict.keys())]
                    else:
                        last_label = channel_labels[-1]
                        last_channel = channels[last_label]
                        last_priors = priors[last_label]
                        
                        if len(last_channel[0]) != len(channel):
                            print(f'Error: salidas del canal {last_label} ({len(last_channel[0])}) no coinciden con entradas del nuevo canal ({len(channel)})')
                            input('Presione Enter para continuar...')
                            continue
                        
                        P_user = getProbsOutSymbols(last_priors, last_channel)
                        print(f'\nUsando probabilidades de salida del canal {last_label} como entrada:')
                        print(f'P(entrada) = {[round(p, 4) for p in P_user]}')
                
                else:
                    print('Modo invalido')
                    input('Presione Enter para continuar...')
                    continue
                
                if channel and P_user:
                    next_label = chr(65 + len(channel_labels))
                    channels[next_label] = channel
                    priors[next_label] = P_user
                    channel_labels.append(next_label)
                    print(f'\nCanal {next_label} agregado correctamente')
                    input('Presione Enter para continuar...')
            
            elif option == '2':
                if not channels:
                    print('\nNo hay canales para reducir')
                    input('Presione Enter para continuar...')
                    continue
                
                print('\n--- Reducir Canal ---')
                print('Canales disponibles:')
                for label in channel_labels:
                    print(f'  {label}')
                
                label = input('Seleccione canal a reducir: ').strip().upper()
                
                if label not in channels:
                    print('Canal invalido')
                    input('Presione Enter para continuar...')
                    continue
                
                print(f'\nDesea reducir el canal {label}? (s/n): ')
                confirm = input('> ').strip().lower()
                
                if confirm == 's':
                    original_channel = channels[label]
                    reduced_channel = getReducedChannel([row[:] for row in original_channel])
                    
                    print(f'\nCanal original {label}:')
                    printMatrix(original_channel)
                    print(f'\nCanal reducido:')
                    printMatrix(reduced_channel)
                    
                    print(f'\nDesea reemplazar {label} con la version reducida? (s/n): ')
                    replace = input('> ').strip().lower()
                    
                    if replace == 's':
                        channels[label] = reduced_channel
                        if len(priors[label]) != len(reduced_channel):
                            priors[label] = [1 / len(reduced_channel)] * len(reduced_channel)
                        print(f'Canal {label} reducido correctamente')
                    else:
                        print('Reduccion cancelada')
                    
                    input('Presione Enter para continuar...')
            
            elif option == '3':
                if not channels:
                    print('\nNo hay canales para mostrar')
                    input('Presione Enter para continuar...')
                    continue
                
                print('\n--- Ver Metricas ---')
                print('Canales disponibles:')
                for label in channel_labels:
                    print(f'  {label}')
                
                label = input('Seleccione canal: ').strip().upper()
                
                if label not in channels:
                    print('Canal invalido')
                    input('Presione Enter para continuar...')
                    continue
                
                printChannelMetrics(label, channels[label], priors[label])
                input('\nPresione Enter para continuar...')
            
            elif option == '4':
                if len(channels) < 2:
                    print('\nSe necesitan al menos 2 canales para combinar')
                    input('Presione Enter para continuar...')
                    continue
                
                print('\n--- Combinar Canales en Serie ---')
                print('Se combinaran los canales en orden de ingreso:')
                print(' -> '.join(channel_labels))
                
                print('\nDesea continuar? (s/n): ')
                confirm = input('> ').strip().lower()
                
                if confirm != 's':
                    continue
                
                result_channel = channels[channel_labels[0]]
                composition_str = channel_labels[0]
                
                for i in range(1, len(channel_labels)):
                    label = channel_labels[i]
                    next_channel = channels[label]
                    
                    if len(result_channel[0]) != len(next_channel):
                        print(f'\nError: canal {channel_labels[i-1]} ({len(result_channel[0])} salidas) no es compatible con canal {label} ({len(next_channel)} entradas)')
                        input('Presione Enter para continuar...')
                        break
                    
                    result_channel = generarComposedChannel(result_channel, next_channel)
                    composition_str += f' x {label}'
                else:
                    print(f'\nCanal compuesto {composition_str}:')
                    printMatrix(result_channel)
                    
                    print(f'\nDesea agregar este canal compuesto? (s/n): ')
                    add = input('> ').strip().lower()
                    
                    if add == 's':
                        next_label = chr(65 + len(channel_labels))
                        channels[next_label] = result_channel
                        first_priors = priors[channel_labels[0]]
                        priors[next_label] = first_priors
                        channel_labels.append(next_label)
                        print(f'\nCanal compuesto agregado como {next_label}')
                    
                    input('Presione Enter para continuar...')
            
            else:
                print('Opcion invalida')
                input('Presione Enter para continuar...')
        
        except Exception as e:
            print(f'\nError: {e}')
            input('Presione Enter para continuar...')

if __name__ == '__main__':
    main()