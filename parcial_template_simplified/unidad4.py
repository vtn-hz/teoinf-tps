#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UNIDAD 4: Códigos y Codificación - Versión Simplificada
Analiza un string fijo y muestra códigos Huffman y Shannon-Fano con métricas.
Sin input(), ejecución lineal con prints claros.
"""

import sys
import os
# Agregar el directorio raíz al path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.fuente_nula.alfabetoS import buildS
from utils.fuente_nula.calculateH import calculateH
from utils.codigos.algorithm.huffman import huffman
from utils.codigos.algorithm.shannonfano import shannonfano
from utils.codigos.metadataCodigo import getLengthMedCodigo
from utils.codigos.metricas.rendRend import rendimientoCodigo, redundanciaCodigo

# ============================================================================
# VARIABLES EDITABLES - Modificar aquí para cambiar el análisis
# ============================================================================

# String a analizar
MENSAJE = "ABRACADABRA"

# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

def main():
    print("=" * 70)
    print("UNIDAD 4: ANÁLISIS DE CÓDIGOS")
    print("=" * 70)
    
    # 1. Analizar el mensaje
    print(f"\n1. MENSAJE A ANALIZAR")
    print(f"   Mensaje: '{MENSAJE}'")
    print(f"   Longitud: {len(MENSAJE)} símbolos")
    
    # 2. Construir distribución de probabilidades
    S = buildS(MENSAJE)
    simbolos = list(S.keys())
    probabilidades = list(S.values())
    
    print(f"\n2. ALFABETO Y PROBABILIDADES")
    print(f"   Alfabeto: {simbolos}")
    for simbolo, prob in S.items():
        ocurrencias = int(prob * len(MENSAJE))
        print(f"   P({simbolo}) = {prob:.4f} ({ocurrencias} ocurrencias)")
    
    # 3. Calcular entropía
    H = calculateH(probabilidades)
    print(f"\n3. ENTROPÍA")
    print(f"   H(X) = {H:.4f} bits/símbolo")
    
    # 4. Generar códigos
    print(f"\n4. CÓDIGOS GENERADOS")
    C_huffman = huffman(probabilidades)
    C_shannon = shannonfano(probabilidades)
    
    print(f"\n   {'Símbolo':<10} {'P(X)':<12} {'Huffman':<15} {'Shannon-Fano':<15}")
    print(f"   {'-'*52}")
    for simbolo, prob, huff, shan in zip(simbolos, probabilidades, C_huffman, C_shannon):
        print(f"   {simbolo:<10} {prob:<12.4f} {huff:<15} {shan:<15}")
    
    # 5. Calcular métricas
    print(f"\n5. MÉTRICAS DE CÓDIGOS")
    
    L_huffman = getLengthMedCodigo(C_huffman, probabilidades)
    rend_huffman = rendimientoCodigo(C_huffman, probabilidades)
    red_huffman = redundanciaCodigo(C_huffman, probabilidades)
    
    L_shannon = getLengthMedCodigo(C_shannon, probabilidades)
    rend_shannon = rendimientoCodigo(C_shannon, probabilidades)
    red_shannon = redundanciaCodigo(C_shannon, probabilidades)
    
    print(f"\n   {'Código':<20} {'Long. Media':<15} {'Rendimiento':<15} {'Redundancia':<15}")
    print(f"   {'-'*65}")
    print(f"   {'Huffman':<20} {L_huffman:<15.4f} {rend_huffman:<15.4f} {red_huffman:<15.4f}")
    print(f"   {'Shannon-Fano':<20} {L_shannon:<15.4f} {rend_shannon:<15.4f} {red_shannon:<15.4f}")
    
    # 6. Relaciones matemáticas
    print(f"\n6. RELACIONES MATEMÁTICAS")
    print(f"   Teorema de Shannon: H(X) ≤ L < H(X) + 1")
    print(f"   ")
    print(f"   Huffman:")
    print(f"     {H:.4f} ≤ {L_huffman:.4f} < {H + 1:.4f}")
    cumple_huff = H <= L_huffman < H + 1
    print(f"     Cumple: {'✓ SÍ' if cumple_huff else '✗ NO'}")
    print(f"   ")
    print(f"   Shannon-Fano:")
    print(f"     {H:.4f} ≤ {L_shannon:.4f} < {H + 1:.4f}")
    cumple_shan = H <= L_shannon < H + 1
    print(f"     Cumple: {'✓ SÍ' if cumple_shan else '✗ NO'}")
    
    print(f"\n   Rendimiento η = H(X) / L")
    print(f"     Huffman:      η = {H:.4f} / {L_huffman:.4f} = {rend_huffman:.4f}")
    print(f"     Shannon-Fano: η = {H:.4f} / {L_shannon:.4f} = {rend_shannon:.4f}")
    
    print(f"\n   Redundancia R = 1 - η")
    print(f"     Huffman:      R = 1 - {rend_huffman:.4f} = {red_huffman:.4f}")
    print(f"     Shannon-Fano: R = 1 - {rend_shannon:.4f} = {red_shannon:.4f}")
    
    print(f"\n" + "=" * 70)
    print("FIN DEL ANÁLISIS")
    print("=" * 70)


if __name__ == "__main__":
    main()
