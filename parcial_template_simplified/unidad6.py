#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UNIDAD 6: Composición de Canales - Versión Simplificada
Analiza dos canales y su composición en serie.
Sin input(), ejecución lineal con prints claros.
"""

import sys
import os
# Agregar el directorio raíz al path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.canales.priori.entropy import calculateHPriori
from utils.canales.posteriori.probs import getProbsOutSymbols
from utils.canales.entropy_media import calculateRuido, calculatePerdida
from utils.canales.informacion_mutua import informacionMutuaABSimple
from utils.canales.metricas import calcularCapacidad
from utils.canales.canales_serie import generarComposedChannel
from utils.matrix import printMatrix

# ============================================================================
# VARIABLES EDITABLES - Modificar aquí para cambiar el análisis
# ============================================================================

# PRIMER CANAL: A → B
# Matriz P(B|A) - Cada fila debe sumar 1
CANAL_1 = [
    [0.9, 0.1, 0.0],
    [0.0, 0.9, 0.1],
    [0.1, 0.0, 0.9]
]

# Probabilidades a priori del primer canal P(A)
# Longitud debe coincidir con número de filas de CANAL_1
PROB_PRIORI_1 = [0.4, 0.35, 0.25]

# SEGUNDO CANAL: B → C
# Matriz P(C|B) - Cada fila debe sumar 1
# Número de filas debe coincidir con número de columnas de CANAL_1
CANAL_2 = [
    [0.8, 0.15, 0.05],
    [0.1, 0.8, 0.1],
    [0.05, 0.15, 0.8]
]

# Etiquetas (opcionales)
SIMBOLOS_A = ['a1', 'a2', 'a3']
SIMBOLOS_B = ['b1', 'b2', 'b3']
SIMBOLOS_C = ['c1', 'c2', 'c3']

# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

def analizar_canal(nombre, matriz, prob_priori, simbolos_entrada, simbolos_salida):
    """Analiza un canal y muestra sus métricas."""
    print(f"\n   {nombre}")
    print(f"   {'-' * len(nombre)}")
    
    # Calcular métricas básicas
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
    
    # Intentar calcular capacidad
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
    print("=" * 70)
    print("UNIDAD 6: COMPOSICIÓN DE CANALES")
    print("=" * 70)
    
    # 1. Mostrar primer canal
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
    
    # 2. Mostrar segundo canal
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
    
    # Calcular probabilidades a priori del segundo canal (salida del primero)
    prob_priori_2 = getProbsOutSymbols(PROB_PRIORI_1, CANAL_1)
    print(f"\n   Probabilidades a priori P(B) (salida del canal 1):")
    for simbolo, prob in zip(SIMBOLOS_B, prob_priori_2):
        print(f"     P({simbolo}) = {prob:.4f}")
    
    # 3. Métricas del primer canal
    print(f"\n3. MÉTRICAS DE LOS CANALES INDIVIDUALES")
    metricas_1 = analizar_canal(
        "Canal 1 (A→B)", 
        CANAL_1, 
        PROB_PRIORI_1, 
        SIMBOLOS_A, 
        SIMBOLOS_B
    )
    
    # 4. Métricas del segundo canal
    metricas_2 = analizar_canal(
        "Canal 2 (B→C)", 
        CANAL_2, 
        prob_priori_2, 
        SIMBOLOS_B, 
        SIMBOLOS_C
    )
    
    # 5. Canal compuesto
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
    
    # 6. Métricas del canal compuesto
    print(f"\n5. MÉTRICAS DEL CANAL COMPUESTO")
    metricas_comp = analizar_canal(
        "Canal Compuesto (A→C)", 
        canal_compuesto, 
        PROB_PRIORI_1, 
        SIMBOLOS_A, 
        SIMBOLOS_C
    )
    
    # 7. Relaciones matemáticas
    print(f"\n6. RELACIONES MATEMÁTICAS")
    print(f"\n   Propiedad fundamental de canales en serie:")
    print(f"   I(A;C) ≤ min(I(A;B), I(B;C))")
    print()
    print(f"   I(A;B) = {metricas_1['I_mutua']:.4f} bits")
    print(f"   I(B;C) = {metricas_2['I_mutua']:.4f} bits")
    print(f"   I(A;C) = {metricas_comp['I_mutua']:.4f} bits")
    print()
    min_mutua = min(metricas_1['I_mutua'], metricas_2['I_mutua'])
    cumple = metricas_comp['I_mutua'] <= min_mutua + 0.0001  # Tolerancia numérica
    print(f"   {metricas_comp['I_mutua']:.4f} ≤ {min_mutua:.4f}: {'✓ CUMPLE' if cumple else '✗ NO CUMPLE'}")
    
    print(f"\n   Comparación de ruido:")
    print(f"   Canal 1: H(A|B) = {metricas_1['ruido']:.4f} bits")
    print(f"   Canal 2: H(B|C) = {metricas_2['ruido']:.4f} bits")
    print(f"   Compuesto: H(A|C) = {metricas_comp['ruido']:.4f} bits")
    
    print(f"\n   Comparación de pérdida:")
    print(f"   Canal 1: H(B|A) = {metricas_1['perdida']:.4f} bits")
    print(f"   Canal 2: H(C|B) = {metricas_2['perdida']:.4f} bits")
    print(f"   Compuesto: H(C|A) = {metricas_comp['perdida']:.4f} bits")
    
    # Resumen
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
