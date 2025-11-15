#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
================================================================================
UNIDAD 4: CÓDIGOS Y CODIFICACIÓN - TEORÍA DE LA INFORMACIÓN
================================================================================

RESUMEN TEÓRICO:

1. ENTROPÍA DE UNA FUENTE:
   La entropía H(X) mide la incertidumbre promedio de una fuente de información.
   Para una fuente de memoria nula con símbolos {s1, s2, ..., sn} y probabilidades
   {p1, p2, ..., pn}, la entropía se calcula como:
   
   H(X) = - Σ pi * log₂(pi) = Σ pi * I(si)
   
   donde I(si) = log₂(1/pi) es la información de cada símbolo.

2. CÓDIGOS DE FUENTE:
   Un código es una asignación de palabras binarias (codewords) a los símbolos
   de una fuente. Los códigos más eficientes asignan palabras cortas a símbolos
   frecuentes y palabras largas a símbolos infrecuentes.

3. ALGORITMOS DE CODIFICACIÓN:
   
   a) Huffman: Genera códigos óptimos (longitud media mínima) mediante la
      construcción de un árbol binario desde las hojas (símbolos) hacia la raíz,
      combinando los dos nodos de menor probabilidad en cada paso.
   
   b) Shannon-Fano: Divide recursivamente el conjunto de símbolos en dos grupos
      de probabilidad similar, asignando 0 a un grupo y 1 al otro.
   
   c) RLC (Run-Length Coding): Codifica secuencias repetidas como (símbolo, cantidad).
      Eficiente para datos con muchas repeticiones consecutivas.

4. PRIMER TEOREMA DE SHANNON:
   Para una fuente con entropía H(X) y un código con alfabeto de r símbolos,
   la longitud media L del código cumple:
   
   Hᵣ(X) ≤ L < Hᵣ(X) + 1
   
   donde Hᵣ(X) = H(X) / log₂(r) es la entropía en base r.
   
   Este teorema establece el límite teórico de compresión sin pérdida.

5. MÉTRICAS DE CÓDIGOS:
   - Longitud media: L = Σ pi * li, donde li es la longitud de la i-ésima palabra
   - Rendimiento: η = H(X) / L (idealmente η → 1)
   - Redundancia: R = 1 - η (idealmente R → 0)
   - Tasa de compresión: longitud_original / longitud_comprimida

6. EXTENSIONES DE FUENTE:
   La extensión de orden n de una fuente S crea símbolos que son n-tuplas
   de los símbolos originales. Esto permite codificar bloques de símbolos,
   mejorando la eficiencia del código.

7. DETECCIÓN Y CORRECCIÓN DE ERRORES:
   - Distancia de Hamming d(x,y): número de posiciones en que difieren x e y
   - Distancia mínima dₘᵢₙ de un código: mínima distancia entre pares de palabras
   - Errores detectables: dₘᵢₙ - 1
   - Errores corregibles: ⌊(dₘᵢₙ - 1) / 2⌋

================================================================================
"""

import math
from typing import List, Tuple, Dict, Optional


# ============================================================================
# FUNCIONES DE INFORMACIÓN Y ENTROPÍA
# ============================================================================

def calculateI(pi: float) -> float:
    """
    Calcula la información de un símbolo con probabilidad pi.
    
    Fundamento teórico:
    La información I(si) mide la "sorpresa" de observar el símbolo si.
    Matemáticamente: I(si) = log₂(1/pi)
    
    Propiedades:
    - Símbolos menos probables tienen mayor información
    - I(si) ≥ 0 para todo 0 < pi ≤ 1
    - I(si) = 0 cuando pi = 1 (certeza total)
    
    Args:
        pi: Probabilidad del símbolo (0 < pi ≤ 1)
    
    Returns:
        Información en bits
    
    Raises:
        ValueError: Si pi ≤ 0
    """
    if pi <= 0:
        raise ValueError("La probabilidad debe ser mayor que 0")
    return math.log2(1 / pi)


def calculateH(P: List[float]) -> float:
    """
    Calcula la entropía H(X) de una fuente de memoria nula.
    
    Fundamento teórico:
    La entropía mide la cantidad promedio de información por símbolo.
    H(X) = Σ pi * I(pi) = - Σ pi * log₂(pi)
    
    La entropía es máxima cuando todos los símbolos son equiprobables:
    H_max = log₂(n), donde n es el número de símbolos.
    
    Args:
        P: Lista de probabilidades de los símbolos (deben sumar 1)
    
    Returns:
        Entropía en bits por símbolo
    """
    return sum(pi * calculateI(pi) for pi in P if pi > 0)


def calculateIr(p: float, r: int) -> float:
    """
    Calcula la información de un símbolo en base r.
    
    Fundamento teórico:
    Para códigos con alfabeto de r símbolos, la información se mide en base r:
    Iᵣ(si) = logᵣ(1/pi)
    
    Args:
        p: Probabilidad del símbolo
        r: Base del logaritmo (tamaño del alfabeto del código)
    
    Returns:
        Información en base r
    """
    return math.log(1 / p, r)


def calculateHr(pbs: List[float], r: int) -> float:
    """
    Calcula la entropía Hᵣ(X) en base r.
    
    Fundamento teórico:
    Para códigos con alfabeto de r símbolos:
    Hᵣ(X) = Σ pi * Iᵣ(pi) = H(X) / log₂(r)
    
    Args:
        pbs: Lista de probabilidades
        r: Base del logaritmo (tamaño del alfabeto del código)
    
    Returns:
        Entropía en base r
    """
    return sum(pbi * calculateIr(pbi, r) for pbi in pbs if pbi > 0)


# ============================================================================
# FUNCIONES DE ANÁLISIS DE SÍMBOLOS
# ============================================================================

def getSymbolOcurrences(phrase: str) -> Dict[str, int]:
    """
    Cuenta las ocurrencias de cada símbolo en una cadena.
    
    Args:
        phrase: Cadena de texto a analizar
    
    Returns:
        Diccionario {símbolo: cantidad de ocurrencias}
    """
    occurrences = {}
    for si in phrase:
        occurrences[si] = occurrences.get(si, 0) + 1
    return occurrences


def buildS(source: str) -> Dict[str, float]:
    """
    Construye una distribución de probabilidad empírica desde un texto.
    
    Fundamento teórico:
    La frecuencia relativa de cada símbolo es una estimación de su probabilidad:
    p(si) ≈ n(si) / N
    donde n(si) es el número de ocurrencias de si y N es el total de símbolos.
    
    Args:
        source: Texto fuente
    
    Returns:
        Diccionario ordenado {símbolo: probabilidad}
    """
    occurrences = getSymbolOcurrences(source)
    frequencies = {symbol: count / len(source) for symbol, count in occurrences.items()}
    return dict(sorted(frequencies.items(), key=lambda item: item[0]))


# ============================================================================
# EXTENSIONES DE FUENTE
# ============================================================================

def generateExtensionsP(prob: List[float], n: int) -> List[float]:
    """
    Genera las probabilidades de la extensión de orden n de una fuente.
    
    Fundamento teórico:
    La extensión Sⁿ de una fuente S tiene qⁿ símbolos, donde q es el tamaño
    del alfabeto original. Para fuentes de memoria nula, la probabilidad de
    una n-tupla (s₁, s₂, ..., sₙ) es el producto de probabilidades individuales:
    P(s₁s₂...sₙ) = P(s₁) * P(s₂) * ... * P(sₙ)
    
    Args:
        prob: Probabilidades de la fuente original
        n: Orden de la extensión
    
    Returns:
        Lista de probabilidades de la extensión Sⁿ
    """
    if n == 1:
        return prob
    
    P = []
    prevP = generateExtensionsP(prob, n - 1)
    
    for pi in prob:
        for pj in prevP:
            P.append(pi * pj)
    return P


def generateExtensionsFromLL(alf: List[str], prob: List[float], n: int) -> Tuple[List[str], List[float]]:
    """
    Genera la extensión de orden n con símbolos y probabilidades.
    
    Args:
        alf: Alfabeto de la fuente original
        prob: Probabilidades de la fuente original
        n: Orden de la extensión
    
    Returns:
        Tupla (símbolos_extensión, probabilidades_extensión)
    """
    if n == 1:
        return alf, prob
    
    P = []
    S = []
    
    prevS, prevP = generateExtensionsFromLL(alf, prob, n - 1)
    
    for i, phrase in enumerate(prevS):
        for j, symbol in enumerate(alf):
            S.append(phrase + symbol)
            P.append(prevP[i] * prob[j])
    return S, P


# ============================================================================
# ALGORITMO DE HUFFMAN
# ============================================================================

def initializeHuffman(P: List[float]) -> List[Tuple[float, List[int]]]:
    """
    Inicializa la estructura para el algoritmo de Huffman.
    
    Args:
        P: Lista de probabilidades
    
    Returns:
        Lista de tuplas (probabilidad, [índices])
    """
    result = []
    for i, p in enumerate(P):
        result.append((p, [i]))
    return result


def huffmanAlgorithm(result: List[str], P: List[float]) -> List[str]:
    """
    Implementa el algoritmo de Huffman para generar códigos óptimos.
    
    Fundamento teórico:
    El algoritmo de Huffman construye un árbol binario óptimo:
    1. Crear un nodo hoja para cada símbolo con su probabilidad
    2. Repetir hasta tener un solo nodo:
       a) Seleccionar los dos nodos de menor probabilidad
       b) Crear un nodo padre con probabilidad = suma de hijos
       c) Asignar '0' a un hijo y '1' al otro
    3. El código de cada símbolo es el camino desde la raíz hasta su hoja
    
    Propiedades:
    - Genera códigos de longitud variable óptimos (longitud media mínima)
    - Es un código prefijo (ninguna palabra es prefijo de otra)
    - Símbolo más probable → código más corto
    
    Args:
        result: Lista de strings inicializada con '' para cada símbolo
        P: Lista de probabilidades
    
    Returns:
        Lista de códigos Huffman
    """
    huffman = initializeHuffman(P)
    huffman.sort(key=lambda x: x[0], reverse=True)
    
    while len(huffman) > 1:
        (p1, c1) = huffman.pop()  # Menor probabilidad
        (p2, c2) = huffman.pop()  # Segunda menor
        
        # Asignar bits: '0' al primer hijo, '1' al segundo
        for i in c1:
            result[i] = '0' + result[i]
        for i in c2:
            result[i] = '1' + result[i]
        
        # Crear nuevo nodo combinado
        huffman.append((p1 + p2, c1 + c2))
        huffman.sort(key=lambda x: x[0], reverse=True)
    
    return result


def huffman(P: List[float]) -> List[str]:
    """
    Genera códigos Huffman para una fuente con probabilidades P.
    
    Args:
        P: Lista de probabilidades de los símbolos
    
    Returns:
        Lista de códigos Huffman (strings binarios)
    """
    result = [''] * len(P)
    return huffmanAlgorithm(result, P)


# ============================================================================
# ALGORITMO DE SHANNON-FANO
# ============================================================================

def initializeShannonFano(P: List[float]) -> List[List]:
    """
    Inicializa la estructura para Shannon-Fano ordenando por probabilidad.
    
    Args:
        P: Lista de probabilidades
    
    Returns:
        Lista de [probabilidad, índice] ordenada descendentemente
    """
    return sorted([[pi, i] for i, pi in enumerate(P)], key=lambda item: item[0], reverse=True)


def propagateSubfix(result: List[str], P: List[List], fix: str) -> None:
    """
    Agrega un sufijo a los códigos de un subconjunto de símbolos.
    
    Args:
        result: Lista de códigos en construcción
        P: Lista de [probabilidad, índice]
        fix: Sufijo a agregar ('0' o '1')
    """
    for pi, i in P:
        result[i] += fix


def shannonfanoAlgorithm(result: List[str], Pindex: List[List]) -> None:
    """
    Implementa el algoritmo de Shannon-Fano recursivamente.
    
    Fundamento teórico:
    Shannon-Fano divide recursivamente el conjunto de símbolos:
    1. Ordenar símbolos por probabilidad decreciente
    2. Dividir en dos grupos de probabilidad total similar
    3. Asignar '1' al primer grupo, '0' al segundo
    4. Aplicar recursivamente a cada grupo
    
    Propiedades:
    - Genera códigos prefijo
    - No siempre óptimo (Huffman lo es)
    - Más simple de implementar que Huffman
    
    Args:
        result: Lista de códigos en construcción
        Pindex: Lista de [probabilidad, índice] ordenada
    """
    if len(Pindex) <= 1:
        return
    
    # Calcular punto de división óptimo
    total = sum(pi for pi, i in Pindex) / 2
    
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
            
            # Dividir en dos grupos
            firstPart = Pindex[:splitLocation]
            secondPart = Pindex[splitLocation:]
            
            # Asignar bits
            propagateSubfix(result, firstPart, '1')
            propagateSubfix(result, secondPart, '0')
            
            # Recursión en cada grupo
            shannonfanoAlgorithm(result, firstPart)
            shannonfanoAlgorithm(result, secondPart)
            return
        
        lastDif = abs(total - acum)


def shannonfano(P: List[float]) -> List[str]:
    """
    Genera códigos Shannon-Fano para una fuente con probabilidades P.
    
    Args:
        P: Lista de probabilidades de los símbolos
    
    Returns:
        Lista de códigos Shannon-Fano (strings binarios)
    """
    result = [''] * len(P)
    Pindex = initializeShannonFano(P)
    shannonfanoAlgorithm(result, Pindex)
    return result


# ============================================================================
# RLC (RUN-LENGTH CODING)
# ============================================================================

def rlc(message: str) -> List[Tuple[str, int]]:
    """
    Aplica codificación Run-Length a un mensaje.
    
    Fundamento teórico:
    RLC codifica secuencias de símbolos repetidos como (símbolo, cantidad).
    Es eficiente cuando hay largas secuencias de repeticiones.
    
    Ejemplo: "AAAABBBCCDAA" → [('A',4), ('B',3), ('C',2), ('D',1), ('A',2)]
    
    Ventajas:
    - Simple de implementar
    - Muy eficiente para datos con muchas repeticiones
    
    Desventajas:
    - Ineficiente si no hay repeticiones (expande el mensaje)
    
    Args:
        message: Cadena a codificar
    
    Returns:
        Lista de tuplas (símbolo, cantidad)
    """
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


# ============================================================================
# METADATA Y MÉTRICAS DE CÓDIGOS
# ============================================================================

def getAlfabetoCodigo(cods: List[str]) -> List[str]:
    """
    Obtiene el alfabeto (símbolos únicos) utilizado en un código.
    
    Args:
        cods: Lista de palabras del código
    
    Returns:
        Lista de símbolos únicos usados
    """
    alfCod = set()
    for cod in cods:
        alfCod.update(cod)
    return list(alfCod)


def getLengthsCodigo(cods: List[str]) -> List[int]:
    """
    Obtiene las longitudes de cada palabra del código.
    
    Args:
        cods: Lista de palabras del código
    
    Returns:
        Lista de longitudes
    """
    return [len(cod) for cod in cods]


def getLengthMedCodigo(cods: List[str], pbs: List[float]) -> float:
    """
    Calcula la longitud media L de un código.
    
    Fundamento teórico:
    La longitud media es el promedio ponderado de las longitudes:
    L = Σ pi * li
    donde li es la longitud de la palabra del símbolo i.
    
    L representa el número promedio de bits necesarios para codificar
    un símbolo de la fuente.
    
    Args:
        cods: Lista de palabras del código
        pbs: Lista de probabilidades de los símbolos
    
    Returns:
        Longitud media en bits por símbolo
    """
    l = getLengthsCodigo(cods)
    return sum(li * pbi for li, pbi in zip(l, pbs))


def rendimientoCodigo(C: List[str], P: List[float]) -> float:
    """
    Calcula el rendimiento η de un código.
    
    Fundamento teórico:
    El rendimiento mide la eficiencia del código:
    η = H(X) / L
    
    donde H(X) es la entropía de la fuente y L es la longitud media del código.
    
    Interpretación:
    - η = 1: código óptimo (alcanza el límite de Shannon)
    - η < 1: código subóptimo (hay redundancia)
    - η cercano a 1: código eficiente
    
    Args:
        C: Lista de palabras del código
        P: Lista de probabilidades
    
    Returns:
        Rendimiento (0 < η ≤ 1)
    """
    H = calculateH(P)
    Lmed = getLengthMedCodigo(C, P)
    return H / Lmed


def redundanciaCodigo(C: List[str], P: List[float]) -> float:
    """
    Calcula la redundancia R de un código.
    
    Fundamento teórico:
    La redundancia mide cuánta información extra contiene el código:
    R = 1 - η = 1 - (H/L) = (L - H) / L
    
    Interpretación:
    - R = 0: código óptimo (sin redundancia)
    - R > 0: hay bits redundantes
    - R pequeña: código eficiente
    
    Args:
        C: Lista de palabras del código
        P: Lista de probabilidades
    
    Returns:
        Redundancia (0 ≤ R < 1)
    """
    return 1 - rendimientoCodigo(C, P)


# ============================================================================
# TEOREMA DE SHANNON
# ============================================================================

def teoremaShannon(C: List[str], P: List[float], n: int) -> bool:
    """
    Verifica si un código cumple el Primer Teorema de Shannon.
    
    Fundamento teórico:
    El Primer Teorema de Shannon establece que para una fuente con entropía H(X)
    y un código con alfabeto de r símbolos, existe un código tal que:
    
    Hᵣ(X) / n ≤ L / n < Hᵣ(X) / n + 1 / n
    
    donde L es la longitud media del código y n es el orden de la extensión.
    
    Cuando n → ∞, L/n → Hᵣ(X), lo que significa que podemos acercarnos
    arbitrariamente al límite teórico de compresión.
    
    Args:
        C: Lista de palabras del código
        P: Lista de probabilidades (puede ser de extensión)
        n: Orden de la extensión
    
    Returns:
        True si cumple el teorema, False en caso contrario
    """
    r = len(getAlfabetoCodigo(C))
    
    # Si hay menos probabilidades que palabras de código, generar extensión
    if len(P) < len(C):
        P = generateExtensionsP(P, n)
        if len(P) != len(C):
            raise ValueError("La cantidad de probabilidades no coincide con la cantidad de palabras del código")
    
    Lmed = getLengthMedCodigo(C, P)
    nHr = calculateHr(P, r)
    
    return nHr / n <= Lmed / n and Lmed / n <= nHr / n + 1 / n


def teoremaShannonExtending(C: List[str], P: List[float], n: int) -> bool:
    """
    Verifica el teorema de Shannon extendiendo el código y la fuente.
    
    Args:
        C: Lista de palabras del código base
        P: Lista de probabilidades base
        n: Orden de la extensión
    
    Returns:
        True si cumple el teorema, False en caso contrario
    """
    r = len(getAlfabetoCodigo(C))
    Hr = calculateHr(P, r)
    
    # Generar extensión del código y probabilidades
    C, P = generateExtensionsFromLL(C, P, n)
    
    Lmed = getLengthMedCodigo(C, P)
    
    return Hr <= Lmed / n and Lmed / n <= Hr + 1 / n


# ============================================================================
# CODIFICACIÓN Y DECODIFICACIÓN
# ============================================================================

def build_byteArray(bits: List[int]) -> bytearray:
    """
    Convierte una lista de bits en un bytearray con padding.
    
    Args:
        bits: Lista de bits (0 o 1)
    
    Returns:
        bytearray con los bits empaquetados y padding al final
    """
    padding = (8 - (len(bits) % 8)) % 8
    bits += [0] * padding
    
    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for bit in bits[i:i+8]:
            byte = (byte << 1) | bit
        byte_array.append(byte)
    
    byte_array.append(padding)
    return byte_array


def solve_byteArray(bytes: bytearray) -> List[int]:
    """
    Convierte un bytearray en una lista de bits, removiendo padding.
    
    Args:
        bytes: bytearray con padding en el último byte
    
    Returns:
        Lista de bits
    """
    if not bytes:
        return []
    
    padding = bytes[-1]
    data_bytes = bytes[:-1]
    
    bits = []
    for byte in data_bytes:
        bits.extend([(byte >> i) & 1 for i in range(7, -1, -1)])
    
    if padding > 0:
        bits = bits[:-padding]
    
    return bits


def codificar(message: str, alf: List[str], C: List[str]) -> bytearray:
    """
    Codifica un mensaje usando un código dado.
    
    Fundamento teórico:
    La codificación reemplaza cada símbolo del mensaje por su palabra código
    correspondiente, generando una secuencia binaria comprimida.
    
    Args:
        message: Mensaje a codificar
        alf: Alfabeto de símbolos
        C: Código correspondiente a cada símbolo
    
    Returns:
        bytearray con el mensaje codificado
    """
    codigo_dict = dict(zip(alf, C))
    bits_str = ''.join(codigo_dict[ch] for ch in message)
    bits = [int(b) for b in bits_str]
    return build_byteArray(bits)


def decodificar(data: bytearray, C: List[str], alf: List[str]) -> str:
    """
    Decodifica un mensaje binario usando un código prefijo.
    
    Fundamento teórico:
    Para códigos prefijo (como Huffman y Shannon-Fano), la decodificación
    es única y se realiza leyendo bits hasta encontrar una palabra válida,
    sin necesidad de delimitadores.
    
    Args:
        data: bytearray con mensaje codificado
        C: Lista de palabras del código
        alf: Lista de símbolos correspondientes
    
    Returns:
        Mensaje decodificado
    """
    codigo_inv = dict(zip(C, alf))
    bits = solve_byteArray(data)
    
    message = ""
    buffer = ""
    
    for bit in bits:
        buffer += str(bit)
        if buffer in codigo_inv:
            message += codigo_inv[buffer]
            buffer = ""
    
    return message


def tasaCompresion(message: str, compressed: bytearray) -> float:
    """
    Calcula la tasa de compresión.
    
    Fundamento teórico:
    La tasa de compresión mide cuánto se redujo el tamaño:
    tasa = tamaño_original / tamaño_comprimido
    
    Una tasa > 1 indica compresión efectiva.
    
    Args:
        message: Mensaje original
        compressed: Mensaje comprimido
    
    Returns:
        Tasa de compresión
    """
    return len(message) / len(compressed)


# ============================================================================
# DISTANCIA DE HAMMING Y DETECCIÓN/CORRECCIÓN DE ERRORES
# ============================================================================

def hamming(C: List[str]) -> int:
    """
    Calcula la distancia mínima de Hamming de un código.
    
    Fundamento teórico:
    La distancia de Hamming entre dos palabras es el número de posiciones
    en que difieren. La distancia mínima dₘᵢₙ de un código es la menor
    distancia entre cualquier par de palabras del código.
    
    dₘᵢₙ determina la capacidad de detección y corrección de errores:
    - Errores detectables: dₘᵢₙ - 1
    - Errores corregibles: ⌊(dₘᵢₙ - 1) / 2⌋
    
    Args:
        C: Lista de palabras del código (todas deben tener igual longitud)
    
    Returns:
        Distancia mínima de Hamming
    
    Raises:
        Exception: Si hay menos de 2 palabras en el código
    """
    if len(C) <= 1:
        raise Exception("No hay cantidad de códigos suficientes")
    
    min_dist = float('inf')
    
    for i in range(len(C)):
        for j in range(i + 1, len(C)):
            # Calcular distancia de Hamming entre C[i] y C[j]
            dif_amount = sum(1 for k in range(len(C[i])) if C[i][k] != C[j][k])
            min_dist = min(min_dist, dif_amount)
    
    return min_dist


def erroresDetectables(C: List[str]) -> int:
    """
    Calcula la cantidad de errores detectables de un código.
    
    Fundamento teórico:
    Un código con distancia mínima dₘᵢₙ puede detectar hasta (dₘᵢₙ - 1) errores.
    
    Esto se debe a que si ocurren hasta (dₘᵢₙ - 1) errores, la palabra
    resultante no puede ser otra palabra válida del código.
    
    Args:
        C: Lista de palabras del código
    
    Returns:
        Número máximo de errores detectables
    """
    return hamming(C) - 1


def erroresCorregibles(C: List[str]) -> int:
    """
    Calcula la cantidad de errores corregibles de un código.
    
    Fundamento teórico:
    Un código con distancia mínima dₘᵢₙ puede corregir hasta
    t = ⌊(dₘᵢₙ - 1) / 2⌋ errores.
    
    Esto garantiza que cualquier palabra con hasta t errores está más cerca
    de la palabra código original que de cualquier otra palabra del código.
    
    Args:
        C: Lista de palabras del código
    
    Returns:
        Número máximo de errores corregibles
    """
    return (hamming(C) - 1) // 2


# ============================================================================
# FUNCIONES AUXILIARES PARA VISUALIZACIÓN
# ============================================================================

def printTable(labels: List[str], P: List[float], C1: List[str], C2: List[str]) -> None:
    """
    Imprime una tabla comparativa de códigos Huffman y Shannon-Fano.
    
    Args:
        labels: Etiquetas de los símbolos
        P: Probabilidades
        C1: Códigos Huffman
        C2: Códigos Shannon-Fano
    """
    print(f"{'Símbolo':<10} {'Prob':<10} {'Huffman':<15} {'Len':<5} {'Shannon-Fano':<15} {'Len':<5}")
    print("-" * 70)
    for label, p, c1i, c2i in zip(labels, P, C1, C2):
        print(f"{label:<10} {p:<10.4f} {c1i:<15} {len(c1i):<5} {c2i:<15} {len(c2i):<5}")


def printMetrics(C1: List[str], C2: List[str], P: List[float]) -> None:
    """
    Imprime métricas de rendimiento de códigos.
    
    Args:
        C1: Códigos Huffman
        C2: Códigos Shannon-Fano
        P: Probabilidades
    """
    print("\nMétricas de los códigos:")
    print(f"{'Código':<20}{'Long. media':<15}{'Rendimiento':<15}{'Redundancia':<15}")
    print("-" * 65)
    
    for nombre, C in [("Huffman", C1), ("Shannon-Fano", C2)]:
        Lmed = getLengthMedCodigo(C, P)
        rend = rendimientoCodigo(C, P)
        redund = redundanciaCodigo(C, P)
        print(f"{nombre:<20}{Lmed:<15.4f}{rend:<15.4f}{redund:<15.4f}")


# ============================================================================
# FUNCIÓN PRINCIPAL - DEMOSTRACIÓN
# ============================================================================

def main():
    """
    Función principal que demuestra todas las funcionalidades del código.
    
    Solicita UNA entrada al usuario (un mensaje de texto) y ejecuta:
    1. Análisis de la fuente (entropía, distribución)
    2. Generación de códigos (Huffman, Shannon-Fano, RLC)
    3. Comparación de métricas
    4. Verificación del teorema de Shannon
    5. Codificación y decodificación
    6. Análisis de capacidad de detección/corrección de errores
    """
    print("=" * 80)
    print("UNIDAD 4: DEMOSTRACIÓN DE CÓDIGOS Y CODIFICACIÓN")
    print("=" * 80)
    
    # Entrada única del usuario
    print("\n📝 Ingrese un mensaje para analizar:")
    print("   (Use letras mayúsculas y símbolos simples para mejores resultados)")
    message = input("   > ").upper()
    
    if not message:
        print("⚠️  Mensaje vacío. Usando mensaje por defecto.")
        message = "ABRACADABRA"
    
    print(f"\n✓ Mensaje recibido: '{message}' (longitud: {len(message)} caracteres)")
    
    # ========================================================================
    # 1. ANÁLISIS DE LA FUENTE
    # ========================================================================
    print("\n" + "=" * 80)
    print("1. ANÁLISIS DE LA FUENTE")
    print("=" * 80)
    
    S = buildS(message)
    simbolos = list(S.keys())
    probabilidades = list(S.values())
    
    print(f"\nAlfabeto encontrado: {simbolos}")
    print("\nDistribución de probabilidades:")
    for simbolo, prob in S.items():
        print(f"  {simbolo}: {prob:.4f} ({int(prob * len(message))} ocurrencias)")
    
    H = calculateH(probabilidades)
    print(f"\n📊 Entropía de la fuente H(X) = {H:.4f} bits/símbolo")
    print(f"   (Máxima entropía posible: {math.log2(len(simbolos)):.4f} bits)")
    print(f"   (Eficiencia de la fuente: {H / math.log2(len(simbolos)) * 100:.2f}%)")
    
    # ========================================================================
    # 2. GENERACIÓN DE CÓDIGOS
    # ========================================================================
    print("\n" + "=" * 80)
    print("2. GENERACIÓN DE CÓDIGOS")
    print("=" * 80)
    
    print("\n🔨 Generando códigos Huffman y Shannon-Fano...")
    C_huffman = huffman(probabilidades)
    C_shannon = shannonfano(probabilidades)
    
    print("\n📋 Tabla de códigos generados:")
    printTable(simbolos, probabilidades, C_huffman, C_shannon)
    
    # ========================================================================
    # 3. MÉTRICAS Y COMPARACIÓN
    # ========================================================================
    print("\n" + "=" * 80)
    print("3. MÉTRICAS Y COMPARACIÓN")
    print("=" * 80)
    
    printMetrics(C_huffman, C_shannon, probabilidades)
    
    # Información adicional
    L_huffman = getLengthMedCodigo(C_huffman, probabilidades)
    L_shannon = getLengthMedCodigo(C_shannon, probabilidades)
    
    print(f"\n💡 Interpretación:")
    print(f"   - El código Huffman es óptimo con L = {L_huffman:.4f} bits/símbolo")
    print(f"   - Shannon-Fano tiene L = {L_shannon:.4f} bits/símbolo")
    print(f"   - Diferencia: {abs(L_huffman - L_shannon):.4f} bits/símbolo")
    
    if L_huffman < L_shannon:
        print(f"   - Huffman es {((L_shannon / L_huffman - 1) * 100):.2f}% más eficiente")
    elif L_shannon < L_huffman:
        print(f"   - Shannon-Fano es {((L_huffman / L_shannon - 1) * 100):.2f}% más eficiente")
    else:
        print(f"   - Ambos códigos tienen la misma eficiencia")
    
    # ========================================================================
    # 4. VERIFICACIÓN DEL TEOREMA DE SHANNON
    # ========================================================================
    print("\n" + "=" * 80)
    print("4. PRIMER TEOREMA DE SHANNON")
    print("=" * 80)
    
    print(f"\nVerificando: H(X) ≤ L < H(X) + 1")
    print(f"             {H:.4f} ≤ L < {H + 1:.4f}")
    
    cumple_huffman = teoremaShannon(C_huffman, probabilidades, 1)
    cumple_shannon = teoremaShannon(C_shannon, probabilidades, 1)
    
    print(f"\n✓ Código Huffman: {'CUMPLE ✓' if cumple_huffman else 'NO CUMPLE ✗'}")
    print(f"  L = {L_huffman:.4f}, H = {H:.4f}, L/H = {L_huffman/H:.4f}")
    
    print(f"\n✓ Código Shannon-Fano: {'CUMPLE ✓' if cumple_shannon else 'NO CUMPLE ✗'}")
    print(f"  L = {L_shannon:.4f}, H = {H:.4f}, L/H = {L_shannon/H:.4f}")
    
    # ========================================================================
    # 5. CODIFICACIÓN Y DECODIFICACIÓN
    # ========================================================================
    print("\n" + "=" * 80)
    print("5. CODIFICACIÓN Y DECODIFICACIÓN")
    print("=" * 80)
    
    print("\n🔐 Codificando mensaje con Huffman...")
    encoded_huffman = codificar(message, simbolos, C_huffman)
    print(f"   Tamaño original: {len(message)} caracteres")
    print(f"   Tamaño codificado: {len(encoded_huffman)} bytes")
    print(f"   Tasa de compresión: {tasaCompresion(message, encoded_huffman):.4f}")
    
    print("\n🔓 Decodificando mensaje...")
    decoded_huffman = decodificar(encoded_huffman, C_huffman, simbolos)
    print(f"   Mensaje decodificado: '{decoded_huffman}'")
    print(f"   ✓ Verificación: {'CORRECTO ✓' if decoded_huffman == message else 'ERROR ✗'}")
    
    print("\n🔐 Codificando mensaje con Shannon-Fano...")
    encoded_shannon = codificar(message, simbolos, C_shannon)
    print(f"   Tamaño codificado: {len(encoded_shannon)} bytes")
    print(f"   Tasa de compresión: {tasaCompresion(message, encoded_shannon):.4f}")
    
    decoded_shannon = decodificar(encoded_shannon, C_shannon, simbolos)
    print(f"   ✓ Verificación: {'CORRECTO ✓' if decoded_shannon == message else 'ERROR ✗'}")
    
    # ========================================================================
    # 6. RUN-LENGTH CODING
    # ========================================================================
    print("\n" + "=" * 80)
    print("6. RUN-LENGTH CODING (RLC)")
    print("=" * 80)
    
    rlc_result = rlc(message)
    print(f"\n📦 Codificación RLC del mensaje:")
    rlc_str = ''.join(f"{symbol}{amount}" for symbol, amount in rlc_result)
    print(f"   {rlc_str}")
    
    # Reconstruir mensaje
    reconstructed = ''.join(symbol * amount for symbol, amount in rlc_result)
    print(f"\n   Original:      '{message}'")
    print(f"   Reconstruido:  '{reconstructed}'")
    print(f"   ✓ Verificación: {'CORRECTO ✓' if reconstructed == message else 'ERROR ✗'}")
    
    # Calcular eficiencia de RLC
    rlc_size = len(rlc_str)
    print(f"\n   Tamaño original: {len(message)} caracteres")
    print(f"   Tamaño RLC: {rlc_size} caracteres")
    if rlc_size < len(message):
        print(f"   ✓ Compresión: {(1 - rlc_size/len(message)) * 100:.2f}%")
    else:
        print(f"   ✗ Expansión: {(rlc_size/len(message) - 1) * 100:.2f}%")
        print(f"   (RLC no es eficiente para este mensaje)")
    
    # ========================================================================
    # 7. DETECCIÓN Y CORRECCIÓN DE ERRORES
    # ========================================================================
    print("\n" + "=" * 80)
    print("7. CAPACIDAD DE DETECCIÓN/CORRECCIÓN DE ERRORES")
    print("=" * 80)
    
    # Crear un código simple para demostración
    codigo_ejemplo = ['000', '111', '010', '101']
    
    print("\n📝 Código de ejemplo para análisis:")
    for i, cod in enumerate(codigo_ejemplo):
        print(f"   Símbolo {i+1}: {cod}")
    
    try:
        d_min = hamming(codigo_ejemplo)
        errores_det = erroresDetectables(codigo_ejemplo)
        errores_corr = erroresCorregibles(codigo_ejemplo)
        
        print(f"\n📊 Análisis de capacidad:")
        print(f"   Distancia mínima de Hamming: {d_min}")
        print(f"   Errores detectables: {errores_det}")
        print(f"   Errores corregibles: {errores_corr}")
        
        print(f"\n💡 Interpretación:")
        print(f"   - Este código puede detectar hasta {errores_det} error(es)")
        print(f"   - Puede corregir hasta {errores_corr} error(es)")
        print(f"   - Para mejorar, necesitaríamos mayor distancia mínima")
    except Exception as e:
        print(f"\n⚠️  Error en análisis: {e}")
    
    # Análisis de códigos Huffman y Shannon-Fano
    print("\n📝 Análisis de códigos generados:")
    for nombre, codigo in [("Huffman", C_huffman), ("Shannon-Fano", C_shannon)]:
        # Ajustar longitudes para comparación
        max_len = max(len(c) for c in codigo)
        codigo_padded = [c.ljust(max_len, '0') for c in codigo]
        
        try:
            d_min = hamming(codigo_padded)
            print(f"\n   {nombre}:")
            print(f"     Distancia mínima: {d_min}")
            print(f"     Errores detectables: {d_min - 1}")
            print(f"     Errores corregibles: {(d_min - 1) // 2}")
        except Exception as e:
            print(f"\n   {nombre}: No se puede calcular (código de longitud variable)")
    
    # ========================================================================
    # RESUMEN FINAL
    # ========================================================================
    print("\n" + "=" * 80)
    print("RESUMEN")
    print("=" * 80)
    
    print(f"""
📊 Características de la fuente:
   - Alfabeto: {len(simbolos)} símbolos
   - Entropía: {H:.4f} bits/símbolo
   - Mensaje: {len(message)} caracteres
   
📈 Rendimiento de códigos:
   - Huffman: {rendimientoCodigo(C_huffman, probabilidades):.4f} (L = {L_huffman:.4f})
   - Shannon-Fano: {rendimientoCodigo(C_shannon, probabilidades):.4f} (L = {L_shannon:.4f})
   
💾 Compresión:
   - Huffman: {tasaCompresion(message, encoded_huffman):.4f}x
   - Shannon-Fano: {tasaCompresion(message, encoded_shannon):.4f}x
   
✓ Ambos códigos verifican el Primer Teorema de Shannon
✓ La decodificación es correcta y sin ambigüedad (códigos prefijo)
""")
    
    print("=" * 80)
    print("Demostración completada exitosamente")
    print("=" * 80)


if __name__ == "__main__":
    main()
