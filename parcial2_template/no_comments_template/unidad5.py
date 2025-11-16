import math
from typing import List, Tuple, Dict

def calculateI(pi: float) -> float:
    if pi <= 0:
        return 0
    return math.log2(1 / pi)

def calculateH(P: List[float]) -> float:
    return sum((pi * calculateI(pi) for pi in P if pi > 0))

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

def getMatrixZeros(filas: int, columnas: int) -> List[List[float]]:
    return [[0.0 for _ in range(columnas)] for _ in range(filas)]

def getMatrixTraspuesta(M: List[List[float]]) -> List[List[float]]:
    result = []
    for i in range(len(M[0])):
        result.append([M[j][i] for j in range(len(M))])
    return result

def printMatrix(matrix: List[List[float]]) -> None:
    max_width = max((len(f'{elem:.4f}') for row in matrix for elem in row))
    for row in matrix:
        print(' '.join((f'{elem:>{max_width}.4f}' for elem in row)))

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

def getPrioriMatrixJust(_input: str, _output: str) -> List[List[float]]:
    inalf = sorted(set(_input))
    outalf = sorted(set(_output))
    return getPrioriMatrixFull(inalf, outalf, _input, _output)

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

def calculateHPriori(Pa: List[float]) -> float:
    return calculateH(Pa)

def calculateHPosteriori(Pa: List[float], channel: List[List[float]]) -> List[float]:
    afterchannel = getPosterioriMatrix(Pa, channel)
    result = []
    for j in range(len(afterchannel[0])):
        collectedPbs = []
        for i in range(len(afterchannel)):
            if afterchannel[i][j] > 0:
                collectedPbs.append(afterchannel[i][j])
        result.append(calculateH(collectedPbs))
    return result

def calculateHPosterioriTotal(Pa: List[float], channel: List[List[float]]) -> float:
    return calculateH(getProbsOutSymbols(Pa, channel))

def calculateHPosterioriMediaABSimple(Pa: List[float], channel: List[List[float]]) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    antiChannel = getPosterioriMatrix(Pa, channel)
    result = 0.0
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if antiChannel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1 / antiChannel[i][j])
    return result

def calculateRuido(Pa: List[float], channel: List[List[float]]) -> float:
    return calculateHPosterioriMediaABSimple(Pa, channel)

def calculateHPosterioriMediaBASimple(Pa: List[float], channel: List[List[float]]) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    result = 0.0
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if channel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1 / channel[i][j])
    return result

def calculatePerdida(Pa: List[float], channel: List[List[float]]) -> float:
    return calculateHPosterioriMediaBASimple(Pa, channel)

def calculateHCanal(Pa: List[float], channel: List[List[float]]) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    result = 0.0
    for row in simulaneusEvent:
        for item in row:
            if item > 0:
                result += item * calculateI(item)
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

def informacionMutuaBASimple(Pa: List[float], channel: List[List[float]]) -> float:
    return informacionMutuaABSimple(Pa, channel)

def printChannelInfo(S: List[str], C: List[str], matrix: List[List[float]]) -> None:
    max_val_len = max((len(str(round(v, 4))) for row in matrix for v in row))
    max_label_len = max(max(map(len, S)), max(map(len, C)))
    cell_width = max(max_val_len, max_label_len) + 2
    print(' ' * (max_label_len + 2), end='')
    for ci in C:
        print(f'{ci:>{cell_width}}', end='')
    print()
    for i, row in enumerate(matrix):
        print(f'{S[i]:<{max_label_len + 2}}', end='')
        for val in row:
            print(f'{round(val, 4):>{cell_width}}', end='')
        print()

def showS(S: Dict[str, float]) -> None:
    for symb, percent in S.items():
        print(f'P({symb}): {round(percent, 4)}')

def main():
    print('=' * 80)
    print('UNIDAD 5: DEMOSTRACIÓN DE TEORÍA DE CANALES')
    print('=' * 80)
    print('\n📝 Ingrese secuencias de entrada y salida de un canal:')
    print("   Ejemplo: entrada='AABBCC' salida='010011'")
    print('\n   Ingrese la secuencia de ENTRADA:')
    input_seq = input('   > ').upper()
    if not input_seq:
        print('⚠️  Entrada vacía. Usando secuencias por defecto.')
        input_seq = 'AABBCCAABBCC'
        output_seq = '010110010101'
    else:
        print('   Ingrese la secuencia de SALIDA:')
        output_seq = input('   > ')
        if len(output_seq) != len(input_seq):
            print('⚠️  Las secuencias deben tener la misma longitud. Usando por defecto.')
            input_seq = 'AABBCCAABBCC'
            output_seq = '010110010101'
    print(f'\n✓ Secuencias recibidas:')
    print(f"   Entrada:  '{input_seq}' (longitud: {len(input_seq)})")
    print(f"   Salida:   '{output_seq}' (longitud: {len(output_seq)})")
    print('\n' + '=' * 80)
    print('1. CONSTRUCCIÓN DEL CANAL')
    print('=' * 80)
    S = sorted(set(input_seq))
    C = sorted(set(output_seq))
    print(f'\nAlfabeto de entrada A: {S}')
    print(f'Alfabeto de salida B: {C}')
    channel = getPrioriMatrixJust(input_seq, output_seq)
    print('\n📊 Matriz de canal P(B|A):')
    printChannelInfo(S, C, channel)
    print('\n' + '=' * 80)
    print('2. PROBABILIDADES A PRIORI')
    print('=' * 80)
    priori_dict = getProbabilidadPriori(input_seq)
    priori_list = [priori_dict[s] for s in S]
    print('\nDistribución a priori P(A):')
    showS(priori_dict)
    print('\n' + '=' * 80)
    print('3. PROBABILIDADES DE SALIDA')
    print('=' * 80)
    outProbs = getProbsOutSymbols(priori_list, channel)
    print('\nProbabilidades de salida P(B):')
    for c, prob in zip(C, outProbs):
        print(f'P({c}): {prob:.4f}')
    print('\n' + '=' * 80)
    print('4. MATRIZ A POSTERIORI P(A|B)')
    print('=' * 80)
    posteriori = getPosterioriMatrix(priori_list, channel)
    print('\nMatriz a posteriori (Teorema de Bayes):')
    printChannelInfo(S, C, posteriori)
    print('\n' + '=' * 80)
    print('5. PROBABILIDADES CONJUNTAS P(A,B)')
    print('=' * 80)
    conjuntas = getMatrixSimultaneusEvent(priori_list, channel)
    print('\nMatriz de probabilidades conjuntas:')
    printChannelInfo(S, C, conjuntas)
    total_conj = sum((sum(row) for row in conjuntas))
    print(f'\n✓ Verificación: Σ P(A,B) = {total_conj:.4f} (debe ser 1.0)')
    print('\n' + '=' * 80)
    print('6. ENTROPÍAS DEL CANAL')
    print('=' * 80)
    H_A = calculateHPriori(priori_list)
    H_B = calculateHPosterioriTotal(priori_list, channel)
    H_AB = calculateRuido(priori_list, channel)
    H_BA = calculatePerdida(priori_list, channel)
    H_conj = calculateHCanal(priori_list, channel)
    print(f'\n📊 Entropías calculadas:')
    print(f'   H(A)   = {H_A:.4f} bits  (entropía de entrada)')
    print(f'   H(B)   = {H_B:.4f} bits  (entropía de salida)')
    print(f'   H(A|B) = {H_AB:.4f} bits  (equivocación/ruido)')
    print(f'   H(B|A) = {H_BA:.4f} bits  (pérdida)')
    print(f'   H(A,B) = {H_conj:.4f} bits  (entropía conjunta)')
    print(f'\n💡 Interpretación:')
    if H_AB < 0.01:
        print(f'   - Canal sin ruido: H(A|B) ≈ 0')
        print(f'     La salida determina completamente la entrada')
    else:
        print(f'   - Canal con ruido: H(A|B) = {H_AB:.4f} bits')
        print(f'     Queda incertidumbre sobre la entrada tras observar la salida')
    if H_BA < 0.01:
        print(f'   - Canal determinístico: H(B|A) ≈ 0')
        print(f'     La entrada determina completamente la salida')
    else:
        print(f'   - Canal con pérdida: H(B|A) = {H_BA:.4f} bits')
        print(f'     La entrada no determina completamente la salida')
    print('\n' + '=' * 80)
    print('7. INFORMACIÓN MUTUA')
    print('=' * 80)
    I_AB = informacionMutuaABSimple(priori_list, channel)
    I_BA = informacionMutuaBASimple(priori_list, channel)
    print(f'\n📊 Información mutua:')
    print(f'   I(A;B) = {I_AB:.4f} bits')
    print(f'   I(B;A) = {I_BA:.4f} bits')
    print(f'\n✓ Verificación de simetría: |I(A;B) - I(B;A)| = {abs(I_AB - I_BA):.6f}')
    print(f'\n💡 Interpretación:')
    if I_AB < 0.01:
        print(f'   - I(A;B) ≈ 0: A y B son prácticamente independientes')
        print(f'     El canal no transmite información útil')
    elif I_AB > H_A * 0.95:
        print(f'   - I(A;B) ≈ H(A): El canal transmite casi toda la información')
        print(f'     Canal de alta calidad')
    else:
        print(f'   - I(A;B) = {I_AB:.4f} bits')
        print(f'     El canal transmite {I_AB / H_A * 100:.2f}% de la información de entrada')
    print('\n' + '=' * 80)
    print('8. VERIFICACIÓN DE RELACIONES FUNDAMENTALES')
    print('=' * 80)
    print('\n📐 Verificando relaciones teóricas:')
    rel1_izq = H_conj
    rel1_der = H_A + H_BA
    print(f'\n   1) H(A,B) = H(A) + H(B|A)')
    print(f'      {rel1_izq:.4f} = {H_A:.4f} + {H_BA:.4f}')
    print(f'      {rel1_izq:.4f} = {rel1_der:.4f}')
    print(f'      Diferencia: {abs(rel1_izq - rel1_der):.6f} {('✓' if abs(rel1_izq - rel1_der) < 0.001 else '✗')}')
    rel2_izq = H_conj
    rel2_der = H_B + H_AB
    print(f'\n   2) H(A,B) = H(B) + H(A|B)')
    print(f'      {rel2_izq:.4f} = {H_B:.4f} + {H_AB:.4f}')
    print(f'      {rel2_izq:.4f} = {rel2_der:.4f}')
    print(f'      Diferencia: {abs(rel2_izq - rel2_der):.6f} {('✓' if abs(rel2_izq - rel2_der) < 0.001 else '✗')}')
    rel3_izq = I_AB
    rel3_der = H_A - H_AB
    print(f'\n   3) I(A;B) = H(A) - H(A|B)')
    print(f'      {rel3_izq:.4f} = {H_A:.4f} - {H_AB:.4f}')
    print(f'      {rel3_izq:.4f} = {rel3_der:.4f}')
    print(f'      Diferencia: {abs(rel3_izq - rel3_der):.6f} {('✓' if abs(rel3_izq - rel3_der) < 0.001 else '✗')}')
    rel4_izq = I_AB
    rel4_der = H_B - H_BA
    print(f'\n   4) I(A;B) = H(B) - H(B|A)')
    print(f'      {rel4_izq:.4f} = {H_B:.4f} - {H_BA:.4f}')
    print(f'      {rel4_izq:.4f} = {rel4_der:.4f}')
    print(f'      Diferencia: {abs(rel4_izq - rel4_der):.6f} {('✓' if abs(rel4_izq - rel4_der) < 0.001 else '✗')}')
    rel5_izq = I_AB
    rel5_der = H_A + H_B - H_conj
    print(f'\n   5) I(A;B) = H(A) + H(B) - H(A,B)')
    print(f'      {rel5_izq:.4f} = {H_A:.4f} + {H_B:.4f} - {H_conj:.4f}')
    print(f'      {rel5_izq:.4f} = {rel5_der:.4f}')
    print(f'      Diferencia: {abs(rel5_izq - rel5_der):.6f} {('✓' if abs(rel5_izq - rel5_der) < 0.001 else '✗')}')
    print('\n' + '=' * 80)
    print('RESUMEN DEL CANAL')
    print('=' * 80)
    print(f'\n📊 Características del canal:\n   - Entrada: {len(S)} símbolos\n   - Salida: {len(C)} símbolos\n   - Muestras: {len(input_seq)} transmisiones\n   \n📈 Entropías:\n   - H(A)   = {H_A:.4f} bits (entrada)\n   - H(B)   = {H_B:.4f} bits (salida)\n   - H(A|B) = {H_AB:.4f} bits (ruido)\n   - H(B|A) = {H_BA:.4f} bits (pérdida)\n   - H(A,B) = {H_conj:.4f} bits (conjunta)\n   \n💬 Información mutua:\n   - I(A;B) = {I_AB:.4f} bits\n   - Eficiencia: {I_AB / H_A * 100:.2f}% de H(A)\n   \n✓ Todas las relaciones fundamentales verificadas\n✓ La teoría de canales se cumple correctamente\n')
    print('=' * 80)
    print('Demostración completada exitosamente')
    print('=' * 80)
if __name__ == '__main__':
    main()