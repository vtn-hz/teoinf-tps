# Guía de Funcionalidades - Parcial 2 Template

Esta guía describe la ubicación de todas las funcionalidades implementadas en los archivos autocontenidos de las Unidades 4, 5 y 6.

## Estructura del Directorio

```
parcial2_template/
├── GUIA_FUNCIONALIDADES.md (este archivo)
├── unidad4.py (1,147 líneas - con documentación completa)
├── unidad5.py (893 líneas - con documentación completa)
├── unidad6.py (1,019 líneas - con documentación completa)
└── no_comments_template/
    ├── README.md
    ├── unidad4.py (380 líneas - sin comentarios)
    ├── unidad5.py (313 líneas - sin comentarios)
    └── unidad6.py (397 líneas - sin comentarios)
```

---

## UNIDAD 4: Códigos y Codificación

**Archivo:** `unidad4.py` (versión documentada) o `no_comments_template/unidad4.py` (sin comentarios)

**Ejecución:** `python unidad4.py`

### Índice de Funcionalidades

#### 1. Funciones de Información y Entropía
- **`calculateI(pi)`** - Calcula información I(x) = log₂(1/p)
- **`calculateH(P)`** - Calcula entropía H(X) = -Σ pᵢ log₂(pᵢ)
- **`calculateIr(p, r)`** - Información en base r
- **`calculateHr(pbs, r)`** - Entropía en base r

**Ubicación en archivo:** Líneas 74-149 (versión documentada)

#### 2. Análisis de Símbolos
- **`getSymbolOcurrences(phrase)`** - Cuenta ocurrencias de símbolos
- **`buildS(source)`** - Construye distribución de probabilidad empírica

**Ubicación en archivo:** Líneas 154-188 (versión documentada)

#### 3. Extensiones de Fuente
- **`generateExtensionsP(prob, n)`** - Genera probabilidades de extensión de orden n
- **`generateExtensionsFromLL(alf, prob, n)`** - Genera símbolos y probabilidades de extensión

**Ubicación en archivo:** Líneas 193-247 (versión documentada)

#### 4. Algoritmo de Huffman
- **`initializeHuffman(P)`** - Inicializa estructura Huffman
- **`huffmanAlgorithm(result, P)`** - Implementación del algoritmo
- **`huffman(P)`** - Genera códigos Huffman

**Ubicación en archivo:** Líneas 252-327 (versión documentada)

**Características:** Códigos óptimos (longitud media mínima), códigos prefijo

#### 5. Algoritmo de Shannon-Fano
- **`initializeShannonFano(P)`** - Inicializa estructura
- **`propagateSubfix(result, P, fix)`** - Propaga sufijos
- **`shannonfanoAlgorithm(result, Pindex)`** - Implementación recursiva
- **`shannonfano(P)`** - Genera códigos Shannon-Fano

**Ubicación en archivo:** Líneas 332-415 (versión documentada)

**Características:** Códigos prefijo, división recursiva por probabilidad

#### 6. Run-Length Coding (RLC)
- **`rlc(message)`** - Codifica secuencias repetidas como (símbolo, cantidad)

**Ubicación en archivo:** Líneas 420-460 (versión documentada)

**Uso:** Eficiente para datos con muchas repeticiones

#### 7. Metadata y Métricas de Códigos
- **`getAlfabetoCodigo(cods)`** - Obtiene alfabeto del código
- **`getLengthsCodigo(cods)`** - Obtiene longitudes de palabras
- **`getLengthMedCodigo(cods, pbs)`** - Calcula longitud media L
- **`rendimientoCodigo(C, P)`** - Calcula rendimiento η = H/L
- **`redundanciaCodigo(C, P)`** - Calcula redundancia R = 1-η

**Ubicación en archivo:** Líneas 465-551 (versión documentada)

#### 8. Teorema de Shannon
- **`teoremaShannon(C, P, n)`** - Verifica el Primer Teorema de Shannon: Hᵣ(X)/n ≤ L/n < Hᵣ(X)/n + 1/n
- **`teoremaShannonExtending(C, P, n)`** - Verifica con extensión de código

**Ubicación en archivo:** Líneas 556-619 (versión documentada)

#### 9. Codificación y Decodificación
- **`build_byteArray(bits)`** - Convierte bits a bytearray
- **`solve_byteArray(bytes)`** - Convierte bytearray a bits
- **`codificar(message, alf, C)`** - Codifica mensaje
- **`decodificar(data, C, alf)`** - Decodifica mensaje
- **`tasaCompresion(message, compressed)`** - Calcula tasa de compresión

**Ubicación en archivo:** Líneas 624-724 (versión documentada)

#### 10. Distancia de Hamming y Errores
- **`hamming(C)`** - Calcula distancia mínima de Hamming
- **`erroresDetectables(C)`** - Calcula errores detectables = dₘᵢₙ - 1
- **`erroresCorregibles(C)`** - Calcula errores corregibles = ⌊(dₘᵢₙ-1)/2⌋

**Ubicación en archivo:** Líneas 729-793 (versión documentada)

**Teoría:** Capacidad de detección y corrección basada en distancia mínima

#### 11. Funciones de Visualización
- **`printTable(labels, P, C1, C2)`** - Tabla comparativa de códigos
- **`printMetrics(C1, C2, P)`** - Métricas de rendimiento

**Ubicación en archivo:** Líneas 798-837 (versión documentada)

---

## UNIDAD 5: Teoría de Canales

**Archivo:** `unidad5.py` (versión documentada) o `no_comments_template/unidad5.py` (sin comentarios)

**Ejecución:** `python unidad5.py`

### Índice de Funcionalidades

#### 1. Funciones Básicas
- **`calculateI(pi)`** - Información
- **`calculateH(P)`** - Entropía
- **`getSymbolOcurrences(phrase)`** - Cuenta símbolos
- **`buildS(source)`** - Distribución empírica
- **`getProbabilidadPriori(message)`** - Probabilidades a priori

**Ubicación en archivo:** Líneas 70-181 (versión documentada)

#### 2. Funciones Matriciales
- **`getMatrixZeros(filas, columnas)`** - Matriz de ceros
- **`getMatrixTraspuesta(M)`** - Transpuesta
- **`printMatrix(matrix)`** - Impresión formateada

**Ubicación en archivo:** Líneas 186-220 (versión documentada)

#### 3. Construcción de Matriz de Canal
- **`getPrioriMatrixFull(fnt, cds, _input, _output)`** - Construye P(B|A) desde datos
- **`getPrioriMatrixJust(_input, _output)`** - Infiere alfabetos

**Ubicación en archivo:** Líneas 225-285 (versión documentada)

**Teoría:** P(bⱼ|aᵢ) = count(aᵢ→bⱼ) / count(aᵢ)

#### 4. Probabilidades del Canal
- **`getProbsOutSymbols(Pinitial, channel)`** - P(B) = Σᵢ P(bⱼ|aᵢ)·P(aᵢ)
- **`getPosterioriMatrix(Pinitial, channel)`** - P(A|B) por Teorema de Bayes
- **`getMatrixSimultaneusEvent(Pinitial, channel)`** - P(A,B) = P(B|A)·P(A)

**Ubicación en archivo:** Líneas 290-352 (versión documentada)

#### 5. Entropías del Canal
- **`calculateHPriori(Pa)`** - H(A) entropía de entrada
- **`calculateHPosteriori(Pa, channel)`** - H(A|bⱼ) para cada salida
- **`calculateHPosterioriTotal(Pa, channel)`** - H(B) entropía de salida
- **`calculateHPosterioriMediaABSimple(Pa, channel)`** - H(A|B) equivocación/ruido
- **`calculateRuido(Pa, channel)`** - Alias de H(A|B)
- **`calculateHPosterioriMediaBASimple(Pa, channel)`** - H(B|A) pérdida
- **`calculatePerdida(Pa, channel)`** - Alias de H(B|A)
- **`calculateHCanal(Pa, channel)`** - H(A,B) entropía conjunta

**Ubicación en archivo:** Líneas 357-510 (versión documentada)

**Relaciones:** H(A,B) = H(A) + H(B|A) = H(B) + H(A|B)

#### 6. Información Mutua
- **`informacionMutuaABSimple(Pa, channel)`** - I(A;B) = H(A) - H(A|B) = H(B) - H(B|A)
- **`informacionMutuaBASimple(Pa, channel)`** - I(B;A) (simétrica)

**Ubicación en archivo:** Líneas 515-565 (versión documentada)

**Propiedades:** I(A;B) ≥ 0, I(A;B) = I(B;A), I(A;B) ≤ min(H(A), H(B))

#### 7. Funciones de Visualización
- **`printChannelInfo(S, C, matrix)`** - Imprime matriz con etiquetas
- **`showS(S)`** - Muestra distribución

**Ubicación en archivo:** Líneas 570-607 (versión documentada)

---

## UNIDAD 6: Propiedades y Capacidad de Canales

**Archivo:** `unidad6.py` (versión documentada) o `no_comments_template/unidad6.py` (sin comentarios)

**Ejecución:** `python unidad6.py`

### Índice de Funcionalidades

#### 1. Funciones Básicas (Reutilizadas)
- **`calculateI(pi)`** - Información
- **`calculateH(P)`** - Entropía
- **`getMatrixZeros(filas, columnas)`** - Matriz de ceros
- **`getMatrixProduct(A, B)`** - Multiplicación matricial
- **`printMatrix(matrix)`** - Impresión

**Ubicación en archivo:** Líneas 78-151 (versión documentada)

#### 2. Probabilidades del Canal
- **`getProbsOutSymbols(Pinitial, channel)`** - P(B)
- **`getPosterioriMatrix(Pinitial, channel)`** - P(A|B)
- **`getMatrixSimultaneusEvent(Pinitial, channel)`** - P(A,B)

**Ubicación en archivo:** Líneas 156-201 (versión documentada)

#### 3. Información Mutua y Entropías
- **`informacionMutuaABSimple(Pa, channel)`** - I(A;B)
- **`calculateRuido(Pa, channel)`** - H(A|B)
- **`calculatePerdida(Pa, channel)`** - H(B|A)

**Ubicación en archivo:** Líneas 206-267 (versión documentada)

#### 4. Propiedades de Canales
- **`isCanalNoRuido(channel)`** - Verifica si es sin ruido (cada columna ≤ 1 elemento no nulo)
- **`isCanalDeterminante(channel)`** - Verifica si es determinístico (cada fila = 1 elemento)
- **`isCanalUniforme(channel)`** - Verifica si las filas son permutaciones
- **`isCanalSimetrico(channel)`** - Verifica simetría (filas y columnas permutaciones)

**Ubicación en archivo:** Líneas 272-381 (versión documentada)

**Teoría:**
- Sin ruido: H(A|B) = 0
- Determinístico: H(B|A) = 0
- Uniforme/Simétrico: Simplifican cálculo de capacidad

#### 5. Capacidad del Canal
- **`calculateCapacidadNoRuido(channel)`** - C = log₂(|A|)
- **`calculateCapacidadDeterminante(channel)`** - C = log₂(|B|)
- **`calculateCapacidadUniforme(channel)`** - C = log₂(|B|) - H(fila)
- **`calcularCapacidad(channel)`** - Selector automático según propiedades
- **`calculateCapacidadBinario(channel, step)`** - Optimización numérica para canales binarios

**Ubicación en archivo:** Líneas 386-483 (versión documentada)

**Teoría:** C = max_{P(A)} I(A;B)

#### 6. Canales en Serie (Composición)
- **`generarComposedChannel(channelA, channelB)`** - P(C|A) = P(B|A) × P(C|B)

**Ubicación en archivo:** Líneas 488-505 (versión documentada)

**Propiedad:** I(A;C) ≤ min(I(A;B), I(B;C))

#### 7. Reducción de Canales
- **`isReduccionSuficiente(channel, col1, col2)`** - Verifica si columnas son combinables
- **`combinateCols(channel, col1, col2)`** - Combina columnas
- **`getCanalDeterminante(channel, col1, col2)`** - Canal determinístico para combinación
- **`getReducedChannel(channel)`** - Reduce canal completamente

**Ubicación en archivo:** Líneas 510-600 (versión documentada)

**Teoría:** Columnas combinables si ∃k: P(bⱼ₁|aᵢ) = k·P(bⱼ₂|aᵢ) ∀i

#### 8. Probabilidad de Error
- **`probabilidadError(channel, P)`** - Calcula Pₑ bajo regla ML (Maximum Likelihood)

**Ubicación en archivo:** Líneas 605-665 (versión documentada)

**Teoría:** Pₑ = Σᵢ P(aᵢ)·(1 - max_j P(bⱼ|aᵢ))

---

## Diferencias entre Versiones

### Versión Documentada (directorio raíz)
- **Tamaño:** 3,059 líneas totales
- **Contenido:**
  - Docstring de módulo con resumen teórico completo
  - Docstrings en todas las funciones con "Fundamento teórico"
  - Comentarios inline explicativos
  - Anotaciones de tipo completas
  - Ejemplos en docstrings

### Versión Sin Comentarios (no_comments_template/)
- **Tamaño:** 1,090 líneas totales (65% reducción)
- **Contenido:**
  - Solo código ejecutable
  - Anotaciones de tipo preservadas
  - Sin docstrings ni comentarios
  - Misma funcionalidad exacta

### ¿Cuál usar?

- **Versión Documentada:** Para aprendizaje, comprensión de teoría, referencia
- **Versión Sin Comentarios:** Para evaluaciones, envío de código limpio, producción

---

## Dependencias

**Ninguna externa.** Solo librerías estándar de Python:
- `math` - Funciones matemáticas (log, log2)
- `typing` - Type hints (List, Tuple, Dict, Optional)

---

## Ejecución

### Todas las versiones aceptan input estándar:

```bash
# Unidad 4: Ingresa un mensaje de texto
echo "MISSISSIPPI" | python unidad4.py

# Unidad 5: Ingresa secuencias entrada/salida
echo -e "AABBCC\n010110" | python unidad5.py

# Unidad 6: Selecciona un canal (1-5)
echo "4" | python unidad6.py
```

### O ejecución interactiva:

```bash
python unidad4.py
# > Ingrese un mensaje: ABRACADABRA

python unidad5.py  
# > Entrada: AAABBBCCC
# > Salida: 010101010

python unidad6.py
# > Seleccione canal (1-5): 3
```

---

## Verificación

Todos los archivos han sido probados:
- ✅ Sintaxis Python válida
- ✅ Ejecución sin errores
- ✅ Output correcto y formateado
- ✅ CodeQL security scan: 0 alertas
- ✅ Funcionalidad idéntica entre versiones documentada y sin comentarios

---

## Comparación Rápida de Funcionalidades

| Funcionalidad | Unidad 4 | Unidad 5 | Unidad 6 |
|---------------|----------|----------|----------|
| Huffman | ✓ | - | - |
| Shannon-Fano | ✓ | - | - |
| RLC | ✓ | - | - |
| Teorema Shannon | ✓ | - | - |
| Hamming | ✓ | - | - |
| Canal P(B\|A) | - | ✓ | ✓ |
| Probabilidades a posteriori | - | ✓ | ✓ |
| Entropías de canal | - | ✓ | ✓ |
| Información mutua | - | ✓ | ✓ |
| Propiedades canal | - | - | ✓ |
| Capacidad | - | - | ✓ |
| Reducción canal | - | - | ✓ |
| Prob. error ML | - | - | ✓ |

---

## Soporte

Para más información sobre la teoría detrás de estas implementaciones, consulte:
- Documentación en los archivos con comentarios
- README.md principal del repositorio
- Apuntes de Teoría de la Información

**Última actualización:** Noviembre 2025
