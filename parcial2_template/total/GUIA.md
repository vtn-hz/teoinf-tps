# GUIA.md - Guía de Funciones Consolidadas

## 📚 Resumen Conceptual: Teoría de la Información y la Comunicación

Este proyecto implementa los conceptos fundamentales de **codificación eficiente**, **modelado de canales ruidosos** y **límites teóricos de transmisión**, conforme a las Unidades 4, 5 y 6 del curso.

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
  - Un código es **compacto** si L = Hr(S), logrando η = 100% y redundancia = 0%

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
  - Relación: **H(A,B) = H(B) + H(A|B) = H(A) + H(B|A)**
- **Equivocación (Ruido) H(A|B)**: Pérdida de información causada por el canal
- **Pérdida H(B|A)**: Incertidumbre de la salida conocida la entrada

### Información Mutua

- **Definición**: **I(A,B) = H(A) - H(A|B)**
  - Representa la información sobre A que atraviesa el canal
- **Simetría**: **I(A,B) = I(B,A) = H(B) - H(B|A)**
- **Dependencia**: I(A,B) depende de P(ai) y P(bj|ai)

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
  - Canal Binario Simétrico: **C = 1 - H(p)**, donde p = probabilidad de error

### Canales Compuestos y Reducción

- **Canales en Serie**: Matriz compuesta = multiplicación de matrices individuales
  - La información mutua disminuye: **I(A,B) ≥ I(A,C)**
- **Reducción Suficiente**: Permite combinar salidas sin perder información mutua

### Probabilidad de Error

- **Regla de Decisión Óptima**: Usar Regla de Máxima Posibilidad Condicional para minimizar PE
- **Segundo Teorema de Shannon**: Si **H < C**, es posible transmitir con probabilidad de error arbitrariamente pequeña usando secuencias largas codificadas

---

## Catálogo de Funciones

### Cómo Importar

```python
# Importar el módulo completo
from parcial2_template.total import utils_standalone as utils

# Usar funciones
matriz_t = utils.getMatrixTraspuesta(matriz)
entropia = utils.calculateH(probabilidades)

# O importar funciones específicas
from parcial2_template.total.utils_standalone import calculateH, huffman, hamming
```

---

## 🔗 Mapeo Teoría → Implementación

### UNIDAD 4: Compresión

| Concepto Teórico | Función | Línea | Importar con |
|------------------|---------|-------|--------------|
| **Entropía H(S)** | `calculateH(P)` | ~248 | `from parcial2_template.total.utils_standalone import calculateH` |
| **Entropía base-r Hr(S)** | `calculateHr(pbs, r)` | ~257 | `from parcial2_template.total.utils_standalone import calculateHr` |
| **Información I(pi)** | `calculateI(pi)` | ~236 | `from parcial2_template.total.utils_standalone import calculateI` |
| **Información base-r Ir(pi)** | `calculateIr(p, r)` | ~253 | `from parcial2_template.total.utils_standalone import calculateIr` |
| **Longitud Media L** | `getLengthMedCodigo(cods, pbs)` | ~300 | `from parcial2_template.total.utils_standalone import getLengthMedCodigo` |
| **Rendimiento η** | `rendimientoCodigo(C, P)` | ~544 | `from parcial2_template.total.utils_standalone import rendimientoCodigo` |
| **Redundancia** | `redundanciaCodigo(C, P)` | ~550 | `from parcial2_template.total.utils_standalone import redundanciaCodigo` |
| **Primer Teorema Shannon** | `teoremaShannon(C, P, n)` | ~308 | `from parcial2_template.total.utils_standalone import teoremaShannon` |
| **Teorema Shannon (extendido)** | `teoremaShannonExtending(C, P, n)` | ~323 | `from parcial2_template.total.utils_standalone import teoremaShannonExtending` |
| **Desigualdad de Kraft** | `kraft(cods)` | ~307 | `from parcial2_template.total.utils_standalone import kraft` |

### Algoritmos de Codificación (UNIDAD 4)

| Algoritmo | Función | Línea | Importar con |
|-----------|---------|-------|--------------|
| **Huffman** | `huffman(P)` | ~587 | `from parcial2_template.total.utils_standalone import huffman` |
| **Shannon-Fano** | `shannonfano(P)` | ~630 | `from parcial2_template.total.utils_standalone import shannonfano` |
| **RLC (Run Length Coding)** | `rlc(message)` | ~639 | `from parcial2_template.total.utils_standalone import rlc` |
| **Codificar con Huffman/SF** | `codificar(message, alf, C)` | ~811 | `from parcial2_template.total.utils_standalone import codificar` |
| **Decodificar** | `decodificar(data, C, alf)` | ~836 | `from parcial2_template.total.utils_standalone import decodificar` |

### Propiedades de Códigos (UNIDAD 4)

| Propiedad | Función | Línea | Importar con |
|-----------|---------|-------|--------------|
| **Es instantáneo** | `isInstantaneous(codes)` | ~384 | `from parcial2_template.total.utils_standalone import isInstantaneous` |
| **Es unívoco** | `isUniquelyDecodable(codes)` | ~380 | `from parcial2_template.total.utils_standalone import isUniquelyDecodable` |
| **Es compacto** | `isCompacto(C, P)` | ~388 | `from parcial2_template.total.utils_standalone import isCompacto` |
| **Obtener propiedad** | `getPropiedadCodigoStr(codes)` | ~399 | `from parcial2_template.total.utils_standalone import getPropiedadCodigoStr` |

### Control de Errores (UNIDAD 4)

| Concepto | Función | Línea | Importar con |
|----------|---------|-------|--------------|
| **Distancia de Hamming d** | `hamming(C)` | ~662 | `from parcial2_template.total.utils_standalone import hamming` |
| **Errores detectables (d-1)** | `erroresDetectables(C)` | ~677 | `from parcial2_template.total.utils_standalone import erroresDetectables` |
| **Errores corregibles ⌊(d-1)/2⌋** | `erroresCorregibles(C)` | ~681 | `from parcial2_template.total.utils_standalone import erroresCorregibles` |
| **Codificar multiparidad** | `encodeMultiparidad(message, par)` | ~736 | `from parcial2_template.total.utils_standalone import encodeMultiparidad` |
| **Decodificar multiparidad** | `decodeMultiparidad(byte_array, par)` | ~958 | `from parcial2_template.total.utils_standalone import decodeMultiparidad` |
| **Detectar error multiparidad** | `detectarErrorMultiparidad(matrix, par)` | ~943 | `from parcial2_template.total.utils_standalone import detectarErrorMultiparidad` |

### Extensiones de Fuentes (UNIDAD 4)

| Concepto | Función | Línea | Importar con |
|----------|---------|-------|--------------|
| **Generar extensión orden n** | `generateExtensionsFromLL(alf, prob, n)` | ~266 | `from parcial2_template.total.utils_standalone import generateExtensionsFromLL` |
| **Extensión desde dict** | `generateExtensionsFromD(S, n)` | ~282 | `from parcial2_template.total.utils_standalone import generateExtensionsFromD` |
| **Extensión de probabilidades** | `generateExtensionsP(prob, n)` | ~287 | `from parcial2_template.total.utils_standalone import generateExtensionsP` |
| **Entropía de extensión Hn** | `calculateHn(P, n)` | ~297 | `from parcial2_template.total.utils_standalone import calculateHn` |

### UNIDAD 5: Canales - Probabilidades

| Concepto | Función | Línea | Importar con |
|----------|---------|-------|--------------|
| **P(ai) - Prob. a priori** | `getProbabilidadPriori(message)` | ~1195 | `from parcial2_template.total.utils_standalone import getProbabilidadPriori` |
| **P(B\|A) - Matriz del canal** | `getPrioriMatrixFull(fnt, cds, _input, _output)` | ~1199 | `from parcial2_template.total.utils_standalone import getPrioriMatrixFull` |
| **P(bj) - Prob. de salida** | `getProbsOutSymbols(Pinitial, channel)` | ~1228 | `from parcial2_template.total.utils_standalone import getProbsOutSymbols` |
| **P(A\|B) - Prob. a posteriori** | `getPosterioriMatrix(Pinitial, channel)` | ~1235 | `from parcial2_template.total.utils_standalone import getPosterioriMatrix` |
| **P(ai, bj) - Evento simultáneo** | `getMatrixSimultaneusEvent(Pinitial, channel)` | ~1246 | `from parcial2_template.total.utils_standalone import getMatrixSimultaneusEvent` |

### UNIDAD 5: Canales - Entropías

| Concepto | Función | Línea | Importar con |
|----------|---------|-------|--------------|
| **H(A) - Entropía a priori** | `calculateHPriori(Pa)` | ~1221 | `from parcial2_template.total.utils_standalone import calculateHPriori` |
| **H(A\|bj) - Entropía a posteriori** | `calculateHPosteriori(Pa, channel)` | ~1255 | `from parcial2_template.total.utils_standalone import calculateHPosteriori` |
| **H(B) - Entropía de salida** | `calculateHPosterioriTotal(Pa, channel)` | ~1268 | `from parcial2_template.total.utils_standalone import calculateHPosterioriTotal` |
| **H(A\|B) - Equivocación/Ruido** | `calculateRuido(Pa, channel)` | ~1290 | `from parcial2_template.total.utils_standalone import calculateRuido` |
| **H(B\|A) - Pérdida** | `calculatePerdida(Pa, channel)` | ~1323 | `from parcial2_template.total.utils_standalone import calculatePerdida` |
| **H(A,B) - Entropía afín** | `calculateHCanal(Pa, channel)` | ~1333 | `from parcial2_template.total.utils_standalone import calculateHCanal` |

### UNIDAD 5: Información Mutua

| Concepto | Función | Línea | Importar con |
|----------|---------|-------|--------------|
| **I(A,B) = H(A) - H(A\|B)** | `informacionMutuaAB(Pa, channel)` | ~1354 | `from parcial2_template.total.utils_standalone import informacionMutuaAB` |
| **I(A,B) fórmula simple** | `informacionMutuaABSimple(Pa, channel)` | ~1358 | `from parcial2_template.total.utils_standalone import informacionMutuaABSimple` |
| **I(B,A) = H(B) - H(B\|A)** | `informacionMutuaBA(Pa, channel)` | ~1371 | `from parcial2_template.total.utils_standalone import informacionMutuaBA` |
| **I(B,A) fórmula simple** | `informacionMutuaBASimple(Pa, channel)` | ~1379 | `from parcial2_template.total.utils_standalone import informacionMutuaBASimple` |

### UNIDAD 5: Propiedades de Canales

| Propiedad | Función | Línea | Importar con |
|-----------|---------|-------|--------------|
| **Canal sin ruido** | `isCanalNoRuido(channel)` | ~1396 | `from parcial2_template.total.utils_standalone import isCanalNoRuido` |
| **Canal determinante** | `isCanalDeterminante(channel)` | ~1407 | `from parcial2_template.total.utils_standalone import isCanalDeterminante` |
| **Canal simétrico** | `isCanalSimetrico(channel)` | ~1446 | `from parcial2_template.total.utils_standalone import isCanalSimetrico` |
| **Canal uniforme** | `isCanalUniforme(channel)` | ~1467 | `from parcial2_template.total.utils_standalone import isCanalUniforme` |

### UNIDAD 6: Capacidad del Canal

| Concepto | Función | Línea | Importar con |
|----------|---------|-------|--------------|
| **C (canal sin ruido)** | `calculateCapacidadNoRuido(channel)` | ~1575 | `from parcial2_template.total.utils_standalone import calculateCapacidadNoRuido` |
| **C (canal determinante)** | `calculateCapacidadDeterminante(channel)` | ~1579 | `from parcial2_template.total.utils_standalone import calculateCapacidadDeterminante` |
| **C (canal uniforme)** | `calculateCapacidadUniforme(channel)` | ~1583 | `from parcial2_template.total.utils_standalone import calculateCapacidadUniforme` |
| **C (general)** | `calcularCapacidad(channel)` | ~1593 | `from parcial2_template.total.utils_standalone import calcularCapacidad` |
| **C (binario por búsqueda)** | `calculateCapacidadBinario(channel, step)` | ~1604 | `from parcial2_template.total.utils_standalone import calculateCapacidadBinario` |

### UNIDAD 6: Canales Compuestos

| Concepto | Función | Línea | Importar con |
|----------|---------|-------|--------------|
| **Canales en serie** | `generarComposedChannel(channelA, channelB)` | ~1514 | `from parcial2_template.total.utils_standalone import generarComposedChannel` |
| **Reducción suficiente** | `isReduccionSuficiente(channel, col1, col2)` | ~1518 | `from parcial2_template.total.utils_standalone import isReduccionSuficiente` |
| **Obtener canal reducido** | `getReducedChannel(channel, squareLimit)` | ~1545 | `from parcial2_template.total.utils_standalone import getReducedChannel` |

### UNIDAD 6: Probabilidad de Error

| Concepto | Función | Línea | Importar con |
|----------|---------|-------|--------------|
| **PE (regla ML)** | `probabilidadError(channel, P)` | ~1624 | `from parcial2_template.total.utils_standalone import probabilidadError` |

### Fuentes de Markov (Memoria)

| Concepto | Función | Línea | Importar con |
|----------|---------|-------|--------------|
| **Generar matriz transición** | `generateMatrixTransicion(message)` | ~1758 | `from parcial2_template.total.utils_standalone import generateMatrixTransicion` |
| **Vector estacionario** | `calculateVEstacionario(M)` | ~1727 | `from parcial2_template.total.utils_standalone import calculateVEstacionario` |
| **H fuente markoviana** | `calculateHFuenteMarkoviana(M, V)` | ~1682 | `from parcial2_template.total.utils_standalone import calculateHFuenteMarkoviana` |
| **Es ergódica** | `isErgodica(M)` | ~1778 | `from parcial2_template.total.utils_standalone import isErgodica` |
| **Es fuente nula** | `isFuenteNula(M, tolerancia)` | ~1748 | `from parcial2_template.total.utils_standalone import isFuenteNula` |
| **Simular fuente Markov** | `simulateFuenteMarkov(M, S, n)` | ~1704 | `from parcial2_template.total.utils_standalone import simulateFuenteMarkov` |

### Utilidades Generales

| Función | Línea | Descripción | Importar con |
|---------|-------|-------------|--------------|
| `getMatrixTraspuesta(M)` | ~25 | Transpone una matriz | `from parcial2_template.total.utils_standalone import getMatrixTraspuesta` |
| `getMatrixZeros(filas, cols)` | ~33 | Crea matriz de ceros | `from parcial2_template.total.utils_standalone import getMatrixZeros` |
| `getMatrixProduct(A, B)` | ~57 | Multiplica matrices | `from parcial2_template.total.utils_standalone import getMatrixProduct` |
| `printMatrix(matrix)` | ~36 | Imprime matriz formateada | `from parcial2_template.total.utils_standalone import printMatrix` |
| `buildS(source)` | ~148 | Construye dict probabilidades | `from parcial2_template.total.utils_standalone import buildS` |

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Calcular Entropía y Rendimiento (UNIDAD 4)

```python
from parcial2_template.total.utils_standalone import calculateH, huffman, rendimientoCodigo

# Probabilidades de la fuente
P = [0.5, 0.3, 0.2]

# Calcular entropía
H = calculateH(P)
print(f"Entropía: {H:.4f} bits")  # ~1.4855 bits

# Generar código de Huffman
C = huffman(P)
print(f"Código Huffman: {C}")  # ['0', '10', '11']

# Calcular rendimiento
eta = rendimientoCodigo(C, P)
print(f"Rendimiento: {eta*100:.2f}%")  # ~98.37%
```

### Ejemplo 2: Verificar Teorema de Shannon (UNIDAD 4)

```python
from parcial2_template.total.utils_standalone import teoremaShannon, huffman

P = [0.4, 0.3, 0.2, 0.1]
C = huffman(P)

# Verificar teorema con extensión de orden 1
cumple = teoremaShannon(C, P, 1)
print(f"¿Cumple Teorema de Shannon? {cumple}")  # True
```

### Ejemplo 3: Análisis de Canal (UNIDAD 5)

```python
from parcial2_template.total.utils_standalone import (
    calculateRuido, calculatePerdida, informacionMutuaABSimple, 
    calculateHPriori, calculateHPosterioriTotal
)

# Canal binario simétrico con p=0.1
canal = [
    [0.9, 0.1],
    [0.1, 0.9]
]

# Probabilidades a priori uniformes
Pa = [0.5, 0.5]

# Métricas del canal
H_A = calculateHPriori(Pa)
ruido = calculateRuido(Pa, canal)
perdida = calculatePerdida(Pa, canal)
info_mutua = informacionMutuaABSimple(Pa, canal)

print(f"H(A): {H_A:.4f} bits")           # 1.0000
print(f"Ruido H(A|B): {ruido:.4f}")      # ~0.4690
print(f"Pérdida H(B|A): {perdida:.4f}")  # ~0.4690
print(f"I(A,B): {info_mutua:.4f}")       # ~0.5310

# Verificar: I(A,B) = H(A) - H(A|B)
assert abs(info_mutua - (H_A - ruido)) < 0.001
```

### Ejemplo 4: Capacidad de Canal (UNIDAD 6)

```python
from parcial2_template.total.utils_standalone import (
    calcularCapacidad, calculateCapacidadBinario,
    isCanalUniforme, isCanalSimetrico
)

# Canal uniforme
canal = [
    [0.3, 0.5, 0.2],
    [0.3, 0.5, 0.2],
    [0.3, 0.5, 0.2]
]

if isCanalUniforme(canal):
    C = calcularCapacidad(canal)
    print(f"Capacidad: {C:.4f} bits")

# Canal binario (búsqueda numérica)
canal_bin = [[0.9, 0.1], [0.2, 0.8]]
p_opt, C_bin = calculateCapacidadBinario(canal_bin, step=0.01)
print(f"P(a1) óptima: {p_opt:.4f}")
print(f"Capacidad: {C_bin:.4f} bits")
```

### Ejemplo 5: Control de Errores (UNIDAD 4)

```python
from parcial2_template.total.utils_standalone import (
    hamming, erroresDetectables, erroresCorregibles
)

# Código con paridad (d=2)
codigo = ['00', '11']
d = hamming(codigo)
print(f"Distancia de Hamming: {d}")              # 2
print(f"Errores detectables: {erroresDetectables(codigo)}")  # 1
print(f"Errores corregibles: {erroresCorregibles(codigo)}")  # 0

# Código de Hamming (d=3)
codigo_hamming = ['000', '011', '101', '110']
d = hamming(codigo_hamming)
print(f"\nCódigo Hamming:")
print(f"Distancia: {d}")                          # 2
print(f"Detecta: {erroresDetectables(codigo_hamming)} errores")  # 1
print(f"Corrige: {erroresCorregibles(codigo_hamming)} errores")  # 0
```

### Ejemplo 6: Probabilidad de Error (UNIDAD 6)

```python
from parcial2_template.total.utils_standalone import probabilidadError

# Canal cuadrado con ruido
canal = [
    [0.8, 0.1, 0.1],
    [0.1, 0.8, 0.1],
    [0.1, 0.1, 0.8]
]

# Distribución a priori
Pa = [0.5, 0.3, 0.2]

# Calcular PE bajo regla ML
PE = probabilidadError(canal, Pa)
print(f"Probabilidad de Error (PE): {PE:.4f}")  # ~0.1400
```

### Ejemplo 7: Fuentes de Markov

```python
from parcial2_template.total.utils_standalone import (
    generateMatrixTransicion, calculateVEstacionario,
    calculateHFuenteMarkoviana, isErgodica
)

# Mensaje de una fuente Markoviana
mensaje = "ababababaabaabaababaabababababab"

# Generar matriz de transición
M = generateMatrixTransicion(mensaje)
print("Matriz de transición:")
for row in M:
    print([f"{x:.3f}" for x in row])

# Calcular vector estacionario
V = calculateVEstacionario(M)
print(f"\nVector estacionario: {[f'{v:.4f}' for v in V]}")

# Verificar ergodicidad
ergodica = isErgodica(M)
print(f"¿Es ergódica? {ergodica}")

# Calcular entropía de la fuente
H = calculateHFuenteMarkoviana(M, V)
print(f"Entropía H: {H:.4f} bits/símbolo")
```

---

## 📝 Notas Importantes

1. **Archivo único y standalone**: Todas las funciones están en `parcial2_template/total/utils_standalone.py`

2. **Sin dependencias internas**: No requiere imports de otros módulos de utils/

3. **Librerías estándar**: Solo usa `math`, `random` y `os`

4. **Compatible Python 3.6+**

5. **Números de línea aproximados**: Pueden variar levemente según la versión del archivo

---

## 🔍 Índice Alfabético de Funciones

- `buildS` (148) - Construye dict de probabilidades
- `calculateCapacidadBinario` (1604) - Capacidad canal binario
- `calculateCapacidadDeterminante` (1579) - Capacidad canal determinante
- `calculateCapacidadNoRuido` (1575) - Capacidad canal sin ruido
- `calculateCapacidadUniforme` (1583) - Capacidad canal uniforme
- `calculateEquivocacion` (1294) - Equivocación H(A|B)
- `calculateH` (248) - Entropía H
- `calculateHAfinCanal` (1346) - Entropía afín
- `calculateHCanal` (1333) - Entropía del canal
- `calculateHFuenteMarkoviana` (1682) - Entropía fuente Markov
- `calculateHn` (297) - Entropía extensión orden n
- `calculateHPosteriori` (1255) - Entropías a posteriori
- `calculateHPosterioriTotal` (1268) - H(B)
- `calculateHPriori` (1221) - H(A)
- `calculateHr` (257) - Entropía base r
- `calculateI` (236) - Información I(pi)
- `calculateIr` (253) - Información base r
- `calculatePerdida` (1323) - Pérdida H(B|A)
- `calculateRuido` (1290) - Ruido H(A|B)
- `calculateVEstacionario` (1727) - Vector estacionario
- `calcularCapacidad` (1593) - Capacidad general
- `codificar` (811) - Codifica mensaje
- `codificar_rlc` (860) - Codifica con RLC
- `decodeMultiparidad` (958) - Decodifica multiparidad
- `decodificar` (836) - Decodifica mensaje
- `decodificar_rlc` (870) - Decodifica RLC
- `detectarErrorMultiparidad` (943) - Detecta error multiparidad
- `encodeMultiparidad` (736) - Codifica multiparidad
- `erroresCorregibles` (681) - Calcula errores corregibles
- `erroresDetectables` (677) - Calcula errores detectables
- `generateExtensionsFromD` (282) - Genera extensión dict
- `generateExtensionsFromLL` (266) - Genera extensión listas
- `generateExtensionsP` (287) - Extensión probabilidades
- `generateMatrixTransicion` (1758) - Matriz de transición
- `generarComposedChannel` (1514) - Canal compuesto
- `getAlfabetoCodigo` (291) - Alfabeto del código
- `getLengthMedCodigo` (300) - Longitud media
- `getLengthsCodigo` (296) - Longitudes del código
- `getMatrixProduct` (57) - Producto de matrices
- `getMatrixSimultaneusEvent` (1246) - Matriz evento simultáneo
- `getMatrixTraspuesta` (25) - Transpone matriz
- `getMatrixZeros` (33) - Matriz de ceros
- `getPosterioriMatrix` (1235) - Matriz a posteriori P(A|B)
- `getPrioriMatrixFull` (1199) - Matriz del canal P(B|A)
- `getProbabilidadPriori` (1195) - Probabilidades a priori
- `getProbsOutSymbols` (1228) - Probabilidades salida P(bj)
- `getPropiedadCodigoStr` (399) - Propiedad del código
- `getReducedChannel` (1545) - Canal reducido
- `hamming` (662) - Distancia de Hamming
- `huffman` (587) - Algoritmo Huffman
- `informacionMutuaAB` (1354) - I(A,B)
- `informacionMutuaABSimple` (1358) - I(A,B) simple
- `informacionMutuaBA` (1371) - I(B,A)
- `informacionMutuaBASimple` (1379) - I(B,A) simple
- `isCanalDeterminante` (1407) - Es canal determinante
- `isCanalNoRuido` (1396) - Es canal sin ruido
- `isCanalSimetrico` (1446) - Es canal simétrico
- `isCanalUniforme` (1467) - Es canal uniforme
- `isCompacto` (388) - Es código compacto
- `isErgodica` (1778) - Es fuente ergódica
- `isFuenteNula` (1748) - Es fuente nula
- `isInstantaneous` (384) - Es código instantáneo
- `isReduccionSuficiente` (1518) - Es reducción suficiente
- `isUniquelyDecodable` (380) - Es unívocamente decodificable
- `kraft` (307) - Desigualdad de Kraft
- `printMatrix` (36) - Imprime matriz
- `probabilidadError` (1624) - Probabilidad de error
- `recoverComprimido` (891) - Recupera comprimido
- `redundanciaCodigo` (550) - Redundancia
- `rendimientoCodigo` (544) - Rendimiento
- `rlc` (639) - Run Length Coding
- `sardinasPatterson` (347) - Algoritmo Sardinas-Patterson
- `saveComprimido` (882) - Guarda comprimido
- `shannonfano` (630) - Algoritmo Shannon-Fano
- `simulateFuenteMarkov` (1704) - Simula fuente Markov
- `tasaCompresion` (900) - Tasa de compresión
- `teoremaShannon` (308) - Primer Teorema Shannon
- `teoremaShannonExtending` (323) - Teorema Shannon extendido
- `trySolveErrorMultiparidad` (920) - Corrige error multiparidad

---

**Total de funciones**: ~120+  
**Archivo**: `parcial2_template/total/utils_standalone.py`  
**Líneas totales**: ~1791
