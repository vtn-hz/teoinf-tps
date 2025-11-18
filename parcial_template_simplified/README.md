# Parcial Template Simplificado

Versión simplificada de las unidades 4, 5 y 6 para preparación de parciales.

## Características

- ✅ **Sin input()**: Ejecución lineal sin interacción
- ✅ **Variables editables al inicio**: Fácil modificación de ejemplos
- ✅ **Outputs claros y concisos**: Solo cálculos clave
- ✅ **Autocontenido**: Todas las funciones implementadas inline (sin imports de utils/)
- ✅ **Sin comentarios**: Código limpio y mínimo
- ✅ **Presentación mínima**: Sin menús ni opciones complejas

## Archivos

### unidad4.py - Códigos y Codificación

Analiza un string fijo y muestra:
- Alfabeto y probabilidades
- Entropía de la fuente
- Códigos Huffman y Shannon-Fano
- Métricas principales (longitud media, rendimiento, redundancia)
- Verificación del Teorema de Shannon

**Variables editables:**
```python
MENSAJE = "ABRACADABRA"  # String a analizar
```

**Ejecutar:**
```bash
python3 parcial_template_simplified/unidad4.py
```

### unidad5.py - Teoría de Canales

Analiza un canal con matriz y probabilidades a priori definidas:
- Matriz de canal P(B|A)
- Probabilidades de salida P(B)
- Matriz a posteriori P(A|B)
- Matriz conjunta P(A,B)
- Entropías (entrada, salida, condicionales)
- Información mutua
- Relaciones matemáticas fundamentales

**Variables editables:**
```python
# Matriz de canal P(B|A) - Filas: entrada, Columnas: salida
MATRIZ_CANAL = [
    [0.6, 0.3, 0.1],
    [0.1, 0.8, 0.1],
    [0.2, 0.2, 0.6]
]

# Probabilidades a priori P(A)
PROB_PRIORI = [0.5, 0.3, 0.2]

# Etiquetas (opcionales)
SIMBOLOS_ENTRADA = ['a1', 'a2', 'a3']
SIMBOLOS_SALIDA = ['b1', 'b2', 'b3']
```

**Ejecutar:**
```bash
python3 parcial_template_simplified/unidad5.py
```

### unidad6.py - Composición de Canales

Analiza dos canales y su composición en serie:
- Matrices de ambos canales
- Métricas de cada canal (capacidad, información mutua, ruido, pérdida)
- Canal compuesto (multiplicación matricial)
- Métricas del canal compuesto
- Verificación de relaciones: I(A;C) ≤ min(I(A;B), I(B;C))

**Variables editables:**
```python
# PRIMER CANAL: A → B
CANAL_1 = [
    [0.9, 0.1, 0.0],
    [0.0, 0.9, 0.1],
    [0.1, 0.0, 0.9]
]
PROB_PRIORI_1 = [0.4, 0.35, 0.25]

# SEGUNDO CANAL: B → C
CANAL_2 = [
    [0.8, 0.15, 0.05],
    [0.1, 0.8, 0.1],
    [0.05, 0.15, 0.8]
]

# Etiquetas (opcionales)
SIMBOLOS_A = ['a1', 'a2', 'a3']
SIMBOLOS_B = ['b1', 'b2', 'b3']
SIMBOLOS_C = ['c1', 'c2', 'c3']
```

**Ejecutar:**
```bash
python3 parcial_template_simplified/unidad6.py
```

## Funciones Implementadas

Estos archivos son autocontenidos con todas las funciones implementadas inline:

### unidad4.py
- `calculateI`, `calculateH` - Información y entropía
- `buildS` - Construcción de alfabeto y probabilidades desde string
- `huffman`, `huffmanAlgorithm` - Algoritmo de Huffman
- `shannonfano`, `shannonfanoAlgorithm` - Algoritmo de Shannon-Fano
- `getLengthMedCodigo` - Longitud media de códigos
- `rendimientoCodigo`, `redundanciaCodigo` - Rendimiento y redundancia

### unidad5.py
- `calculateI`, `calculateH` - Información y entropía
- `getProbsOutSymbols` - Probabilidades de salida P(B)
- `getPosterioriMatrix` - Matriz a posteriori P(A|B)
- `getMatrixSimultaneusEvent` - Matriz conjunta P(A,B)
- `calculateRuido`, `calculatePerdida` - Ruido y pérdida
- `calculateHCanal` - Entropía conjunta
- `informacionMutuaABSimple` - Información mutua

### unidad6.py
- Todas las funciones de unidad5.py
- `getMatrixProduct` - Multiplicación matricial
- `isCanalNoRuido`, `isCanalDeterminante`, `isCanalUniforme` - Propiedades del canal
- `calcularCapacidad` - Capacidad del canal
- `generarComposedChannel` - Composición de canales

## Ventajas

1. **Rápido para estudiar**: Ver ejemplos completos en segundos
2. **Fácil de modificar**: Cambiar solo las variables al inicio
3. **Comprensión clara**: Outputs organizados por secciones
4. **Sin complejidad extra**: No hay menús ni configuraciones
5. **Autónomo**: Funciona independientemente, sin imports externos
6. **Código limpio**: Sin comentarios, solo implementación
7. **Basado en no_comments_template**: Sigue el mismo estilo que parcial2_template/no_comments_template/

## Diferencias con parcial2_template

| Característica | parcial2_template | parcial_template_simplified |
|---------------|-------------------|---------------------------|
| Líneas de código | 1000+ por archivo | ~150-300 por archivo |
| Documentación | Exhaustiva | Ninguna (solo código) |
| Dependencias | Ninguna (autocontenido) | Ninguna (autocontenido) |
| Input del usuario | Sí (una entrada) | No (todo definido arriba) |
| Explicaciones teóricas | Extensas en comentarios | Solo en outputs |
| Funciones duplicadas | Todas incluidas | Todas incluidas |
| Comentarios en código | Sí | No |

## Uso Recomendado

1. **Para estudiar**: Ejecutar tal como está para ver un ejemplo completo
2. **Para practicar**: Modificar las variables al inicio con ejercicios del parcial
3. **Para verificar**: Comparar resultados con cálculos manuales

## Ejemplos de Modificación

### Cambiar el mensaje en unidad4.py:
```python
MENSAJE = "MISSISSIPPI"
```

### Cambiar la matriz de canal en unidad5.py:
```python
MATRIZ_CANAL = [
    [0.9, 0.1],
    [0.2, 0.8]
]
PROB_PRIORI = [0.6, 0.4]
SIMBOLOS_ENTRADA = ['a1', 'a2']
SIMBOLOS_SALIDA = ['b1', 'b2']
```

### Cambiar los canales en unidad6.py:
```python
# Canal binario simétrico
CANAL_1 = [
    [0.9, 0.1],
    [0.1, 0.9]
]
PROB_PRIORI_1 = [0.5, 0.5]
```

## Notas

- Las matrices de canal deben tener filas que sumen 1 (distribución de probabilidad)
- Las probabilidades a priori deben sumar 1
- Para canales compuestos, el número de columnas de CANAL_1 debe coincidir con el número de filas de CANAL_2
