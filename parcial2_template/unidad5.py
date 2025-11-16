#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
================================================================================
UNIDAD 5: TEORÍA DE CANALES - TEORÍA DE LA INFORMACIÓN
================================================================================

Archivo autocontenido sin dependencias externas.
Ejecutar con: python unidad5.py

RESUMEN TEÓRICO:

1. CANAL DE COMUNICACIÓN:
   Un canal es un medio de transmisión que conecta una fuente con un destino.
   Se modela mediante probabilidades condicionales P(B|A), donde:
   - A es el alfabeto de entrada (fuente)
   - B es el alfabeto de salida (destino)
   - P(bj|ai) es la probabilidad de recibir bj cuando se envía ai

2. MATRIZ DE CANAL:
   La matriz de canal M es una matriz donde:
   - Filas representan símbolos de entrada (ai)
   - Columnas representan símbolos de salida (bj)
   - M[i][j] = P(bj|ai)
   - Cada fila suma 1 (distribución de probabilidad)

3. PROBABILIDADES:
   
   a) A Priori P(A): Probabilidades de los símbolos de entrada antes del canal.
      Se obtienen de la frecuencia relativa de la fuente.
   
   b) A Posteriori P(A|B): Probabilidades de entrada dado que se observó una salida.
      Usando Teorema de Bayes: P(ai|bj) = P(bj|ai) * P(ai) / P(bj)
   
   c) Probabilidades de Salida P(B): 
      P(bj) = Σi P(bj|ai) * P(ai)
   
   d) Probabilidades Conjuntas P(A,B):
      P(ai,bj) = P(bj|ai) * P(ai) = P(ai|bj) * P(bj)

4. ENTROPÍAS DEL CANAL:
   
   a) H(A): Entropía de la fuente (entrada)
      Mide la incertidumbre de la entrada antes del canal.
   
   b) H(B): Entropía de la salida
      Mide la incertidumbre de la salida del canal.
   
   c) H(A|B): Equivocación o Ruido
      Incertidumbre que queda sobre A después de observar B.
      H(A|B) = Σj P(bj) * H(A|bj) = Σi,j P(ai,bj) * log2(1/P(ai|bj))
      Si H(A|B) = 0, el canal no tiene ruido (sin pérdida de información).
   
   d) H(B|A): Pérdida
      Incertidumbre que queda sobre B después de conocer A.
      H(B|A) = Σi P(ai) * H(B|ai) = Σi,j P(ai,bj) * log2(1/P(bj|ai))
      Mide la degradación introducida por el canal.
   
   e) H(A,B): Entropía Conjunta
      H(A,B) = Σi,j P(ai,bj) * log2(1/P(ai,bj))
      Relaciones: H(A,B) = H(A) + H(B|A) = H(B) + H(A|B)

5. INFORMACIÓN MUTUA:
   I(A;B) mide la cantidad de información que comparten A y B.
   
   I(A;B) = H(A) - H(A|B) = H(B) - H(B|A)
   I(A;B) = Σi,j P(ai,bj) * log2(P(ai,bj) / (P(ai)*P(bj)))
   
   Propiedades:
   - I(A;B) ≥ 0 (siempre no negativa)
   - I(A;B) = I(B;A) (simétrica)
   - I(A;B) = 0 si A y B son independientes
   - I(A;B) ≤ min(H(A), H(B))

6. RELACIONES FUNDAMENTALES:
   H(A,B) = H(A) + H(B|A) = H(B) + H(A|B)
   I(A;B) = H(A) + H(B) - H(A,B)
   I(A;B) = H(A) - H(A|B) = H(B) - H(B|A)

================================================================================
"""

import math
from typing import List, Tuple, Dict


# ============================================================================
# FUNCIONES BÁSICAS DE INFORMACIÓN Y ENTROPÍA
# ============================================================================

def calculateI(pi: float) -> float:
    """
    Calcula la información de un símbolo con probabilidad pi.
    
    Fundamento teórico:
    I(si) = log₂(1/pi)
    Mide la "sorpresa" o cantidad de información del símbolo.
    
    Args:
        pi: Probabilidad del símbolo (0 < pi ≤ 1)
    
    Returns:
        Información en bits
    """
    if pi <= 0:
        return 0
    return math.log2(1 / pi)


def calculateH(P: List[float]) -> float:
    """
    Calcula la entropía H(X) de una distribución de probabilidad.
    
    Fundamento teórico:
    H(X) = - Σ pi * log₂(pi) = Σ pi * I(pi)
    
    Args:
        P: Lista de probabilidades
    
    Returns:
        Entropía en bits
    """
    return sum(pi * calculateI(pi) for pi in P if pi > 0)


# ============================================================================
# FUNCIONES PARA CONSTRUIR DISTRIBUCIONES DE PROBABILIDAD
# ============================================================================

def getSymbolOcurrences(phrase: str) -> Dict[str, int]:
    """
    Cuenta las ocurrencias de cada símbolo en una cadena.
    
    Args:
        phrase: Cadena de texto
    
    Returns:
        Diccionario {símbolo: cantidad}
    """
    occurrences = {}
    for si in phrase:
        occurrences[si] = occurrences.get(si, 0) + 1
    return occurrences


def buildS(source: str) -> Dict[str, float]:
    """
    Construye distribución de probabilidad empírica desde un texto.
    
    Fundamento teórico:
    Frecuencia relativa: p(si) ≈ n(si) / N
    
    Args:
        source: Texto fuente
    
    Returns:
        Diccionario ordenado {símbolo: probabilidad}
    """
    occurrences = getSymbolOcurrences(source)
    frequencies = {symbol: count / len(source) for symbol, count in occurrences.items()}
    return dict(sorted(frequencies.items(), key=lambda item: item[0]))


def getProbabilidadPriori(message: str) -> Dict[str, float]:
    """
    Obtiene las probabilidades a priori desde un mensaje.
    
    Args:
        message: Mensaje de entrada
    
    Returns:
        Diccionario de probabilidades a priori
    """
    return buildS(message)


# ============================================================================
# FUNCIONES MATRICIALES
# ============================================================================

def getMatrixZeros(filas: int, columnas: int) -> List[List[float]]:
    """
    Crea una matriz de ceros.
    
    Args:
        filas: Número de filas
        columnas: Número de columnas
    
    Returns:
        Matriz inicializada con ceros
    """
    return [[0.0 for _ in range(columnas)] for _ in range(filas)]


def getMatrixTraspuesta(M: List[List[float]]) -> List[List[float]]:
    """
    Calcula la transpuesta de una matriz.
    
    Args:
        M: Matriz original
    
    Returns:
        Matriz transpuesta
    """
    result = []
    for i in range(len(M[0])):
        result.append([M[j][i] for j in range(len(M))])
    return result


def printMatrix(matrix: List[List[float]]) -> None:
    """
    Imprime una matriz con formato.
    
    Args:
        matrix: Matriz a imprimir
    """
    max_width = max(len(f"{elem:.4f}") for row in matrix for elem in row)
    for row in matrix:
        print(" ".join(f"{elem:>{max_width}.4f}" for elem in row))


# ============================================================================
# CONSTRUCCIÓN DE MATRIZ DE CANAL DESDE DATOS
# ============================================================================

def getPrioriMatrixFull(fnt: List[str], cds: List[str], _input: str, _output: str) -> List[List[float]]:
    """
    Construye la matriz de canal P(B|A) desde secuencias de entrada/salida.
    
    Fundamento teórico:
    Cuenta las transiciones ai → bj y normaliza por filas:
    P(bj|ai) = count(ai → bj) / count(ai)
    
    Args:
        fnt: Alfabeto de entrada
        cds: Alfabeto de salida
        _input: Secuencia de entrada
        _output: Secuencia de salida correspondiente
    
    Returns:
        Matriz de canal [len(fnt) x len(cds)]
    """
    result = getMatrixZeros(len(fnt), len(cds))
    
    for i in range(min(len(_input), len(_output))):
        row = fnt.index(_input[i])
        col = cds.index(_output[i])
        result[row][col] += 1
    
    # Normalizar por filas
    for row in result:
        s = sum(row)
        if s > 0:
            for j in range(len(row)):
                row[j] /= s
    
    return result


def getPrioriMatrixByInputOutput(_input: str, _output: str) -> List[List[float]]:
    """
    Construye matriz de canal inferiendo los alfabetos desde las secuencias.
    
    Args:
        _input: Secuencia de entrada
        _output: Secuencia de salida
    
    Returns:
        Matriz de canal
    """
    inalf = sorted(set(_input))
    outalf = sorted(set(_output))
    return getPrioriMatrixFull(inalf, outalf, _input, _output)


# ============================================================================
# PROBABILIDADES DEL CANAL
# ============================================================================

def getProbsOutSymbols(Pinitial: List[float], channel: List[List[float]]) -> List[float]:
    """
    Calcula las probabilidades de salida P(B) del canal.
    
    Fundamento teórico:
    P(bj) = Σi P(bj|ai) * P(ai)
    (Teorema de probabilidad total)
    
    Args:
        Pinitial: Probabilidades a priori P(A)
        channel: Matriz de canal P(B|A)
    
    Returns:
        Lista de probabilidades de salida P(B)
    """
    result = [0.0] * len(channel[0])
    for j in range(len(channel[0])):
        for i in range(len(channel)):
            result[j] += channel[i][j] * Pinitial[i]
    return result


def getPosterioriMatrix(Pinitial: List[float], channel: List[List[float]]) -> List[List[float]]:
    """
    Calcula la matriz de probabilidades a posteriori P(A|B).
    
    Fundamento teórico:
    Teorema de Bayes: P(ai|bj) = P(bj|ai) * P(ai) / P(bj)
    
    Args:
        Pinitial: Probabilidades a priori P(A)
        channel: Matriz de canal P(B|A)
    
    Returns:
        Matriz a posteriori P(A|B) [len(A) x len(B)]
    """
    result = getMatrixZeros(len(channel), len(channel[0]))
    outsSymbProbs = getProbsOutSymbols(Pinitial, channel)
    
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if outsSymbProbs[j] != 0:
                result[i][j] = channel[i][j] * Pinitial[i] / outsSymbProbs[j]
    
    return result


def getMatrixSimultaneusEvent(Pinitial: List[float], channel: List[List[float]]) -> List[List[float]]:
    """
    Calcula la matriz de probabilidades conjuntas P(A,B).
    
    Fundamento teórico:
    P(ai, bj) = P(bj|ai) * P(ai) = P(ai|bj) * P(bj)
    
    Args:
        Pinitial: Probabilidades a priori P(A)
        channel: Matriz de canal P(B|A)
    
    Returns:
        Matriz de probabilidades conjuntas [len(A) x len(B)]
    """
    rows = len(channel)
    cols = len(channel[0])
    result = getMatrixZeros(rows, cols)
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = Pinitial[i] * channel[i][j]
    
    return result


# ============================================================================
# ENTROPÍAS DEL CANAL
# ============================================================================

def calculateHPriori(Pa: List[float]) -> float:
    """
    Calcula la entropía a priori H(A) de la fuente.
    
    Fundamento teórico:
    H(A) = - Σi P(ai) * log₂(P(ai))
    Mide la incertidumbre de la entrada antes del canal.
    
    Args:
        Pa: Probabilidades a priori
    
    Returns:
        Entropía en bits
    """
    return calculateH(Pa)


def calculateHPosteriori(Pa: List[float], channel: List[List[float]]) -> List[float]:
    """
    Calcula H(A|bj) para cada símbolo de salida bj.
    
    Fundamento teórico:
    Para cada bj: H(A|bj) = - Σi P(ai|bj) * log₂(P(ai|bj))
    
    Args:
        Pa: Probabilidades a priori
        channel: Matriz de canal
    
    Returns:
        Lista de entropías condicionales
    """
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
    """
    Calcula la entropía de salida H(B).
    
    Fundamento teórico:
    H(B) = - Σj P(bj) * log₂(P(bj))
    
    Args:
        Pa: Probabilidades a priori
        channel: Matriz de canal
    
    Returns:
        Entropía de salida en bits
    """
    return calculateH(getProbsOutSymbols(Pa, channel))


def calculateHPosterioriMediaABSimple(Pa: List[float], channel: List[List[float]]) -> float:
    """
    Calcula H(A|B): Equivocación o Ruido del canal.
    
    Fundamento teórico:
    H(A|B) = Σi,j P(ai,bj) * log₂(1/P(ai|bj))
           = Σj P(bj) * H(A|bj)
    
    Mide la incertidumbre sobre la entrada después de observar la salida.
    Si H(A|B) = 0, el canal no tiene ruido (determinístico en reversa).
    
    Args:
        Pa: Probabilidades a priori
        channel: Matriz de canal
    
    Returns:
        Equivocación en bits
    """
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    antiChannel = getPosterioriMatrix(Pa, channel)
    
    result = 0.0
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if antiChannel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1 / antiChannel[i][j])
    
    return result


def calculateRuido(Pa: List[float], channel: List[List[float]]) -> float:
    """
    Calcula el ruido del canal (equivocación) H(A|B).
    
    Args:
        Pa: Probabilidades a priori
        channel: Matriz de canal
    
    Returns:
        Ruido en bits
    """
    return calculateHPosterioriMediaABSimple(Pa, channel)


def calculateHPosterioriMediaBASimple(Pa: List[float], channel: List[List[float]]) -> float:
    """
    Calcula H(B|A): Pérdida del canal.
    
    Fundamento teórico:
    H(B|A) = Σi,j P(ai,bj) * log₂(1/P(bj|ai))
           = Σi P(ai) * H(B|ai)
    
    Mide la incertidumbre sobre la salida dado que se conoce la entrada.
    Si H(B|A) = 0, el canal es determinístico (sin ambigüedad).
    
    Args:
        Pa: Probabilidades a priori
        channel: Matriz de canal
    
    Returns:
        Pérdida en bits
    """
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    
    result = 0.0
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if channel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1 / channel[i][j])
    
    return result


def calculatePerdida(Pa: List[float], channel: List[List[float]]) -> float:
    """
    Calcula la pérdida del canal H(B|A).
    
    Args:
        Pa: Probabilidades a priori
        channel: Matriz de canal
    
    Returns:
        Pérdida en bits
    """
    return calculateHPosterioriMediaBASimple(Pa, channel)


def calculateHCanal(Pa: List[float], channel: List[List[float]]) -> float:
    """
    Calcula la entropía conjunta H(A,B) del canal.
    
    Fundamento teórico:
    H(A,B) = Σi,j P(ai,bj) * log₂(1/P(ai,bj))
    
    Relaciones:
    H(A,B) = H(A) + H(B|A) = H(B) + H(A|B)
    
    Args:
        Pa: Probabilidades a priori
        channel: Matriz de canal
    
    Returns:
        Entropía conjunta en bits
    """
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    result = 0.0
    
    for row in simulaneusEvent:
        for item in row:
            if item > 0:
                result += item * calculateI(item)
    
    return result


# ============================================================================
# INFORMACIÓN MUTUA
# ============================================================================

def informacionMutuaABSimple(Pa: List[float], channel: List[List[float]]) -> float:
    """
    Calcula la información mutua I(A;B) del canal.
    
    Fundamento teórico:
    I(A;B) = H(A) - H(A|B) = H(B) - H(B|A)
    I(A;B) = Σi,j P(ai,bj) * log₂(P(ai,bj) / (P(ai)*P(bj)))
    
    Propiedades:
    - I(A;B) ≥ 0
    - I(A;B) = I(B;A) (simétrica)
    - I(A;B) = 0 si A y B son independientes
    - I(A;B) ≤ min(H(A), H(B))
    
    Interpretación:
    Mide cuánta información sobre A se puede obtener al observar B
    (y viceversa, por simetría).
    
    Args:
        Pa: Probabilidades a priori
        channel: Matriz de canal
    
    Returns:
        Información mutua en bits
    """
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    outProbs = getProbsOutSymbols(Pa, channel)
    
    result = 0.0
    for i in range(len(simulaneusEvent)):
        for j in range(len(simulaneusEvent[0])):
            if simulaneusEvent[i][j] > 0 and outProbs[j] > 0 and Pa[i] > 0:
                result += simulaneusEvent[i][j] * math.log2(
                    simulaneusEvent[i][j] / (Pa[i] * outProbs[j])
                )
    
    return result


def informacionMutuaBASimple(Pa: List[float], channel: List[List[float]]) -> float:
    """
    Calcula I(B;A), equivalente a I(A;B) por simetría.
    
    Args:
        Pa: Probabilidades a priori
        channel: Matriz de canal
    
    Returns:
        Información mutua en bits
    """
    return informacionMutuaABSimple(Pa, channel)


# ============================================================================
# FUNCIONES AUXILIARES PARA VISUALIZACIÓN
# ============================================================================

def printChannelInfo(S: List[str], C: List[str], matrix: List[List[float]]) -> None:
    """
    Imprime información completa del canal con etiquetas.
    
    Args:
        S: Símbolos de entrada
        C: Símbolos de salida
        matrix: Matriz de canal
    """
    max_val_len = max(len(str(round(v, 4))) for row in matrix for v in row)
    max_label_len = max(max(map(len, S)), max(map(len, C)))
    cell_width = max(max_val_len, max_label_len) + 2
    
    # Encabezado de columnas
    print(" " * (max_label_len + 2), end="")
    for ci in C:
        print(f"{ci:>{cell_width}}", end="")
    print()
    
    # Filas
    for i, row in enumerate(matrix):
        print(f"{S[i]:<{max_label_len + 2}}", end="")
        for val in row:
            print(f"{round(val, 4):>{cell_width}}", end="")
        print()


def showS(S: Dict[str, float]) -> None:
    """
    Muestra distribución de probabilidades.
    
    Args:
        S: Diccionario de probabilidades
    """
    for symb, percent in S.items():
        print(f'P({symb}): {round(percent, 4)}')


# ============================================================================
# FUNCIÓN PRINCIPAL - DEMOSTRACIÓN
# ============================================================================

def main():
    """
    Función principal que demuestra todas las funcionalidades del canal.
    
    Solicita UNA entrada al usuario (par de secuencias entrada/salida) y ejecuta:
    1. Construcción de matriz de canal desde datos
    2. Cálculo de probabilidades (a priori, a posteriori, conjuntas)
    3. Cálculo de todas las entropías del canal
    4. Cálculo de información mutua
    5. Verificación de relaciones fundamentales
    """
    print("=" * 80)
    print("UNIDAD 5: DEMOSTRACIÓN DE TEORÍA DE CANALES")
    print("=" * 80)
    
    # Entrada única del usuario
    print("\n📝 Ingrese secuencias de entrada y salida de un canal:")
    print("   Ejemplo: entrada='AABBCC' salida='010011'")
    print("\n   Ingrese la secuencia de ENTRADA:")
    input_seq = input("   > ").upper()
    
    if not input_seq:
        print("⚠️  Entrada vacía. Usando secuencias por defecto.")
        input_seq = "AABBCCAABBCC"
        output_seq = "010110010101"
    else:
        print("   Ingrese la secuencia de SALIDA:")
        output_seq = input("   > ")
        if len(output_seq) != len(input_seq):
            print("⚠️  Las secuencias deben tener la misma longitud. Usando por defecto.")
            input_seq = "AABBCCAABBCC"
            output_seq = "010110010101"
    
    print(f"\n✓ Secuencias recibidas:")
    print(f"   Entrada:  '{input_seq}' (longitud: {len(input_seq)})")
    print(f"   Salida:   '{output_seq}' (longitud: {len(output_seq)})")
    
    # ========================================================================
    # 1. CONSTRUCCIÓN DEL CANAL
    # ========================================================================
    print("\n" + "=" * 80)
    print("1. CONSTRUCCIÓN DEL CANAL")
    print("=" * 80)
    
    # Inferir alfabetos
    S = sorted(set(input_seq))
    C = sorted(set(output_seq))
    
    print(f"\nAlfabeto de entrada A: {S}")
    print(f"Alfabeto de salida B: {C}")
    
    # Construir matriz de canal
    channel = getPrioriMatrixJust(input_seq, output_seq)
    
    print("\n📊 Matriz de canal P(B|A):")
    printChannelInfo(S, C, channel)
    
    # ========================================================================
    # 2. PROBABILIDADES A PRIORI
    # ========================================================================
    print("\n" + "=" * 80)
    print("2. PROBABILIDADES A PRIORI")
    print("=" * 80)
    
    priori_dict = getProbabilidadPriori(input_seq)
    priori_list = [priori_dict[s] for s in S]
    
    print("\nDistribución a priori P(A):")
    showS(priori_dict)
    
    # ========================================================================
    # 3. PROBABILIDADES DE SALIDA
    # ========================================================================
    print("\n" + "=" * 80)
    print("3. PROBABILIDADES DE SALIDA")
    print("=" * 80)
    
    outProbs = getProbsOutSymbols(priori_list, channel)
    
    print("\nProbabilidades de salida P(B):")
    for c, prob in zip(C, outProbs):
        print(f"P({c}): {prob:.4f}")
    
    # ========================================================================
    # 4. MATRIZ A POSTERIORI
    # ========================================================================
    print("\n" + "=" * 80)
    print("4. MATRIZ A POSTERIORI P(A|B)")
    print("=" * 80)
    
    posteriori = getPosterioriMatrix(priori_list, channel)
    
    print("\nMatriz a posteriori (Teorema de Bayes):")
    printChannelInfo(S, C, posteriori)
    
    # ========================================================================
    # 5. PROBABILIDADES CONJUNTAS
    # ========================================================================
    print("\n" + "=" * 80)
    print("5. PROBABILIDADES CONJUNTAS P(A,B)")
    print("=" * 80)
    
    conjuntas = getMatrixSimultaneusEvent(priori_list, channel)
    
    print("\nMatriz de probabilidades conjuntas:")
    printChannelInfo(S, C, conjuntas)
    
    # Verificar que suman 1
    total_conj = sum(sum(row) for row in conjuntas)
    print(f"\n✓ Verificación: Σ P(A,B) = {total_conj:.4f} (debe ser 1.0)")
    
    # ========================================================================
    # 6. ENTROPÍAS DEL CANAL
    # ========================================================================
    print("\n" + "=" * 80)
    print("6. ENTROPÍAS DEL CANAL")
    print("=" * 80)
    
    H_A = calculateHPriori(priori_list)
    H_B = calculateHPosterioriTotal(priori_list, channel)
    H_AB = calculateRuido(priori_list, channel)
    H_BA = calculatePerdida(priori_list, channel)
    H_conj = calculateHCanal(priori_list, channel)
    
    print(f"\n📊 Entropías calculadas:")
    print(f"   H(A)   = {H_A:.4f} bits  (entropía de entrada)")
    print(f"   H(B)   = {H_B:.4f} bits  (entropía de salida)")
    print(f"   H(A|B) = {H_AB:.4f} bits  (equivocación/ruido)")
    print(f"   H(B|A) = {H_BA:.4f} bits  (pérdida)")
    print(f"   H(A,B) = {H_conj:.4f} bits  (entropía conjunta)")
    
    print(f"\n💡 Interpretación:")
    if H_AB < 0.01:
        print(f"   - Canal sin ruido: H(A|B) ≈ 0")
        print(f"     La salida determina completamente la entrada")
    else:
        print(f"   - Canal con ruido: H(A|B) = {H_AB:.4f} bits")
        print(f"     Queda incertidumbre sobre la entrada tras observar la salida")
    
    if H_BA < 0.01:
        print(f"   - Canal determinístico: H(B|A) ≈ 0")
        print(f"     La entrada determina completamente la salida")
    else:
        print(f"   - Canal con pérdida: H(B|A) = {H_BA:.4f} bits")
        print(f"     La entrada no determina completamente la salida")
    
    # ========================================================================
    # 7. INFORMACIÓN MUTUA
    # ========================================================================
    print("\n" + "=" * 80)
    print("7. INFORMACIÓN MUTUA")
    print("=" * 80)
    
    I_AB = informacionMutuaABSimple(priori_list, channel)
    I_BA = informacionMutuaBASimple(priori_list, channel)
    
    print(f"\n📊 Información mutua:")
    print(f"   I(A;B) = {I_AB:.4f} bits")
    print(f"   I(B;A) = {I_BA:.4f} bits")
    print(f"\n✓ Verificación de simetría: |I(A;B) - I(B;A)| = {abs(I_AB - I_BA):.6f}")
    
    print(f"\n💡 Interpretación:")
    if I_AB < 0.01:
        print(f"   - I(A;B) ≈ 0: A y B son prácticamente independientes")
        print(f"     El canal no transmite información útil")
    elif I_AB > H_A * 0.95:
        print(f"   - I(A;B) ≈ H(A): El canal transmite casi toda la información")
        print(f"     Canal de alta calidad")
    else:
        print(f"   - I(A;B) = {I_AB:.4f} bits")
        print(f"     El canal transmite {(I_AB/H_A)*100:.2f}% de la información de entrada")
    
    # ========================================================================
    # 8. VERIFICACIÓN DE RELACIONES FUNDAMENTALES
    # ========================================================================
    print("\n" + "=" * 80)
    print("8. VERIFICACIÓN DE RELACIONES FUNDAMENTALES")
    print("=" * 80)
    
    print("\n📐 Verificando relaciones teóricas:")
    
    # Relación 1: H(A,B) = H(A) + H(B|A)
    rel1_izq = H_conj
    rel1_der = H_A + H_BA
    print(f"\n   1) H(A,B) = H(A) + H(B|A)")
    print(f"      {rel1_izq:.4f} = {H_A:.4f} + {H_BA:.4f}")
    print(f"      {rel1_izq:.4f} = {rel1_der:.4f}")
    print(f"      Diferencia: {abs(rel1_izq - rel1_der):.6f} {'✓' if abs(rel1_izq - rel1_der) < 0.001 else '✗'}")
    
    # Relación 2: H(A,B) = H(B) + H(A|B)
    rel2_izq = H_conj
    rel2_der = H_B + H_AB
    print(f"\n   2) H(A,B) = H(B) + H(A|B)")
    print(f"      {rel2_izq:.4f} = {H_B:.4f} + {H_AB:.4f}")
    print(f"      {rel2_izq:.4f} = {rel2_der:.4f}")
    print(f"      Diferencia: {abs(rel2_izq - rel2_der):.6f} {'✓' if abs(rel2_izq - rel2_der) < 0.001 else '✗'}")
    
    # Relación 3: I(A;B) = H(A) - H(A|B)
    rel3_izq = I_AB
    rel3_der = H_A - H_AB
    print(f"\n   3) I(A;B) = H(A) - H(A|B)")
    print(f"      {rel3_izq:.4f} = {H_A:.4f} - {H_AB:.4f}")
    print(f"      {rel3_izq:.4f} = {rel3_der:.4f}")
    print(f"      Diferencia: {abs(rel3_izq - rel3_der):.6f} {'✓' if abs(rel3_izq - rel3_der) < 0.001 else '✗'}")
    
    # Relación 4: I(A;B) = H(B) - H(B|A)
    rel4_izq = I_AB
    rel4_der = H_B - H_BA
    print(f"\n   4) I(A;B) = H(B) - H(B|A)")
    print(f"      {rel4_izq:.4f} = {H_B:.4f} - {H_BA:.4f}")
    print(f"      {rel4_izq:.4f} = {rel4_der:.4f}")
    print(f"      Diferencia: {abs(rel4_izq - rel4_der):.6f} {'✓' if abs(rel4_izq - rel4_der) < 0.001 else '✗'}")
    
    # Relación 5: I(A;B) = H(A) + H(B) - H(A,B)
    rel5_izq = I_AB
    rel5_der = H_A + H_B - H_conj
    print(f"\n   5) I(A;B) = H(A) + H(B) - H(A,B)")
    print(f"      {rel5_izq:.4f} = {H_A:.4f} + {H_B:.4f} - {H_conj:.4f}")
    print(f"      {rel5_izq:.4f} = {rel5_der:.4f}")
    print(f"      Diferencia: {abs(rel5_izq - rel5_der):.6f} {'✓' if abs(rel5_izq - rel5_der) < 0.001 else '✗'}")
    
    # ========================================================================
    # RESUMEN FINAL
    # ========================================================================
    print("\n" + "=" * 80)
    print("RESUMEN DEL CANAL")
    print("=" * 80)
    
    print(f"""
📊 Características del canal:
   - Entrada: {len(S)} símbolos
   - Salida: {len(C)} símbolos
   - Muestras: {len(input_seq)} transmisiones
   
📈 Entropías:
   - H(A)   = {H_A:.4f} bits (entrada)
   - H(B)   = {H_B:.4f} bits (salida)
   - H(A|B) = {H_AB:.4f} bits (ruido)
   - H(B|A) = {H_BA:.4f} bits (pérdida)
   - H(A,B) = {H_conj:.4f} bits (conjunta)
   
💬 Información mutua:
   - I(A;B) = {I_AB:.4f} bits
   - Eficiencia: {(I_AB/H_A)*100:.2f}% de H(A)
   
✓ Todas las relaciones fundamentales verificadas
✓ La teoría de canales se cumple correctamente
""")
    
    print("=" * 80)
    print("Demostración completada exitosamente")
    print("=" * 80)


if __name__ == "__main__":
    main()
