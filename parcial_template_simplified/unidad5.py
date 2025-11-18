#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UNIDAD 5: Canales de Comunicación - Versión Simplificada
Analiza un canal con matriz y probabilidades a priori definidas.
Sin input(), ejecución lineal con prints claros.
"""

import sys
import os
# Agregar el directorio raíz al path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.canales.priori.entropy import calculateHPriori
from utils.canales.posteriori.entropy import calculateHPosteriori, calculateHPosterioriTotal
from utils.canales.posteriori.probs import getProbsOutSymbols, getPosterioriMatrix, getMatrixSimultaneusEvent
from utils.canales.entropy_media import calculateRuido, calculatePerdida
from utils.canales.entropia_canal import calculateHCanal
from utils.canales.informacion_mutua import informacionMutuaABSimple
from utils.matrix import printMatrix

# ============================================================================
# VARIABLES EDITABLES - Modificar aquí para cambiar el análisis
# ============================================================================

# Matriz de canal P(B|A) - Filas: entrada, Columnas: salida
# Cada fila debe sumar 1
MATRIZ_CANAL = [
    [0.6, 0.3, 0.1],
    [0.1, 0.8, 0.1],
    [0.2, 0.2, 0.6]
]

# Probabilidades a priori P(A) - Deben sumar 1
# Longitud debe coincidir con número de filas de MATRIZ_CANAL
PROB_PRIORI = [0.5, 0.3, 0.2]

# Etiquetas (opcionales, para mejor visualización)
SIMBOLOS_ENTRADA = ['a1', 'a2', 'a3']
SIMBOLOS_SALIDA = ['b1', 'b2', 'b3']

# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

def main():
    print("=" * 70)
    print("UNIDAD 5: ANÁLISIS DE CANAL")
    print("=" * 70)
    
    # 1. Mostrar matriz de canal
    print(f"\n1. MATRIZ DE CANAL P(B|A)")
    print(f"   (Filas: símbolos de entrada, Columnas: símbolos de salida)")
    print()
    # Encabezado
    print(f"        ", end="")
    for s in SIMBOLOS_SALIDA:
        print(f"{s:>10}", end="")
    print()
    # Filas
    for i, fila in enumerate(MATRIZ_CANAL):
        print(f"   {SIMBOLOS_ENTRADA[i]:<4} ", end="")
        for val in fila:
            print(f"{val:>10.4f}", end="")
        print()
    
    # 2. Mostrar probabilidades a priori
    print(f"\n2. PROBABILIDADES A PRIORI P(A)")
    for i, (simbolo, prob) in enumerate(zip(SIMBOLOS_ENTRADA, PROB_PRIORI)):
        print(f"   P({simbolo}) = {prob:.4f}")
    
    # 3. Calcular probabilidades de salida
    print(f"\n3. PROBABILIDADES DE SALIDA P(B)")
    prob_salida = getProbsOutSymbols(PROB_PRIORI, MATRIZ_CANAL)
    for simbolo, prob in zip(SIMBOLOS_SALIDA, prob_salida):
        print(f"   P({simbolo}) = {prob:.4f}")
    print(f"\n   Fórmula: P(bj) = Σi P(bj|ai) * P(ai)")
    
    # 4. Calcular matriz a posteriori
    print(f"\n4. MATRIZ A POSTERIORI P(A|B)")
    print(f"   (Probabilidades de entrada dado que se observó una salida)")
    print()
    matriz_posteriori = getPosterioriMatrix(PROB_PRIORI, MATRIZ_CANAL)
    # Encabezado
    print(f"        ", end="")
    for s in SIMBOLOS_SALIDA:
        print(f"{s:>10}", end="")
    print()
    # Filas
    for i, fila in enumerate(matriz_posteriori):
        print(f"   {SIMBOLOS_ENTRADA[i]:<4} ", end="")
        for val in fila:
            print(f"{val:>10.4f}", end="")
        print()
    print(f"\n   Fórmula (Teorema de Bayes): P(ai|bj) = P(bj|ai) * P(ai) / P(bj)")
    
    # 5. Calcular matriz conjunta
    print(f"\n5. MATRIZ CONJUNTA P(A,B)")
    print(f"   (Probabilidades de ocurrencia simultánea)")
    print()
    matriz_conjunta = getMatrixSimultaneusEvent(PROB_PRIORI, MATRIZ_CANAL)
    # Encabezado
    print(f"        ", end="")
    for s in SIMBOLOS_SALIDA:
        print(f"{s:>10}", end="")
    print()
    # Filas
    for i, fila in enumerate(matriz_conjunta):
        print(f"   {SIMBOLOS_ENTRADA[i]:<4} ", end="")
        for val in fila:
            print(f"{val:>10.4f}", end="")
        print()
    print(f"\n   Fórmula: P(ai, bj) = P(bj|ai) * P(ai)")
    suma_conjunta = sum(sum(fila) for fila in matriz_conjunta)
    print(f"   Verificación: Σ P(A,B) = {suma_conjunta:.4f} (debe ser 1.0)")
    
    # 6. Calcular entropías
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
    
    # Entropías condicionales por símbolo de salida
    H_A_given_bj = calculateHPosteriori(PROB_PRIORI, MATRIZ_CANAL)
    print(f"\n   Entropías condicionales H(A|B=bj):")
    for simbolo, h_val in zip(SIMBOLOS_SALIDA, H_A_given_bj):
        print(f"     H(A|{simbolo}) = {h_val:.4f} bits")
    
    # 7. Calcular información mutua
    print(f"\n7. INFORMACIÓN MUTUA")
    I_AB = informacionMutuaABSimple(PROB_PRIORI, MATRIZ_CANAL)
    print(f"   I(A;B) = {I_AB:.4f} bits")
    print(f"\n   Fórmula: I(A;B) = H(A) - H(A|B) = H(B) - H(B|A)")
    print(f"           I(A;B) = {H_A:.4f} - {H_A_given_B:.4f} = {I_AB:.4f}")
    print(f"           I(A;B) = {H_B:.4f} - {H_B_given_A:.4f} = {I_AB:.4f}")
    
    # 8. Relaciones matemáticas
    print(f"\n8. RELACIONES MATEMÁTICAS")
    
    # H(A,B) = H(A) + H(B|A)
    rel1_izq = H_AB
    rel1_der = H_A + H_B_given_A
    print(f"   H(A,B) = H(A) + H(B|A)")
    print(f"   {rel1_izq:.4f} = {H_A:.4f} + {H_B_given_A:.4f} = {rel1_der:.4f}")
    print(f"   Diferencia: {abs(rel1_izq - rel1_der):.6f}")
    
    # H(A,B) = H(B) + H(A|B)
    rel2_izq = H_AB
    rel2_der = H_B + H_A_given_B
    print(f"\n   H(A,B) = H(B) + H(A|B)")
    print(f"   {rel2_izq:.4f} = {H_B:.4f} + {H_A_given_B:.4f} = {rel2_der:.4f}")
    print(f"   Diferencia: {abs(rel2_izq - rel2_der):.6f}")
    
    # I(A;B) = H(A) - H(A|B)
    rel3_izq = I_AB
    rel3_der = H_A - H_A_given_B
    print(f"\n   I(A;B) = H(A) - H(A|B)")
    print(f"   {rel3_izq:.4f} = {H_A:.4f} - {H_A_given_B:.4f} = {rel3_der:.4f}")
    print(f"   Diferencia: {abs(rel3_izq - rel3_der):.6f}")
    
    # I(A;B) = H(B) - H(B|A)
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
