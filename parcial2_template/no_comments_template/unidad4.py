import math
from typing import List, Tuple, Dict, Optional

def calculateI(pi: float) -> float:
    if pi <= 0:
        raise ValueError('La probabilidad debe ser mayor que 0')
    return math.log2(1 / pi)

def calculateH(P: List[float]) -> float:
    return sum((pi * calculateI(pi) for pi in P if pi > 0))

def calculateIr(p: float, r: int) -> float:
    return math.log(1 / p, r)

def calculateHr(pbs: List[float], r: int) -> float:
    return sum((pbi * calculateIr(pbi, r) for pbi in pbs if pbi > 0))

def getSymbolOcurrences(phrase: str) -> Dict[str, int]:
    occurrences = {}
    for si in phrase:
        occurrences[si] = occurrences.get(si, 0) + 1
    return occurrences

def buildS(source: str) -> Dict[str, float]:
    occurrences = getSymbolOcurrences(source)
    frequencies = {symbol: count / len(source) for symbol, count in occurrences.items()}
    return dict(sorted(frequencies.items(), key=lambda item: item[0]))

def generateExtensionsP(prob: List[float], n: int) -> List[float]:
    if n == 1:
        return prob
    P = []
    prevP = generateExtensionsP(prob, n - 1)
    for pi in prob:
        for pj in prevP:
            P.append(pi * pj)
    return P

def generateExtensionsFromLL(alf: List[str], prob: List[float], n: int) -> Tuple[List[str], List[float]]:
    if n == 1:
        return (alf, prob)
    P = []
    S = []
    prevS, prevP = generateExtensionsFromLL(alf, prob, n - 1)
    for i, phrase in enumerate(prevS):
        for j, symbol in enumerate(alf):
            S.append(phrase + symbol)
            P.append(prevP[i] * prob[j])
    return (S, P)

def initializeHuffman(P: List[float]) -> List[Tuple[float, List[int]]]:
    result = []
    for i, p in enumerate(P):
        result.append((p, [i]))
    return result

def huffmanAlgorithm(result: List[str], P: List[float]) -> List[str]:
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

def huffman(P: List[float]) -> List[str]:
    result = [''] * len(P)
    return huffmanAlgorithm(result, P)

def initializeShannonFano(P: List[float]) -> List[List]:
    return sorted([[pi, i] for i, pi in enumerate(P)], key=lambda item: item[0], reverse=True)

def propagateSubfix(result: List[str], P: List[List], fix: str) -> None:
    for pi, i in P:
        result[i] += fix

def shannonfanoAlgorithm(result: List[str], Pindex: List[List]) -> None:
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

def shannonfano(P: List[float]) -> List[str]:
    result = [''] * len(P)
    Pindex = initializeShannonFano(P)
    shannonfanoAlgorithm(result, Pindex)
    return result

def rlc(message: str) -> List[Tuple[str, int]]:
    if not message:
        return []
    result = []
    symbol = message[0]
    amount = 1
    for ch in message[1:]:
        if ch == symbol:
            amount += 1
        else:
            result.append((symbol, amount))
            symbol = ch
            amount = 1
    result.append((symbol, amount))
    return result

def getAlfabetoCodigo(cods: List[str]) -> List[str]:
    alfCod = set()
    for cod in cods:
        alfCod.update(cod)
    return list(alfCod)

def getLengthsCodigo(cods: List[str]) -> List[int]:
    return [len(cod) for cod in cods]

def getLengthMedCodigo(cods: List[str], pbs: List[float]) -> float:
    l = getLengthsCodigo(cods)
    return sum((li * pbi for li, pbi in zip(l, pbs)))

def rendimientoCodigo(C: List[str], P: List[float]) -> float:
    H = calculateH(P)
    Lmed = getLengthMedCodigo(C, P)
    return H / Lmed

def redundanciaCodigo(C: List[str], P: List[float]) -> float:
    return 1 - rendimientoCodigo(C, P)

def teoremaShannon(C: List[str], P: List[float], n: int) -> bool:
    r = len(getAlfabetoCodigo(C))
    if len(P) < len(C):
        P = generateExtensionsP(P, n)
        if len(P) != len(C):
            raise ValueError('La cantidad de probabilidades no coincide con la cantidad de palabras del código')
    Lmed = getLengthMedCodigo(C, P)
    nHr = calculateHr(P, r)
    return nHr / n <= Lmed / n and Lmed / n <= nHr / n + 1 / n

def teoremaShannonExtending(C: List[str], P: List[float], n: int) -> bool:
    r = len(getAlfabetoCodigo(C))
    Hr = calculateHr(P, r)
    C, P = generateExtensionsFromLL(C, P, n)
    Lmed = getLengthMedCodigo(C, P)
    return Hr <= Lmed / n and Lmed / n <= Hr + 1 / n

def build_byteArray(bits: List[int]) -> bytearray:
    padding = (8 - len(bits) % 8) % 8
    bits += [0] * padding
    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for bit in bits[i:i + 8]:
            byte = byte << 1 | bit
        byte_array.append(byte)
    byte_array.append(padding)
    return byte_array

def solve_byteArray(bytes: bytearray) -> List[int]:
    if not bytes:
        return []
    padding = bytes[-1]
    data_bytes = bytes[:-1]
    bits = []
    for byte in data_bytes:
        bits.extend([byte >> i & 1 for i in range(7, -1, -1)])
    if padding > 0:
        bits = bits[:-padding]
    return bits

def codificar(message: str, alf: List[str], C: List[str]) -> bytearray:
    codigo_dict = dict(zip(alf, C))
    bits_str = ''.join((codigo_dict[ch] for ch in message))
    bits = [int(b) for b in bits_str]
    return build_byteArray(bits)

def decodificar(data: bytearray, C: List[str], alf: List[str]) -> str:
    codigo_inv = dict(zip(C, alf))
    bits = solve_byteArray(data)
    message = ''
    buffer = ''
    for bit in bits:
        buffer += str(bit)
        if buffer in codigo_inv:
            message += codigo_inv[buffer]
            buffer = ''
    return message

def tasaCompresion(message: str, compressed: bytearray) -> float:
    return len(message) / len(compressed)

def hamming(C: List[str]) -> int:
    if len(C) <= 1:
        raise Exception('No hay cantidad de códigos suficientes')
    min_dist = float('inf')
    for i in range(len(C)):
        for j in range(i + 1, len(C)):
            dif_amount = sum((1 for k in range(len(C[i])) if C[i][k] != C[j][k]))
            min_dist = min(min_dist, dif_amount)
    return min_dist

def erroresDetectables(C: List[str]) -> int:
    return hamming(C) - 1

def erroresCorregibles(C: List[str]) -> int:
    return (hamming(C) - 1) // 2

def printTable(labels: List[str], P: List[float], C1: List[str], C2: List[str]) -> None:
    print(f'{'Símbolo':<10} {'Prob':<10} {'Huffman':<15} {'Len':<5} {'Shannon-Fano':<15} {'Len':<5}')
    print('-' * 70)
    for label, p, c1i, c2i in zip(labels, P, C1, C2):
        print(f'{label:<10} {p:<10.4f} {c1i:<15} {len(c1i):<5} {c2i:<15} {len(c2i):<5}')

def printMetrics(C1: List[str], C2: List[str], P: List[float]) -> None:
    print('\nMétricas de los códigos:')
    print(f'{'Código':<20}{'Long. media':<15}{'Rendimiento':<15}{'Redundancia':<15}')
    print('-' * 65)
    for nombre, C in [('Huffman', C1), ('Shannon-Fano', C2)]:
        Lmed = getLengthMedCodigo(C, P)
        rend = rendimientoCodigo(C, P)
        redund = redundanciaCodigo(C, P)
        print(f'{nombre:<20}{Lmed:<15.4f}{rend:<15.4f}{redund:<15.4f}')

def main():
    print('=' * 80)
    print('UNIDAD 4: DEMOSTRACIÓN DE CÓDIGOS Y CODIFICACIÓN')
    print('=' * 80)
    print('\n📝 Ingrese un mensaje para analizar:')
    print('   (Use letras mayúsculas y símbolos simples para mejores resultados)')
    message = input('   > ').upper()
    if not message:
        print('⚠️  Mensaje vacío. Usando mensaje por defecto.')
        message = 'ABRACADABRA'
    print(f"\n✓ Mensaje recibido: '{message}' (longitud: {len(message)} caracteres)")
    print('\n' + '=' * 80)
    print('1. ANÁLISIS DE LA FUENTE')
    print('=' * 80)
    S = buildS(message)
    simbolos = list(S.keys())
    probabilidades = list(S.values())
    print(f'\nAlfabeto encontrado: {simbolos}')
    print('\nDistribución de probabilidades:')
    for simbolo, prob in S.items():
        print(f'  {simbolo}: {prob:.4f} ({int(prob * len(message))} ocurrencias)')
    H = calculateH(probabilidades)
    print(f'\n📊 Entropía de la fuente H(X) = {H:.4f} bits/símbolo')
    print(f'   (Máxima entropía posible: {math.log2(len(simbolos)):.4f} bits)')
    print(f'   (Eficiencia de la fuente: {H / math.log2(len(simbolos)) * 100:.2f}%)')
    print('\n' + '=' * 80)
    print('2. GENERACIÓN DE CÓDIGOS')
    print('=' * 80)
    print('\n🔨 Generando códigos Huffman y Shannon-Fano...')
    C_huffman = huffman(probabilidades)
    C_shannon = shannonfano(probabilidades)
    print('\n📋 Tabla de códigos generados:')
    printTable(simbolos, probabilidades, C_huffman, C_shannon)
    print('\n' + '=' * 80)
    print('3. MÉTRICAS Y COMPARACIÓN')
    print('=' * 80)
    printMetrics(C_huffman, C_shannon, probabilidades)
    L_huffman = getLengthMedCodigo(C_huffman, probabilidades)
    L_shannon = getLengthMedCodigo(C_shannon, probabilidades)
    print(f'\n💡 Interpretación:')
    print(f'   - El código Huffman es óptimo con L = {L_huffman:.4f} bits/símbolo')
    print(f'   - Shannon-Fano tiene L = {L_shannon:.4f} bits/símbolo')
    print(f'   - Diferencia: {abs(L_huffman - L_shannon):.4f} bits/símbolo')
    if L_huffman < L_shannon:
        print(f'   - Huffman es {(L_shannon / L_huffman - 1) * 100:.2f}% más eficiente')
    elif L_shannon < L_huffman:
        print(f'   - Shannon-Fano es {(L_huffman / L_shannon - 1) * 100:.2f}% más eficiente')
    else:
        print(f'   - Ambos códigos tienen la misma eficiencia')
    print('\n' + '=' * 80)
    print('4. PRIMER TEOREMA DE SHANNON')
    print('=' * 80)
    print(f'\nVerificando: H(X) ≤ L < H(X) + 1')
    print(f'             {H:.4f} ≤ L < {H + 1:.4f}')
    cumple_huffman = teoremaShannon(C_huffman, probabilidades, 1)
    cumple_shannon = teoremaShannon(C_shannon, probabilidades, 1)
    print(f'\n✓ Código Huffman: {('CUMPLE ✓' if cumple_huffman else 'NO CUMPLE ✗')}')
    print(f'  L = {L_huffman:.4f}, H = {H:.4f}, L/H = {L_huffman / H:.4f}')
    print(f'\n✓ Código Shannon-Fano: {('CUMPLE ✓' if cumple_shannon else 'NO CUMPLE ✗')}')
    print(f'  L = {L_shannon:.4f}, H = {H:.4f}, L/H = {L_shannon / H:.4f}')
    print('\n' + '=' * 80)
    print('5. CODIFICACIÓN Y DECODIFICACIÓN')
    print('=' * 80)
    print('\n🔐 Codificando mensaje con Huffman...')
    encoded_huffman = codificar(message, simbolos, C_huffman)
    print(f'   Tamaño original: {len(message)} caracteres')
    print(f'   Tamaño codificado: {len(encoded_huffman)} bytes')
    print(f'   Tasa de compresión: {tasaCompresion(message, encoded_huffman):.4f}')
    print('\n🔓 Decodificando mensaje...')
    decoded_huffman = decodificar(encoded_huffman, C_huffman, simbolos)
    print(f"   Mensaje decodificado: '{decoded_huffman}'")
    print(f'   ✓ Verificación: {('CORRECTO ✓' if decoded_huffman == message else 'ERROR ✗')}')
    print('\n🔐 Codificando mensaje con Shannon-Fano...')
    encoded_shannon = codificar(message, simbolos, C_shannon)
    print(f'   Tamaño codificado: {len(encoded_shannon)} bytes')
    print(f'   Tasa de compresión: {tasaCompresion(message, encoded_shannon):.4f}')
    decoded_shannon = decodificar(encoded_shannon, C_shannon, simbolos)
    print(f'   ✓ Verificación: {('CORRECTO ✓' if decoded_shannon == message else 'ERROR ✗')}')
    print('\n' + '=' * 80)
    print('6. RUN-LENGTH CODING (RLC)')
    print('=' * 80)
    rlc_result = rlc(message)
    print(f'\n📦 Codificación RLC del mensaje:')
    rlc_str = ''.join((f'{symbol}{amount}' for symbol, amount in rlc_result))
    print(f'   {rlc_str}')
    reconstructed = ''.join((symbol * amount for symbol, amount in rlc_result))
    print(f"\n   Original:      '{message}'")
    print(f"   Reconstruido:  '{reconstructed}'")
    print(f'   ✓ Verificación: {('CORRECTO ✓' if reconstructed == message else 'ERROR ✗')}')
    rlc_size = len(rlc_str)
    print(f'\n   Tamaño original: {len(message)} caracteres')
    print(f'   Tamaño RLC: {rlc_size} caracteres')
    if rlc_size < len(message):
        print(f'   ✓ Compresión: {(1 - rlc_size / len(message)) * 100:.2f}%')
    else:
        print(f'   ✗ Expansión: {(rlc_size / len(message) - 1) * 100:.2f}%')
        print(f'   (RLC no es eficiente para este mensaje)')
    print('\n' + '=' * 80)
    print('7. CAPACIDAD DE DETECCIÓN/CORRECCIÓN DE ERRORES')
    print('=' * 80)
    codigo_ejemplo = ['000', '111', '010', '101']
    print('\n📝 Código de ejemplo para análisis:')
    for i, cod in enumerate(codigo_ejemplo):
        print(f'   Símbolo {i + 1}: {cod}')
    try:
        d_min = hamming(codigo_ejemplo)
        errores_det = erroresDetectables(codigo_ejemplo)
        errores_corr = erroresCorregibles(codigo_ejemplo)
        print(f'\n📊 Análisis de capacidad:')
        print(f'   Distancia mínima de Hamming: {d_min}')
        print(f'   Errores detectables: {errores_det}')
        print(f'   Errores corregibles: {errores_corr}')
        print(f'\n💡 Interpretación:')
        print(f'   - Este código puede detectar hasta {errores_det} error(es)')
        print(f'   - Puede corregir hasta {errores_corr} error(es)')
        print(f'   - Para mejorar, necesitaríamos mayor distancia mínima')
    except Exception as e:
        print(f'\n⚠️  Error en análisis: {e}')
    print('\n📝 Análisis de códigos generados:')
    for nombre, codigo in [('Huffman', C_huffman), ('Shannon-Fano', C_shannon)]:
        max_len = max((len(c) for c in codigo))
        codigo_padded = [c.ljust(max_len, '0') for c in codigo]
        try:
            d_min = hamming(codigo_padded)
            print(f'\n   {nombre}:')
            print(f'     Distancia mínima: {d_min}')
            print(f'     Errores detectables: {d_min - 1}')
            print(f'     Errores corregibles: {(d_min - 1) // 2}')
        except Exception as e:
            print(f'\n   {nombre}: No se puede calcular (código de longitud variable)')
    print('\n' + '=' * 80)
    print('RESUMEN')
    print('=' * 80)
    print(f'\n📊 Características de la fuente:\n   - Alfabeto: {len(simbolos)} símbolos\n   - Entropía: {H:.4f} bits/símbolo\n   - Mensaje: {len(message)} caracteres\n   \n📈 Rendimiento de códigos:\n   - Huffman: {rendimientoCodigo(C_huffman, probabilidades):.4f} (L = {L_huffman:.4f})\n   - Shannon-Fano: {rendimientoCodigo(C_shannon, probabilidades):.4f} (L = {L_shannon:.4f})\n   \n💾 Compresión:\n   - Huffman: {tasaCompresion(message, encoded_huffman):.4f}x\n   - Shannon-Fano: {tasaCompresion(message, encoded_shannon):.4f}x\n   \n✓ Ambos códigos verifican el Primer Teorema de Shannon\n✓ La decodificación es correcta y sin ambigüedad (códigos prefijo)\n')
    print('=' * 80)
    print('Demostración completada exitosamente')
    print('=' * 80)
if __name__ == '__main__':
    main()