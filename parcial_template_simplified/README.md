# Parcial Template Simplificado

Versión simplificada de las unidades 4, 5 y 6 para preparación de parciales.

## Características

- ✅ **Sin input()**: Ejecución lineal sin interacción
- ✅ **Variables editables al inicio**: Fácil modificación de ejemplos
- ✅ **Outputs claros y concisos**: Solo cálculos clave
- ✅ **Usa funciones existentes**: No duplica código del repositorio
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

## Funciones Utilizadas

Estos archivos utilizan las funciones existentes del repositorio:

### unidad4.py
- `utils.fuente_nula.alfabetoS.buildS` - Construcción de alfabeto y probabilidades
- `utils.fuente_nula.calculateH` - Cálculo de entropía
- `utils.codigos.algorithm.huffman` - Algoritmo de Huffman
- `utils.codigos.algorithm.shannonfano` - Algoritmo de Shannon-Fano
- `utils.codigos.metadataCodigo` - Longitud media de códigos
- `utils.codigos.metricas.rendRend` - Rendimiento y redundancia

### unidad5.py
- `utils.canales.priori.entropy` - Entropía a priori
- `utils.canales.posteriori.probs` - Probabilidades a posteriori y conjuntas
- `utils.canales.posteriori.entropy` - Entropía a posteriori
- `utils.canales.entropy_media` - Ruido y pérdida
- `utils.canales.entropia_canal` - Entropía conjunta
- `utils.canales.informacion_mutua` - Información mutua

### unidad6.py
- `utils.canales.metricas` - Capacidad del canal
- `utils.canales.canales_serie` - Composición de canales
- Todas las funciones de unidad5.py

## Ventajas

1. **Rápido para estudiar**: Ver ejemplos completos en segundos
2. **Fácil de modificar**: Cambiar solo las variables al inicio
3. **Comprensión clara**: Outputs organizados por secciones
4. **Sin complejidad extra**: No hay menús ni configuraciones
5. **Autónomo**: Funciona independientemente del resto del repositorio

## Diferencias con parcial2_template

| Característica | parcial2_template | parcial_template_simplified |
|---------------|-------------------|---------------------------|
| Líneas de código | 1000+ por archivo | ~150-200 por archivo |
| Documentación | Exhaustiva | Mínima |
| Dependencias | Ninguna (autocontenido) | Usa utils/ del repo |
| Input del usuario | Sí (una entrada) | No (todo definido arriba) |
| Explicaciones teóricas | Extensas en comentarios | Solo en outputs |
| Funciones duplicadas | Todas incluidas | Solo imports |

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
