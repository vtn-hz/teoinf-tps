#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
================================================================================
UNIDAD 6: PROPIEDADES Y CAPACIDAD DE CANALES - TEORÍA DE LA INFORMACIÓN
================================================================================

Archivo autocontenido sin dependencias externas.
Ejecutar con: python unidad6.py

RESUMEN TEÓRICO:

1. PROPIEDADES DE CANALES:
   
   a) Canal Sin Ruido (Noiseless Channel):
      Un canal es sin ruido si cada símbolo de salida proviene de un único
      símbolo de entrada. Matemáticamente, en cada columna de P(B|A) hay a
      lo más un elemento no nulo.
      
      Propiedad: H(A|B) = 0 (no hay equivocación)
      
   b) Canal Determinístico (Deterministic Channel):
      Un canal es determinístico si cada símbolo de entrada produce un único
      símbolo de salida. En cada fila de P(B|A) hay exactamente un 1 y el
      resto son 0.
      
      Propiedad: H(B|A) = 0 (no hay pérdida)
      
   c) Canal Uniforme:
      Un canal es uniforme si todas las filas de P(B|A) son permutaciones
      de la misma distribución de probabilidad.
      
   d) Canal Simétrico:
      Un canal es simétrico si es uniforme Y además todas las columnas son
      permutaciones de la misma distribución.

2. CAPACIDAD DEL CANAL:
   La capacidad C de un canal es la máxima información mutua sobre todas
   las posibles distribuciones de entrada:
   
   C = max_{P(A)} I(A;B)
   
   Casos especiales:
   - Canal sin ruido: C = log₂(|A|)
   - Canal determinístico: C = log₂(|B|)
   - Canal uniforme: C = log₂(|B|) - H(fila)
   
   Para canales binarios, se puede encontrar numéricamente maximizando I(A;B).

3. CANALES EN SERIE (COMPOSICIÓN):
   Cuando dos canales A→B y B→C se conectan en serie, el canal resultante
   A→C se obtiene multiplicando las matrices de canal:
   
   P(C|A) = P(B|A) × P(C|B)
   
   La información mutua del canal compuesto cumple:
   I(A;C) ≤ min(I(A;B), I(B;C))

4. REDUCCIÓN DE CANALES:
   Dos columnas j₁ y j₂ de un canal pueden combinarse si existe una constante
   k tal que para toda fila i:
   P(bⱼ₁|aᵢ) = k · P(bⱼ₂|aᵢ)
   
   La reducción no cambia la información mutua del canal.
   Un canal reducido es el canal con el menor número de símbolos de salida
   que preserva la información mutua.

5. PROBABILIDAD DE ERROR:
   Bajo la regla ML (Maximum Likelihood), se asigna cada salida a la entrada
   más probable. La probabilidad de error es:
   
   Pₑ = Σᵢ P(aᵢ) · (1 - max_j P(bⱼ|aᵢ))

================================================================================
"""

import math
from typing import List, Tuple, Dict, Optional


# ============================================================================
# FUNCIONES BÁSICAS (REQUERIDAS PARA CÁLCULOS)
# ============================================================================

def calculateI(pi: float) -> float:
    """Calcula la información I(x) = log₂(1/p)."""
    if pi <= 0:
        return 0
    return math.log2(1 / pi)


def calculateH(P: List[float]) -> float:
    """Calcula la entropía H(X) = Σ p·log₂(1/p)."""
    return sum(pi * calculateI(pi) for pi in P if pi > 0)


def getMatrixZeros(filas: int, columnas: int) -> List[List[float]]:
    """Crea una matriz de ceros."""
    return [[0.0 for _ in range(columnas)] for _ in range(filas)]


def getMatrixProduct(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Multiplica dos matrices: C = A × B.
    
    Fundamento teórico:
    Para canales en serie, P(C|A) = P(B|A) × P(C|B)
    
    Args:
        A: Matriz [n × m]
        B: Matriz [m × p]
    
    Returns:
        Matriz producto [n × p]
    """
    if len(A[0]) != len(B):
        raise Exception("Las matrices no son compatibles para multiplicación")
    
    result = getMatrixZeros(len(A), len(B[0]))
    
    for i in range(len(A)):
        for k in range(len(B[0])):
            amount = 0.0
            for j in range(len(B)):
                amount += A[i][j] * B[j][k]
            result[i][k] = amount
    
    return result


def printMatrix(matrix: List[List[float]]) -> None:
    """Imprime una matriz con formato."""
    max_width = max(len(f"{elem:.4f}") for row in matrix for elem in row)
    for row in matrix:
        print(" ".join(f"{elem:>{max_width}.4f}" for elem in row))


# ============================================================================
# PROBABILIDADES DEL CANAL
# ============================================================================

def getProbsOutSymbols(Pinitial: List[float], channel: List[List[float]]) -> List[float]:
    """
    Calcula P(B) = Σᵢ P(bⱼ|aᵢ) · P(aᵢ).
    
    Args:
        Pinitial: Probabilidades a priori P(A)
        channel: Matriz P(B|A)
    
    Returns:
        Probabilidades de salida P(B)
    """
    result = [0.0] * len(channel[0])
    for j in range(len(channel[0])):
        for i in range(len(channel)):
            result[j] += channel[i][j] * Pinitial[i]
    return result


def getPosterioriMatrix(Pinitial: List[float], channel: List[List[float]]) -> List[List[float]]:
    """
    Calcula P(A|B) usando Teorema de Bayes.
    
    Args:
        Pinitial: P(A)
        channel: P(B|A)
    
    Returns:
        Matriz P(A|B)
    """
    result = getMatrixZeros(len(channel), len(channel[0]))
    outsSymbProbs = getProbsOutSymbols(Pinitial, channel)
    
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if outsSymbProbs[j] != 0:
                result[i][j] = channel[i][j] * Pinitial[i] / outsSymbProbs[j]
    
    return result


def getMatrixSimultaneusEvent(Pinitial: List[float], channel: List[List[float]]) -> List[List[float]]:
    """Calcula P(A,B) = P(B|A) · P(A)."""
    rows = len(channel)
    cols = len(channel[0])
    result = getMatrixZeros(rows, cols)
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = Pinitial[i] * channel[i][j]
    
    return result


# ============================================================================
# INFORMACIÓN MUTUA Y ENTROPÍAS
# ============================================================================

def informacionMutuaABSimple(Pa: List[float], channel: List[List[float]]) -> float:
    """
    Calcula I(A;B) = Σᵢⱼ P(aᵢ,bⱼ) · log₂(P(aᵢ,bⱼ) / (P(aᵢ)·P(bⱼ))).
    
    Fundamento teórico:
    I(A;B) mide cuánta información sobre A se obtiene al observar B.
    
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


def calculateRuido(Pa: List[float], channel: List[List[float]]) -> float:
    """
    Calcula H(A|B): equivocación del canal.
    
    Returns:
        Ruido en bits
    """
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    antiChannel = getPosterioriMatrix(Pa, channel)
    
    result = 0.0
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if antiChannel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1 / antiChannel[i][j])
    
    return result


def calculatePerdida(Pa: List[float], channel: List[List[float]]) -> float:
    """
    Calcula H(B|A): pérdida del canal.
    
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


# ============================================================================
# PROPIEDADES DE CANALES
# ============================================================================

def isCanalNoRuido(channel: List[List[float]]) -> bool:
    """
    Verifica si el canal es sin ruido (noiseless).
    
    Fundamento teórico:
    Un canal es sin ruido si cada columna tiene a lo más un elemento no nulo.
    Esto significa que cada símbolo de salida proviene de un único símbolo
    de entrada, por lo que H(A|B) = 0.
    
    Args:
        channel: Matriz de canal P(B|A)
    
    Returns:
        True si el canal es sin ruido
    """
    for j in range(len(channel[0])):
        amount = 0
        for i in range(len(channel)):
            if channel[i][j] != 0:
                amount += 1
                if amount > 1:
                    return False
    return True


def isCanalDeterminante(channel: List[List[float]]) -> bool:
    """
    Verifica si el canal es determinístico.
    
    Fundamento teórico:
    Un canal es determinístico si cada fila tiene exactamente un 1 y el
    resto son 0. Esto significa que cada entrada produce una única salida,
    por lo que H(B|A) = 0.
    
    Args:
        channel: Matriz de canal P(B|A)
    
    Returns:
        True si el canal es determinístico
    """
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
    """
    Verifica si el canal es uniforme.
    
    Fundamento teórico:
    Un canal es uniforme si todas las filas son permutaciones de la misma
    distribución de probabilidad. Esto simplifica el cálculo de capacidad.
    
    Args:
        channel: Matriz de canal P(B|A)
    
    Returns:
        True si el canal es uniforme
    """
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
    """
    Verifica si el canal es simétrico.
    
    Fundamento teórico:
    Un canal es simétrico si:
    1. Es uniforme (filas son permutaciones de la misma distribución)
    2. Las columnas también son permutaciones de la misma distribución
    
    Args:
        channel: Matriz de canal P(B|A)
    
    Returns:
        True si el canal es simétrico
    """
    if len(channel) != len(channel[0]):
        return False
    
    # Verificar filas (uniformidad)
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


# ============================================================================
# CAPACIDAD DEL CANAL
# ============================================================================

def calculateCapacidadNoRuido(channel: List[List[float]]) -> float:
    """
    Calcula la capacidad de un canal sin ruido.
    
    Fundamento teórico:
    Para un canal sin ruido: C = log₂(|A|)
    
    Args:
        channel: Matriz de canal
    
    Returns:
        Capacidad en bits
    """
    return math.log2(len(channel))


def calculateCapacidadDeterminante(channel: List[List[float]]) -> float:
    """
    Calcula la capacidad de un canal determinístico.
    
    Fundamento teórico:
    Para un canal determinístico: C = log₂(|B|)
    
    Args:
        channel: Matriz de canal
    
    Returns:
        Capacidad en bits
    """
    return math.log2(len(channel[0]))


def calculateCapacidadUniforme(channel: List[List[float]]) -> float:
    """
    Calcula la capacidad de un canal uniforme.
    
    Fundamento teórico:
    Para un canal uniforme:
    C = log₂(|B|) - H(fila)
    
    donde H(fila) es la entropía de cualquier fila (son todas iguales
    como permutaciones).
    
    Args:
        channel: Matriz de canal
    
    Returns:
        Capacidad en bits
    """
    log2NroSalida = math.log2(len(channel[0]))
    amount = 0.0
    
    for pij in channel[0]:
        if pij != 0:
            amount += pij * math.log2(1 / pij)
    
    return log2NroSalida - amount


def calcularCapacidad(channel: List[List[float]]) -> float:
    """
    Calcula la capacidad de un canal según sus propiedades.
    
    Fundamento teórico:
    C = max_{P(A)} I(A;B)
    
    Para canales especiales, hay fórmulas cerradas.
    
    Args:
        channel: Matriz de canal
    
    Returns:
        Capacidad en bits
    
    Raises:
        NotImplementedError: Si el canal no es especial
    """
    if isCanalNoRuido(channel):
        return calculateCapacidadNoRuido(channel)
    
    if isCanalDeterminante(channel):
        return calculateCapacidadDeterminante(channel)
    
    if isCanalUniforme(channel):
        return calculateCapacidadUniforme(channel)
    
    raise NotImplementedError("Canal general: use optimización numérica")


def calculateCapacidadBinario(channel: List[List[float]], step: float = 0.0001) -> Tuple[float, float]:
    """
    Calcula la capacidad de un canal binario por búsqueda exhaustiva.
    
    Fundamento teórico:
    Para canal binario, C = max_{p} I(A;B) donde p es P(a₁).
    Se busca numéricamente el máximo evaluando I(A;B) para distintos p.
    
    Args:
        channel: Matriz 2×m del canal
        step: Paso de búsqueda
    
    Returns:
        Tupla (p_óptimo, C) donde p es P(a₁) que maximiza I(A;B)
    """
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


# ============================================================================
# CANALES EN SERIE (COMPOSICIÓN)
# ============================================================================

def generarComposedChannel(channelA: List[List[float]], channelB: List[List[float]]) -> List[List[float]]:
    """
    Genera el canal compuesto de dos canales en serie.
    
    Fundamento teórico:
    Si A→B con P(B|A) y B→C con P(C|B), entonces:
    P(C|A) = P(B|A) × P(C|B) (multiplicación matricial)
    
    Propiedad: I(A;C) ≤ min(I(A;B), I(B;C))
    
    Args:
        channelA: Primer canal A→B
        channelB: Segundo canal B→C
    
    Returns:
        Canal compuesto A→C
    """
    return getMatrixProduct(channelA, channelB)


# ============================================================================
# REDUCCIÓN DE CANALES
# ============================================================================

def isReduccionSuficiente(channel: List[List[float]], col1: int, col2: int) -> bool:
    """
    Verifica si dos columnas pueden combinarse.
    
    Fundamento teórico:
    Dos columnas j₁ y j₂ son combinables si existe k tal que:
    ∀i: P(bⱼ₁|aᵢ) = k · P(bⱼ₂|aᵢ)
    
    La combinación no altera I(A;B).
    
    Args:
        channel: Matriz de canal
        col1: Índice de primera columna
        col2: Índice de segunda columna
    
    Returns:
        True si las columnas son combinables
    """
    const = 0
    tolerance = 1e-5
    isCalculated = False
    
    # Calcular la constante k
    i = 0
    while i < len(channel) and not isCalculated:
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
    
    # Verificar que k es constante para todas las filas
    for j in range(len(channel)):
        if abs(channel[j][col1] - const * channel[j][col2]) > tolerance:
            return False
    
    return True


def combinateCols(channel: List[List[float]], col1: int, col2: int) -> List[List[float]]:
    """
    Combina dos columnas de un canal.
    
    Args:
        channel: Matriz de canal
        col1: Primera columna
        col2: Segunda columna (se elimina)
    
    Returns:
        Canal con columnas combinadas
    """
    for i in range(len(channel)):
        channel[i][col1] += channel[i][col2]
        del channel[i][col2]
    
    return channel


def getCanalDeterminante(channel: List[List[float]], col1: int, col2: int) -> List[List[float]]:
    """
    Obtiene el canal determinístico para combinar dos columnas.
    
    Args:
        channel: Matriz de canal
        col1: Primera columna
        col2: Segunda columna
    
    Returns:
        Matriz determinística
    """
    result = getMatrixZeros(len(channel[0]), len(channel[0]) - 1)
    j = 0
    for i in range(len(channel[0])):
        if i != col2:
            result[i][j] = 1
            j += 1
    
    result[col2][col1] = 1
    return result


def getReducedChannel(channel: List[List[float]]) -> List[List[float]]:
    """
    Reduce un canal combinando todas las columnas combinables.
    
    Fundamento teórico:
    El canal reducido es el canal con el menor número de símbolos de salida
    que preserva I(A;B).
    
    Args:
        channel: Matriz de canal
    
    Returns:
        Canal reducido
    """
    isReductable = True
    
    while isReductable:
        col1 = -1
        col2 = -1
        
        # Buscar dos columnas combinables
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


# ============================================================================
# PROBABILIDAD DE ERROR
# ============================================================================

def probabilidadError(channel: List[List[float]], P: List[float]) -> float:
    """
    Calcula la probabilidad de error bajo la regla ML (Maximum Likelihood).
    
    Fundamento teórico:
    Regla ML: Para cada salida bⱼ, elegir la entrada aᵢ con mayor P(bⱼ|aᵢ).
    La probabilidad de error es la suma de las probabilidades de asignaciones
    incorrectas.
    
    Pₑ = Σᵢ P(aᵢ) · (1 - max_j P(bⱼ|aᵢ))
    
    Args:
        channel: Matriz de canal cuadrada n×n
        P: Probabilidades a priori
    
    Returns:
        Probabilidad de error
    """
    if not channel or len(channel) != len(channel[0]):
        raise ValueError("La matriz del canal debe ser cuadrada")
    n = len(channel)
    
    if len(P) != n:
        raise ValueError("P debe tener tamaño igual al número de filas")
    
    # Asignación ML con columnas únicas
    columnas_tomadas = set()
    asignacion = [-1] * n
    
    for i in range(n):
        # Ordenar columnas por valor descendente en la fila i
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
    
    # Calcular probabilidad de error
    error = 0.0
    for i, j in enumerate(asignacion):
        fila_sum = sum(channel[i][k] for k in range(n))
        correcto = channel[i][j]
        error += P[i] * (fila_sum - correcto)
    
    return error


# ============================================================================
# FUNCIÓN PRINCIPAL - DEMOSTRACIÓN
# ============================================================================

def main():
    """
    Función principal que demuestra propiedades y capacidad de canales.
    
    Solicita UNA entrada (selección de canal) y ejecuta:
    1. Análisis de propiedades del canal
    2. Cálculo de capacidad
    3. Cálculo de información mutua con diferentes distribuciones
    4. Composición de canales
    5. Reducción de canales
    6. Probabilidad de error
    """
    print("=" * 80)
    print("UNIDAD 6: PROPIEDADES Y CAPACIDAD DE CANALES")
    print("=" * 80)
    
    # Definir canales de ejemplo
    canales = {
        "1": {
            "nombre": "Canal Determinístico",
            "matriz": [
                [0.0, 0.0, 1.0, 0.0],
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 1.0]
            ],
            "descripcion": "Cada entrada produce una única salida"
        },
        "2": {
            "nombre": "Canal Sin Ruido",
            "matriz": [
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0],
                [0.0, 1.0, 0.0],
                [1.0, 0.0, 0.0]
            ],
            "descripcion": "Cada salida proviene de una única entrada"
        },
        "3": {
            "nombre": "Canal Simétrico",
            "matriz": [
                [0.3, 0.5, 0.2],
                [0.2, 0.3, 0.5],
                [0.5, 0.2, 0.3]
            ],
            "descripcion": "Filas y columnas son permutaciones"
        },
        "4": {
            "nombre": "Canal Binario Simétrico (BSC)",
            "matriz": [
                [0.9, 0.1],
                [0.1, 0.9]
            ],
            "descripcion": "Canal binario con probabilidad de error 0.1"
        },
        "5": {
            "nombre": "Canal con Ruido y Pérdida",
            "matriz": [
                [0.6, 0.3, 0.1],
                [0.1, 0.8, 0.1],
                [0.3, 0.3, 0.4]
            ],
            "descripcion": "Canal general con ruido y pérdida"
        }
    }
    
    # Mostrar opciones
    print("\n📋 Canales disponibles:")
    for key, info in canales.items():
        print(f"   {key}. {info['nombre']}")
        print(f"      {info['descripcion']}")
    
    # Entrada del usuario
    print("\n📝 Seleccione un canal para analizar (1-5):")
    seleccion = input("   > ")
    
    if seleccion not in canales:
        print("⚠️  Selección inválida. Usando Canal Binario Simétrico.")
        seleccion = "4"
    
    canal_info = canales[seleccion]
    channel = [row[:] for row in canal_info["matriz"]]  # Copia profunda
    
    print(f"\n✓ Canal seleccionado: {canal_info['nombre']}")
    
    # ========================================================================
    # 1. VISUALIZACIÓN DEL CANAL
    # ========================================================================
    print("\n" + "=" * 80)
    print("1. MATRIZ DEL CANAL")
    print("=" * 80)
    
    print(f"\n{canal_info['descripcion']}")
    print(f"\nMatriz P(B|A) [{len(channel)}×{len(channel[0])}]:")
    printMatrix(channel)
    
    # ========================================================================
    # 2. PROPIEDADES DEL CANAL
    # ========================================================================
    print("\n" + "=" * 80)
    print("2. PROPIEDADES DEL CANAL")
    print("=" * 80)
    
    es_noruido = isCanalNoRuido(channel)
    es_determinante = isCanalDeterminante(channel)
    es_uniforme = isCanalUniforme(channel)
    es_simetrico = isCanalSimetrico(channel)
    
    print(f"\n{'Propiedad':<25} {'Estado':<10}")
    print("-" * 35)
    print(f"{'Sin ruido':<25} {'✓ SÍ' if es_noruido else '✗ NO':<10}")
    print(f"{'Determinístico':<25} {'✓ SÍ' if es_determinante else '✗ NO':<10}")
    print(f"{'Uniforme':<25} {'✓ SÍ' if es_uniforme else '✗ NO':<10}")
    print(f"{'Simétrico':<25} {'✓ SÍ' if es_simetrico else '✗ NO':<10}")
    
    # ========================================================================
    # 3. CAPACIDAD DEL CANAL
    # ========================================================================
    print("\n" + "=" * 80)
    print("3. CAPACIDAD DEL CANAL")
    print("=" * 80)
    
    try:
        capacidad = calcularCapacidad(channel)
        print(f"\n📊 Capacidad C = {capacidad:.4f} bits")
        
        if es_noruido:
            print(f"   Fórmula: C = log₂(|A|) = log₂({len(channel)}) = {capacidad:.4f}")
        elif es_determinante:
            print(f"   Fórmula: C = log₂(|B|) = log₂({len(channel[0])}) = {capacidad:.4f}")
        elif es_uniforme:
            print(f"   Fórmula: C = log₂(|B|) - H(fila)")
            print(f"   C = log₂({len(channel[0])}) - H = {capacidad:.4f}")
        
    except NotImplementedError:
        print("\n📊 Canal general: calculando capacidad numéricamente...")
        
        if len(channel) == 2:
            # Canal binario: búsqueda exhaustiva
            p_opt, capacidad = calculateCapacidadBinario(channel)
            print(f"   Capacidad C = {capacidad:.4f} bits")
            print(f"   Distribución óptima: P(a₁) = {p_opt:.4f}, P(a₂) = {1-p_opt:.4f}")
        else:
            print("   ⚠️ Optimización numérica no implementada para canales no binarios")
            capacidad = None
    
    # ========================================================================
    # 4. INFORMACIÓN MUTUA CON DIFERENTES DISTRIBUCIONES
    # ========================================================================
    print("\n" + "=" * 80)
    print("4. INFORMACIÓN MUTUA CON DIFERENTES DISTRIBUCIONES")
    print("=" * 80)
    
    # Probar con distribución uniforme
    P_uniforme = [1/len(channel)] * len(channel)
    I_uniforme = informacionMutuaABSimple(P_uniforme, channel)
    
    print(f"\n📊 Con distribución uniforme:")
    print(f"   P(A) = {P_uniforme}")
    print(f"   I(A;B) = {I_uniforme:.4f} bits")
    
    # Probar con distribución sesgada
    if len(channel) >= 2:
        P_sesgada = [0.8] + [0.2/(len(channel)-1)] * (len(channel)-1)
        I_sesgada = informacionMutuaABSimple(P_sesgada, channel)
        
        print(f"\n📊 Con distribución sesgada:")
        print(f"   P(A) = {[round(p, 3) for p in P_sesgada]}")
        print(f"   I(A;B) = {I_sesgada:.4f} bits")
    
    # Comparar con capacidad
    if capacidad is not None:
        print(f"\n💡 Comparación:")
        print(f"   I(uniforme) = {I_uniforme:.4f} bits")
        if len(channel) >= 2:
            print(f"   I(sesgada) = {I_sesgada:.4f} bits")
        print(f"   Capacidad C = {capacidad:.4f} bits")
        print(f"   C - I(uniforme) = {capacidad - I_uniforme:.4f} bits")
    
    # ========================================================================
    # 5. RUIDO Y PÉRDIDA
    # ========================================================================
    print("\n" + "=" * 80)
    print("5. RUIDO Y PÉRDIDA DEL CANAL")
    print("=" * 80)
    
    ruido = calculateRuido(P_uniforme, channel)
    perdida = calculatePerdida(P_uniforme, channel)
    
    print(f"\n📊 Con distribución uniforme:")
    print(f"   H(A|B) = {ruido:.4f} bits (equivocación/ruido)")
    print(f"   H(B|A) = {perdida:.4f} bits (pérdida)")
    
    print(f"\n💡 Interpretación:")
    if ruido < 0.01:
        print(f"   - Canal prácticamente sin ruido")
    else:
        print(f"   - Ruido: {ruido:.4f} bits de incertidumbre sobre entrada")
    
    if perdida < 0.01:
        print(f"   - Canal prácticamente determinístico")
    else:
        print(f"   - Pérdida: {perdida:.4f} bits de incertidumbre sobre salida")
    
    # ========================================================================
    # 6. COMPOSICIÓN DE CANALES (si hay espacio)
    # ========================================================================
    if len(channel) <= 3 and len(channel[0]) <= 3:
        print("\n" + "=" * 80)
        print("6. COMPOSICIÓN DE CANALES EN SERIE")
        print("=" * 80)
        
        # Crear un segundo canal simple
        channel2 = [
            [0.9, 0.1, 0.0],
            [0.0, 0.9, 0.1],
            [0.1, 0.0, 0.9]
        ][:len(channel[0])]
        
        if len(channel[0]) == len(channel2):
            print("\nSegundo canal B→C:")
            printMatrix(channel2)
            
            channel_comp = generarComposedChannel(channel, channel2)
            print("\nCanal compuesto A→C = A→B × B→C:")
            printMatrix(channel_comp)
            
            I_AB = informacionMutuaABSimple(P_uniforme[:len(channel)], channel)
            I_BC = informacionMutuaABSimple(P_uniforme[:len(channel2)], channel2)
            I_AC = informacionMutuaABSimple(P_uniforme[:len(channel)], channel_comp)
            
            print(f"\n📊 Información mutua:")
            print(f"   I(A;B) = {I_AB:.4f} bits")
            print(f"   I(B;C) = {I_BC:.4f} bits")
            print(f"   I(A;C) = {I_AC:.4f} bits")
            print(f"\n✓ Verificación: I(A;C) ≤ min(I(A;B), I(B;C))")
            print(f"   {I_AC:.4f} ≤ {min(I_AB, I_BC):.4f}: {I_AC <= min(I_AB, I_BC)}")
    
    # ========================================================================
    # 7. PROBABILIDAD DE ERROR (si es cuadrado)
    # ========================================================================
    if len(channel) == len(channel[0]):
        print("\n" + "=" * 80)
        print("7. PROBABILIDAD DE ERROR (REGLA ML)")
        print("=" * 80)
        
        Pe = probabilidadError(channel, P_uniforme)
        print(f"\n📊 Con distribución uniforme:")
        print(f"   Probabilidad de error ML: {Pe:.4f}")
        print(f"   Probabilidad de acierto: {1-Pe:.4f}")
        
        if len(channel) >= 2:
            Pe_sesgada = probabilidadError(channel, P_sesgada)
            print(f"\n📊 Con distribución sesgada:")
            print(f"   Probabilidad de error ML: {Pe_sesgada:.4f}")
            print(f"   Diferencia con uniforme: {abs(Pe - Pe_sesgada):.4f}")
    
    # ========================================================================
    # RESUMEN
    # ========================================================================
    print("\n" + "=" * 80)
    print("RESUMEN DEL CANAL")
    print("=" * 80)
    
    print(f"""
📊 Canal: {canal_info['nombre']}
   - Dimensión: {len(channel)}×{len(channel[0])}
   
🔍 Propiedades:
   - Sin ruido: {'Sí' if es_noruido else 'No'}
   - Determinístico: {'Sí' if es_determinante else 'No'}
   - Uniforme: {'Sí' if es_uniforme else 'No'}
   - Simétrico: {'Sí' if es_simetrico else 'No'}
   
💬 Métricas (distribución uniforme):
   - I(A;B) = {I_uniforme:.4f} bits
   - H(A|B) = {ruido:.4f} bits (ruido)
   - H(B|A) = {perdida:.4f} bits (pérdida)
""")
    
    if capacidad is not None:
        print(f"   - Capacidad C = {capacidad:.4f} bits")
    
    print("\n" + "=" * 80)
    print("Demostración completada exitosamente")
    print("=" * 80)


if __name__ == "__main__":
    main()
