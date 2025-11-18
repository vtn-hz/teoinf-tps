# GUIA.md - Guía de Funciones Consolidadas

## 📚 Resumen Conceptual: Teoría de la Información y la Comunicación

Este proyecto implementa los conceptos fundamentales de **codificación eficiente**, **modelado de canales ruidosos** y **límites teóricos de transmisión**, conforme a las Unidades 4, 5 y 6 del curso.

**IMPORTANTE**: Este archivo standalone contiene ÚNICAMENTE las funciones utilizadas en los trabajos prácticos tp4, tp5 y tp6.

---

## 📋 Índice

- [UNIDAD 4: Compresión y Errores](#unidad-4-compresión-y-errores)
- [UNIDAD 5: El Canal y sus Propiedades](#unidad-5-el-canal-y-sus-propiedades)
- [UNIDAD 6: Capacidad y Probabilidad de Error](#unidad-6-capacidad-y-probabilidad-de-error)
- [Catálogo de Funciones](#catálogo-de-funciones)

---

## UNIDAD 4: Compresión y Errores

### Fundamentos Teóricos de la Compresión

- **Primer Teorema de Shannon (Codificación sin Ruido)**: Establece la cota mínima para la longitud media (L) de un código instantáneo r-ario. La longitud media siempre debe ser mayor o igual a la entropía de la fuente: **L ≥ Hr(S)**

- **Cota de Compresión**: Para la extensión de orden n, la longitud media por símbolo Ln/n está acotada por:
  ```
  Hr(S) ≤ Ln/n < Hr(S) + 1/n
  ```

- **Rendimiento y Redundancia**:
  - Rendimiento o Eficiencia: **η = Hr(S) / L**
  - Redundancia: **1 - η**

### Algoritmos de Codificación

- **Códigos de Huffman**: Algoritmo óptimo que produce códigos instantáneos y compactos
- **Códigos de Shannon-Fano**: Procedimiento subóptimo, cumple L ≤ H(S) + 2
- **Run Length Coding (RLC)**: Codifica secuencias idénticas como pares (símbolo, repeticiones)

### Control de Errores

- **Distancia de Hamming (d)**: Número de bits que difieren entre dos palabras de código
  - Detección: hasta **d - 1** errores
  - Corrección: hasta **⌊(d-1)/2⌋** errores

- **Paridad Cruzada (VRC/LRC)**: Distancia de Hamming = 4, detecta hasta 3 errores y corrige 1 error simple

---

## UNIDAD 5: El Canal y sus Propiedades

### Caracterización del Canal

- **Canal de Información**: Definido por:
  - Alfabeto de entrada (A)
  - Alfabeto de salida (B)
  - Matriz de probabilidades condicionales P(bj|ai)

### Métricas de Entropía y Ruido

- **Entropía a Priori H(A)**: Incertidumbre promedio de la entrada
- **Entropía de la Salida H(B)**: Incertidumbre promedio de la salida
- **Entropía Afín H(A,B)**: Incertidumbre del evento simultáneo (ai,bj)
- **Equivocación (Ruido) H(A|B)**: Pérdida de información causada por el canal
- **Pérdida H(B|A)**: Incertidumbre de la salida conocida la entrada

### Información Mutua

- **Definición**: **I(A,B) = H(A) - H(A|B)**
- **Simetría**: **I(A,B) = I(B,A) = H(B) - H(B|A)**

---

## UNIDAD 6: Capacidad y Probabilidad de Error

### Capacidad del Canal (C)

- **Definición**: Máximo valor de Información Mutua
  ```
  C = max_P(ai) { I(A,B) }
  ```

- **Casos Especiales**:
  - Canal Sin Ruido: **C = log(nro de entradas)**
  - Canal Determinante: **C = log(nro de salidas)**
  - Canal Uniforme: Fórmula específica según distribución

### Canales Compuestos y Reducción

- **Canales en Serie**: Matriz compuesta = multiplicación de matrices individuales
- **Reducción Suficiente**: Permite combinar salidas sin perder información mutua

---

## Catálogo de Funciones

### Cómo Importar

```python
# Importar el módulo completo
from parcial2_template.total import utils_standalone as utils

# Usar funciones
entropia = utils.calculateH(probabilidades)

# O importar funciones específicas
from parcial2_template.total.utils_standalone import calculateH, huffman
```

---

## 🔗 Mapeo Teoría → Implementación

### UNIDAD 4: Compresión (Funciones usadas en tp4/tp5/tp6)

| Concepto Teórico | Función | Importar con |
|------------------|---------|--------------|
| **Entropía H(S)** | `calculateH(P)` | `from parcial2_template.total.utils_standalone import calculateH` |
| **Entropía base-r Hr(S)** | `calculateHr(pbs, r)` | `from parcial2_template.total.utils_standalone import calculateHr` |
| **Información I(pi)** | `calculateI(pi)` | `from parcial2_template.total.utils_standalone import calculateI` |
| **Información base-r Ir(pi)** | `calculateIr(p, r)` | `from parcial2_template.total.utils_standalone import calculateIr` |
| **Longitud Media L** | `getLengthMedCodigo(cods, pbs)` | `from parcial2_template.total.utils_standalone import getLengthMedCodigo` |
| **Alfabeto del código** | `getAlfabetoCodigo(cods)` | `from parcial2_template.total.utils_standalone import getAlfabetoCodigo` |
| **Longitudes** | `getLengthsCodigo(cods)` | `from parcial2_template.total.utils_standalone import getLengthsCodigo` |
| **Rendimiento η** | `rendimientoCodigo(C, P)` | `from parcial2_template.total.utils_standalone import rendimientoCodigo` |
| **Redundancia** | `redundanciaCodigo(C, P)` | `from parcial2_template.total.utils_standalone import redundanciaCodigo` |
| **Primer Teorema Shannon** | `teoremaShannon(C, P, n)` | `from parcial2_template.total.utils_standalone import teoremaShannon` |
| **Teorema Shannon (extendido)** | `teoremaShannonExtending(C, P, n)` | `from parcial2_template.total.utils_standalone import teoremaShannonExtending` |

### Algoritmos de Codificación (UNIDAD 4)

| Algoritmo | Función | Importar con |
|-----------|---------|--------------|
| **Huffman** | `huffman(P)` | `from parcial2_template.total.utils_standalone import huffman` |
| **Shannon-Fano** | `shannonfano(P)` | `from parcial2_template.total.utils_standalone import shannonfano` |
| **RLC (Run Length Coding)** | `rlc(message)` | `from parcial2_template.total.utils_standalone import rlc` |
| **Codificar con Huffman/SF** | `codificar(message, alf, C)` | `from parcial2_template.total.utils_standalone import codificar` |
| **Codificar con diccionario** | `codificar_dict(message, C)` | `from parcial2_template.total.utils_standalone import codificar_dict` |
| **Decodificar** | `decodificar(data, C, alf)` | `from parcial2_template.total.utils_standalone import decodificar` |
| **Decodificar con diccionario** | `decodificar_dict(data, C)` | `from parcial2_template.total.utils_standalone import decodificar_dict` |

### Control de Errores (UNIDAD 4)

| Concepto | Función | Importar con |
|----------|---------|--------------|
| **Distancia de Hamming d** | `hamming(C)` | `from parcial2_template.total.utils_standalone import hamming` |
| **Errores detectables (d-1)** | `erroresDetectables(C)` | `from parcial2_template.total.utils_standalone import erroresDetectables` |
| **Errores corregibles ⌊(d-1)/2⌋** | `erroresCorregibles(C)` | `from parcial2_template.total.utils_standalone import erroresCorregibles` |
| **Codificar multiparidad** | `encodeMultiparidad(message, par)` | `from parcial2_template.total.utils_standalone import encodeMultiparidad` |
| **Decodificar multiparidad** | `decodeMultiparidad(byte_array, par)` | `from parcial2_template.total.utils_standalone import decodeMultiparidad` |

### Extensiones de Fuentes (UNIDAD 4)

| Concepto | Función | Importar con |
|----------|---------|--------------|
| **Generar extensión orden n** | `generateExtensionsFromLL(alf, prob, n)` | `from parcial2_template.total.utils_standalone import generateExtensionsFromLL` |
| **Extensión desde dict** | `generateExtensionsFromD(S, n)` | `from parcial2_template.total.utils_standalone import generateExtensionsFromD` |
| **Extensión de probabilidades** | `generateExtensionsP(prob, n)` | `from parcial2_template.total.utils_standalone import generateExtensionsP` |
| **Construir fuente** | `buildS(source)` | `from parcial2_template.total.utils_standalone import buildS` |
| **Obtener ocurrencias** | `getSymbolOcurrences(phrase)` | `from parcial2_template.total.utils_standalone import getSymbolOcurrences` |

### Almacenamiento (UNIDAD 4)

| Concepto | Función | Importar con |
|----------|---------|--------------|
| **Guardar comprimido** | `saveComprimido(bits, filename, path)` | `from parcial2_template.total.utils_standalone import saveComprimido` |
| **Recuperar comprimido** | `recoverComprimido(filename, path)` | `from parcial2_template.total.utils_standalone import recoverComprimido` |
| **Tasa de compresión** | `tasaCompresion(message, compressed)` | `from parcial2_template.total.utils_standalone import tasaCompresion` |

### UNIDAD 5: Canales - Probabilidades

| Concepto | Función | Importar con |
|----------|---------|--------------|
| **P(ai) - Prob. a priori** | `getProbabilidadPriori(message)` | `from parcial2_template.total.utils_standalone import getProbabilidadPriori` |
| **P(B\|A) - Matriz del canal** | `getPrioriMatrixFull(fnt, cds, _input, _output)` | `from parcial2_template.total.utils_standalone import getPrioriMatrixFull` |
| **P(bj) - Prob. de salida** | `getProbsOutSymbols(Pinitial, channel)` | `from parcial2_template.total.utils_standalone import getProbsOutSymbols` |
| **P(A\|B) - Prob. a posteriori** | `getPosterioriMatrix(Pinitial, channel)` | `from parcial2_template.total.utils_standalone import getPosterioriMatrix` |
| **P(ai, bj) - Evento simultáneo** | `getMatrixSimultaneusEvent(Pinitial, channel)` | `from parcial2_template.total.utils_standalone import getMatrixSimultaneusEvent` |

### UNIDAD 5: Canales - Entropías

| Concepto | Función | Importar con |
|----------|---------|--------------|
| **H(A) - Entropía a priori** | `calculateHPriori(Pa)` | `from parcial2_template.total.utils_standalone import calculateHPriori` |
| **H(A\|bj) - Entropía a posteriori** | `calculateHPosteriori(Pa, channel)` | `from parcial2_template.total.utils_standalone import calculateHPosteriori` |
| **H(B) - Entropía de salida** | `calculateHPosterioriTotal(Pa, channel)` | `from parcial2_template.total.utils_standalone import calculateHPosterioriTotal` |
| **H(A\|B) - Equivocación/Ruido** | `calculateRuido(Pa, channel)` | `from parcial2_template.total.utils_standalone import calculateRuido` |
| **H(B\|A) - Pérdida** | `calculatePerdida(Pa, channel)` | `from parcial2_template.total.utils_standalone import calculatePerdida` |
| **H(A,B) - Entropía afín** | `calculateHCanal(Pa, channel)` | `from parcial2_template.total.utils_standalone import calculateHCanal` |

### UNIDAD 5: Información Mutua

| Concepto | Función | Importar con |
|----------|---------|--------------|
| **I(A,B) fórmula simple** | `informacionMutuaABSimple(Pa, channel)` | `from parcial2_template.total.utils_standalone import informacionMutuaABSimple` |
| **I(B,A) fórmula simple** | `informacionMutuaBASimple(Pa, channel)` | `from parcial2_template.total.utils_standalone import informacionMutuaBASimple` |

### UNIDAD 5: Propiedades de Canales

| Propiedad | Función | Importar con |
|-----------|---------|--------------|
| **Canal sin ruido** | `isCanalNoRuido(channel)` | `from parcial2_template.total.utils_standalone import isCanalNoRuido` |
| **Canal determinante** | `isCanalDeterminante(channel)` | `from parcial2_template.total.utils_standalone import isCanalDeterminante` |

### UNIDAD 6: Capacidad del Canal

| Concepto | Función | Importar con |
|----------|---------|--------------|
| **C (general)** | `calcularCapacidad(channel)` | `from parcial2_template.total.utils_standalone import calcularCapacidad` |

### UNIDAD 6: Canales Compuestos

| Concepto | Función | Importar con |
|----------|---------|--------------|
| **Canales en serie** | `generarComposedChannel(channelA, channelB)` | `from parcial2_template.total.utils_standalone import generarComposedChannel` |
| **Reducción suficiente** | `isReduccionSuficiente(channel, col1, col2)` | `from parcial2_template.total.utils_standalone import isReduccionSuficiente` |
| **Obtener canal reducido** | `getReducedChannel(channel, squareLimit)` | `from parcial2_template.total.utils_standalone import getReducedChannel` |
| **Combinar columnas** | `combinateCols(channel, col1, col2)` | `from parcial2_template.total.utils_standalone import combinateCols` |
| **Canal determinante** | `getCanalDeterminante(channel, col1, col2)` | `from parcial2_template.total.utils_standalone import getCanalDeterminante` |

### Utilidades de Matrices

| Función | Importar con |
|---------|--------------|
| `printMatrix(matrix)` | `from parcial2_template.total.utils_standalone import printMatrix` |
| `printMatrixVerbose(matrix, row_labels, col_labels)` | `from parcial2_template.total.utils_standalone import printMatrixVerbose` |

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Calcular Entropía y Rendimiento (UNIDAD 4)

```python
from parcial2_template.total.utils_standalone import calculateH, huffman, rendimientoCodigo

# Probabilidades de la fuente
P = [0.5, 0.3, 0.2]

# Calcular entropía
H = calculateH(P)
print(f"Entropía: {H:.4f} bits")

# Generar código de Huffman
C = huffman(P)
print(f"Código Huffman: {C}")

# Calcular rendimiento
eta = rendimientoCodigo(C, P)
print(f"Rendimiento: {eta*100:.2f}%")
```

### Ejemplo 2: Análisis de Canal (UNIDAD 5)

```python
from parcial2_template.total.utils_standalone import (
    calculateRuido, calculatePerdida, informacionMutuaABSimple
)

# Canal binario simétrico con p=0.1
canal = [
    [0.9, 0.1],
    [0.1, 0.9]
]

# Probabilidades a priori uniformes
Pa = [0.5, 0.5]

# Métricas del canal
ruido = calculateRuido(Pa, canal)
perdida = calculatePerdida(Pa, canal)
info_mutua = informacionMutuaABSimple(Pa, canal)

print(f"Ruido H(A|B): {ruido:.4f}")
print(f"Pérdida H(B|A): {perdida:.4f}")
print(f"I(A,B): {info_mutua:.4f}")
```

### Ejemplo 3: Control de Errores (UNIDAD 4)

```python
from parcial2_template.total.utils_standalone import (
    hamming, erroresDetectables, erroresCorregibles
)

# Código de ejemplo
codigo = ['000', '011', '101', '110']

# Calcular distancia de Hamming
d = hamming(codigo)
print(f"Distancia de Hamming: {d}")

# Capacidades
detectables = erroresDetectables(codigo)
corregibles = erroresCorregibles(codigo)

print(f"Errores detectables: {detectables}")
print(f"Errores corregibles: {corregibles}")
```

---

## 📝 Notas Importantes

1. **Solo funciones usadas**: Este standalone contiene ÚNICAMENTE las funciones utilizadas en tp4, tp5 y tp6

2. **Sin dependencias internas**: El archivo es completamente standalone

3. **Imports necesarios**: Solo usa librerías estándar de Python: `math`, `random`, `os`

4. **Compatibilidad**: Compatible con Python 3.6+

---

## 🔍 Lista Completa de Funciones Incluidas

Las siguientes funciones están disponibles en utils_standalone.py:

**Compresión y Códigos:**
- `calculateH`, `calculateI`, `calculateHr`, `calculateIr`
- `huffman`, `shannonfano`, `rlc`
- `getAlfabetoCodigo`, `getLengthsCodigo`, `getLengthMedCodigo`
- `rendimientoCodigo`, `redundanciaCodigo`
- `teoremaShannon`, `teoremaShannonExtending`
- `codificar`, `decodificar`, `codificar_dict`, `decodificar_dict`
- `saveComprimido`, `recoverComprimido`, `tasaCompresion`

**Errores:**
- `hamming`, `erroresDetectables`, `erroresCorregibles`
- `encodeMultiparidad`, `decodeMultiparidad`

**Extensiones:**
- `generateExtensionsFromLL`, `generateExtensionsFromD`, `generateExtensionsP`
- `buildS`, `getSymbolOcurrences`

**Canales:**
- `getProbabilidadPriori`, `getPrioriMatrixFull`
- `getProbsOutSymbols`, `getPosterioriMatrix`, `getMatrixSimultaneusEvent`
- `calculateHPriori`, `calculateHPosteriori`, `calculateHPosterioriTotal`
- `calculateRuido`, `calculatePerdida`, `calculateHCanal`
- `informacionMutuaABSimple`, `informacionMutuaBASimple`
- `isCanalNoRuido`, `isCanalDeterminante`
- `calcularCapacidad`

**Canales en Serie:**
- `generarComposedChannel`, `isReduccionSuficiente`, `getReducedChannel`
- `combinateCols`, `getCanalDeterminante`

**Utilidades:**
- `printMatrix`, `printMatrixVerbose`

---

**Total de funciones**: 78 (incluyendo dependencias internas)  
**Archivo**: `parcial2_template/total/utils_standalone.py`  
**Líneas**: ~976
