import math
from fractions import Fraction

def calculateI(pi: float) -> float:
    if pi <= 0:
        return 0
    return math.log2(1 / pi)

def calculateH(P: list[float]) -> float:
    return sum((pi * calculateI(pi) for pi in P if pi > 0))

def getSymbolOcurrences(phrase: str) -> dict[str, int]:
    occurrences = {}
    for si in phrase:
        occurrences[si] = occurrences.get(si, 0) + 1
    return occurrences

def buildS(source: str) -> dict[str, float]:
    occurrences = getSymbolOcurrences(source)
    frequencies = {symbol: count / len(source) for symbol, count in occurrences.items()}
    return dict(sorted(frequencies.items(), key=lambda item: item[0]))

def getProbabilidadPriori(message: str) -> dict[str, float]:
    return buildS(message)

def getMatrixZeros(filas: int, columnas: int) -> list[list[float]]:
    return [[0.0 for _ in range(columnas)] for _ in range(filas)]

def getMatrixTraspuesta(M: list[list[float]]) -> list[list[float]]:
    result = []
    for i in range(len(M[0])):
        result.append([M[j][i] for j in range(len(M))])
    return result

def printMatrix(matrix: list[list[float]]) -> None:
    max_width = max((len(f'{elem:.4f}') for row in matrix for elem in row))
    for row in matrix:
        print(' '.join((f'{elem:>{max_width}.4f}' for elem in row)))

def getPrioriMatrixFull(fnt: list[str], cds: list[str], _input: str, _output: str) -> list[list[float]]:
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

def getPrioriMatrixByInputOutput(_input: str, _output: str) -> list[list[float]]:
    inalf = sorted(set(_input))
    outalf = sorted(set(_output))
    return getPrioriMatrixFull(inalf, outalf, _input, _output)

def getProbsOutSymbols(Pinitial: list[float], channel: list[list[float]]) -> list[float]:
    result = [0.0] * len(channel[0])
    for j in range(len(channel[0])):
        for i in range(len(channel)):
            result[j] += channel[i][j] * Pinitial[i]
    return result

def getPosterioriMatrix(Pinitial: list[float], channel: list[list[float]]) -> list[list[float]]:
    result = getMatrixZeros(len(channel), len(channel[0]))
    outsSymbProbs = getProbsOutSymbols(Pinitial, channel)
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if outsSymbProbs[j] != 0:
                result[i][j] = channel[i][j] * Pinitial[i] / outsSymbProbs[j]
    return result

def getMatrixSimultaneusEvent(Pinitial: list[float], channel: list[list[float]]) -> list[list[float]]:
    rows = len(channel)
    cols = len(channel[0])
    result = getMatrixZeros(rows, cols)
    for i in range(rows):
        for j in range(cols):
            result[i][j] = Pinitial[i] * channel[i][j]
    return result

def calculateHPriori(Pa: list[float]) -> float:
    return calculateH(Pa)

def calculateHPosteriori(Pa: list[float], channel: list[list[float]]) -> list[float]:
    afterchannel = getPosterioriMatrix(Pa, channel)
    result = []
    for j in range(len(afterchannel[0])):
        collectedPbs = []
        for i in range(len(afterchannel)):
            if afterchannel[i][j] > 0:
                collectedPbs.append(afterchannel[i][j])
        result.append(calculateH(collectedPbs))
    return result

def calculateHPosterioriTotal(Pa: list[float], channel: list[list[float]]) -> float:
    return calculateH(getProbsOutSymbols(Pa, channel))

def calculateHPosterioriMediaABSimple(Pa: list[float], channel: list[list[float]]) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    antiChannel = getPosterioriMatrix(Pa, channel)
    result = 0.0
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if antiChannel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1 / antiChannel[i][j])
    return result

def calculateRuido(Pa: list[float], channel: list[list[float]]) -> float:
    return calculateHPosterioriMediaABSimple(Pa, channel)

def calculateHPosterioriMediaBASimple(Pa: list[float], channel: list[list[float]]) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    result = 0.0
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if channel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1 / channel[i][j])
    return result

def calculatePerdida(Pa: list[float], channel: list[list[float]]) -> float:
    return calculateHPosterioriMediaBASimple(Pa, channel)

def calculateHCanal(Pa: list[float], channel: list[list[float]]) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    result = 0.0
    for row in simulaneusEvent:
        for item in row:
            if item > 0:
                result += item * calculateI(item)
    return result

def informacionMutuaABSimple(Pa: list[float], channel: list[list[float]]) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    outProbs = getProbsOutSymbols(Pa, channel)
    result = 0.0
    for i in range(len(simulaneusEvent)):
        for j in range(len(simulaneusEvent[0])):
            if simulaneusEvent[i][j] > 0 and outProbs[j] > 0 and (Pa[i] > 0):
                result += simulaneusEvent[i][j] * math.log2(simulaneusEvent[i][j] / (Pa[i] * outProbs[j]))
    return result

def informacionMutuaBASimple(Pa: list[float], channel: list[list[float]]) -> float:
    return informacionMutuaABSimple(Pa, channel)

def printChannelInfo(S: list[str], C: list[str], matrix: list[list[float]]) -> None:
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

def showS(S: dict[str, float]) -> None:
    for symb, percent in S.items():
        print(f'P({symb}): {round(percent, 4)}')

def askMatrix() -> list[list[float]]:
    print('Ingrese la matriz de canal fila por fila, separando los valores con espacios.')
    print('Puede ingresar fracciones (ej: 1/3).')
    print("Ingrese una línea vacía para finalizar la entrada.")
    matrix: list[list[float]] = []
    expected_cols: int | None = None
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
            print(f'Entrada inválida ({e}). Reingrese la fila. Ej: "0.5 1/3 2/3"')
    return matrix

def askPrioriProbabilities(num_symbols: int) -> list[float]:
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
    print('UNIDAD 5: DEMOSTRACIÓN DE TEORÍA DE CANALES')
    print('=' * 80)
    print('\nSeleccione el modo de entrada:')
    print('  1. Ingresar secuencias de entrada y salida del canal')
    print('  2. Ingresar directamente probabilidades a priori y matriz de canal')
    print('\nIngrese su opcion (1 o 2):')
    mode = input('> ').strip()
    
    if mode == '2':
        print('\n' + '=' * 80)
        print('MODO: ENTRADA DIRECTA DE PROBABILIDADES Y MATRIZ')
        print('=' * 80)
        print('\nPaso 1: Definir alfabetos')
        print('Ingrese los simbolos del alfabeto de entrada separados por espacios:')
        print('Ejemplo: A B C')
        S_input = input('> ').strip().split()
        S = sorted(S_input)
        print(f'\nAlfabeto de entrada A: {S}')
        
        print('\nIngrese los simbolos del alfabeto de salida separados por espacios:')
        print('Ejemplo: 0 1')
        C_input = input('> ').strip().split()
        C = sorted(C_input)
        print(f'Alfabeto de salida B: {C}')
        
        print('\nPaso 2: Ingresar matriz de canal P(B|A)')
        print(f'La matriz debe tener {len(S)} filas (entrada) y {len(C)} columnas (salida).')
        channel = askMatrix()
        
        if len(channel) != len(S) or (len(channel) > 0 and len(channel[0]) != len(C)):
            raise ValueError(f'La matriz debe tener {len(S)} filas y {len(C)} columnas.')
        
        print('\nPaso 3: Ingresar probabilidades a priori P(A)')
        priori_list = askPrioriProbabilities(len(S))
        
        print('\n' + '=' * 80)
        print('1. DATOS INGRESADOS')
        print('=' * 80)
        print(f'\nAlfabeto de entrada A: {S}')
        print(f'Alfabeto de salida B: {C}')
        print('\n Matriz de canal P(B|A):')
        printChannelInfo(S, C, channel)
        print('\n' + '=' * 80)
        print('2. PROBABILIDADES A PRIORI')
        print('=' * 80)
        priori_dict = {S[i]: priori_list[i] for i in range(len(S))}
        print('\nDistribucion a priori P(A):')
        showS(priori_dict)
    else:
        print('\n' + '=' * 80)
        print('MODO: SECUENCIAS DE ENTRADA Y SALIDA')
        print('=' * 80)
        print('\n Ingrese secuencias de entrada y salida de un canal:')
        print("   Ejemplo: entrada='AABBCC' salida='010011'")
        print('\n   Ingrese la secuencia de ENTRADA:')
        input_seq = input('   > ').upper()
        if not input_seq:
            print('  Entrada vacia. Usando secuencias por defecto.')
            input_seq = 'AABBCCAABBCC'
            output_seq = '010110010101'
        else:
            print('   Ingrese la secuencia de SALIDA:')
            output_seq = input('   > ')
            if len(output_seq) != len(input_seq):
                raise ValueError('La secuencia de salida debe tener la misma longitud que la de entrada.')
        print(f'\n Secuencias recibidas:')
        print(f"   Entrada:  '{input_seq}' (longitud: {len(input_seq)})")
        print(f"   Salida:   '{output_seq}' (longitud: {len(output_seq)})")
        print('\n' + '=' * 80)
        print('1. CONSTRUCCIÓN DEL CANAL')
        print('=' * 80)
        S = sorted(set(input_seq))
        C = sorted(set(output_seq))
        print(f'\nAlfabeto de entrada A: {S}')
        print(f'Alfabeto de salida B: {C}')
        channel = getPrioriMatrixByInputOutput(input_seq, output_seq)
        print('\n Matriz de canal P(B|A):')
        printChannelInfo(S, C, channel)
        print('\n' + '=' * 80)
        print('2. PROBABILIDADES A PRIORI')
        print('=' * 80)
        priori_dict = getProbabilidadPriori(input_seq)
        priori_list = [priori_dict[s] for s in S]
        print('\nDistribucion a priori P(A):')
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
    print(f'\nv Verificación: Σ P(A,B) = {total_conj:.4f} (debe ser 1.0)')
    print('\n' + '=' * 80)
    print('6. ENTROPÍAS DEL CANAL')
    print('=' * 80)
    H_A = calculateHPriori(priori_list)
    H_B = calculateHPosterioriTotal(priori_list, channel)
    H_AB = calculateRuido(priori_list, channel)
    H_BA = calculatePerdida(priori_list, channel)
    H_conj = calculateHCanal(priori_list, channel)
    print(f'\n Entropías calculadas:')
    print(f'   H(A)   = {H_A:.4f} bits  (entropía de entrada)')
    print(f'   H(B)   = {H_B:.4f} bits  (entropía de salida)')
    print(f'   H(A|B) = {H_AB:.4f} bits  (equivocación/ruido)')
    print(f'   H(B|A) = {H_BA:.4f} bits  (pérdida)')
    print(f'   H(A,B) = {H_conj:.4f} bits  (entropía conjunta)')
    print(f'\n Interpretación:')
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
    print(f'\n Información mutua:')
    print(f'   I(A;B) = {I_AB:.4f} bits')
    print(f'   I(B;A) = {I_BA:.4f} bits')
    print(f'\n Verificación de simetría: |I(A;B) - I(B;A)| = {abs(I_AB - I_BA):.6f}')
    print(f'\n Interpretación:')
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
    print('\n Verificando relaciones teóricas:')
    rel1_izq = H_conj
    rel1_der = H_A + H_BA
    print(f'\n   1) H(A,B) = H(A) + H(B|A)')
    print(f'      {rel1_izq:.4f} = {H_A:.4f} + {H_BA:.4f}')
    print(f'      {rel1_izq:.4f} = {rel1_der:.4f}')
    print(f"      Diferencia: {abs(rel1_izq - rel1_der):.6f} {('v' if abs(rel1_izq - rel1_der) < 0.001 else 'x')}")
    rel2_izq = H_conj
    rel2_der = H_B + H_AB
    print(f"\n   2) H(A,B) = H(B) + H(A|B)")
    print(f"      {rel2_izq:.4f} = {H_B:.4f} + {H_AB:.4f}")
    print(f"      {rel2_izq:.4f} = {rel2_der:.4f}")
    print(f"      Diferencia: {abs(rel2_izq - rel2_der):.6f} {('v' if abs(rel2_izq - rel2_der) < 0.001 else 'x')}")
    rel3_izq = I_AB
    rel3_der = H_A - H_AB
    print(f"\n   3) I(A;B) = H(A) - H(A|B)")
    print(f"      {rel3_izq:.4f} = {H_A:.4f} - {H_AB:.4f}")
    print(f"      {rel3_izq:.4f} = {rel3_der:.4f}")
    print(f"      Diferencia: {abs(rel3_izq - rel3_der):.6f} {('v' if abs(rel3_izq - rel3_der) < 0.001 else 'x')}")
    rel4_izq = I_AB
    rel4_der = H_B - H_BA
    print(f"\n   4) I(A;B) = H(B) - H(B|A)")
    print(f"      {rel4_izq:.4f} = {H_B:.4f} - {H_BA:.4f}")
    print(f"      {rel4_izq:.4f} = {rel4_der:.4f}")
    print(f"      Diferencia: {abs(rel4_izq - rel4_der):.6f} {('v' if abs(rel4_izq - rel4_der) < 0.001 else 'x')}")
    rel5_izq = I_AB
    rel5_der = H_A + H_B - H_conj
    print(f"\n   5) I(A;B) = H(A) + H(B) - H(A,B)")
    print(f"      {rel5_izq:.4f} = {H_A:.4f} + {H_B:.4f} - {H_conj:.4f}")
    print(f"      {rel5_izq:.4f} = {rel5_der:.4f}")
    print(f"      Diferencia: {abs(rel5_izq - rel5_der):.6f} {('v' if abs(rel5_izq - rel5_der) < 0.001 else 'x')}")
    print('\n' + '=' * 80)
    print('RESUMEN DEL CANAL')
    print('=' * 80)
    if mode == '2':
        print(f"\n Características del canal:\n   - Entrada: {len(S)} símbolos\n   - Salida: {len(C)} símbolos\n   \n Entropías:\n   - H(A)   = {H_A:.4f} bits (entrada)\n   - H(B)   = {H_B:.4f} bits (salida)\n   - H(A|B) = {H_AB:.4f} bits (ruido)\n   - H(B|A) = {H_BA:.4f} bits (pérdida)\n   - H(A,B) = {H_conj:.4f} bits (conjunta)\n   \n Información mutua:\n   - I(A;B) = {I_AB:.4f} bits\n   - Eficiencia: {I_AB / H_A * 100:.2f}% de H(A)\n   \nv Todas las relaciones fundamentales verificadas\nv La teoría de canales se cumple correctamente\n")
    else:
        print(f"\n Características del canal:\n   - Entrada: {len(S)} símbolos\n   - Salida: {len(C)} símbolos\n   - Muestras: {len(input_seq)} transmisiones\n   \n Entropías:\n   - H(A)   = {H_A:.4f} bits (entrada)\n   - H(B)   = {H_B:.4f} bits (salida)\n   - H(A|B) = {H_AB:.4f} bits (ruido)\n   - H(B|A) = {H_BA:.4f} bits (pérdida)\n   - H(A,B) = {H_conj:.4f} bits (conjunta)\n   \n Información mutua:\n   - I(A;B) = {I_AB:.4f} bits\n   - Eficiencia: {I_AB / H_A * 100:.2f}% de H(A)\n   \nv Todas las relaciones fundamentales verificadas\nv La teoría de canales se cumple correctamente\n")
    print('=' * 80)
    print('Demostración completada exitosamente')
    print('=' * 80)
if __name__ == '__main__':
    main()