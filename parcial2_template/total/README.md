# Total - Utilidades Consolidadas

Este directorio contiene una versión **standalone** (independiente) de todas las funciones de utilidad utilizadas en **tp4, tp5 y tp6**, consolidadas en un único archivo para facilitar su uso en exámenes parciales y trabajos prácticos.

## 📁 Contenido

### `utils_standalone.py`
Archivo Python que contiene **solo las funciones utilizadas en tp4, tp5 y tp6**:

- **976 líneas** de código
- **78 funciones** implementadas (incluyendo dependencias internas)
- **Sin dependencias internas** (no requiere imports de otros módulos del proyecto)
- Solo usa librerías estándar: `math`, `random`, `os`

### `GUIA.md`
Guía completa de referencia que incluye:

- Resumen conceptual de las Unidades 4, 5 y 6
- Mapeo de teoría a implementación
- Catálogo completo de funciones con instrucciones de importación
- Ejemplos de uso prácticos
- Lista de todas las funciones incluidas

### `README.md`
Este archivo - Guía de inicio rápido

## 🚀 Uso Rápido

```python
# Importar el módulo completo
from parcial2_template.total import utils_standalone as utils

# Usar funciones
entropia = utils.calculateH([0.5, 0.3, 0.2])
codigo = utils.huffman([0.5, 0.3, 0.2])
distancia = utils.hamming(['00', '11'])

# O importar funciones específicas
from parcial2_template.total.utils_standalone import (
    calculateH,
    huffman,
    hamming,
    informacionMutuaABSimple,
    calcularCapacidad
)
```

## 📚 Funciones por Categoría

### UNIDAD 4: Compresión y Control de Errores

**Compresión:**
- Entropía y cálculo de información (H, I, Hr, Ir)
- Algoritmos: Huffman, Shannon-Fano, RLC
- Rendimiento y redundancia
- Teorema de Shannon
- Extensiones de fuentes

**Control de Errores:**
- Distancia de Hamming
- Códigos con multiparidad
- Detección y corrección de errores

**Codificación:**
- Codificación/decodificación de mensajes
- Guardar y recuperar archivos comprimidos
- Cálculo de tasa de compresión

### UNIDAD 5: Canales de Comunicación

**Probabilidades:**
- Probabilidades a priori P(A)
- Matriz del canal P(B|A)
- Probabilidades a posteriori P(A|B)
- Probabilidades de salida P(B)

**Entropías:**
- Entropía a priori H(A)
- Entropía a posteriori H(A|B)
- Equivocación/Ruido H(A|B)
- Pérdida H(B|A)
- Entropía afín H(A,B)
- Información mutua I(A,B)

**Propiedades:**
- Canal sin ruido
- Canal determinante

### UNIDAD 6: Capacidad y Probabilidad de Error

**Capacidad:**
- Capacidad de canal (general)

**Canales Compuestos:**
- Canales en serie
- Reducción suficiente
- Canal reducido

### Utilidades

- Impresión de matrices con y sin etiquetas

## 💡 Ejemplos

### Ejemplo 1: Análisis de Código

```python
from parcial2_template.total.utils_standalone import (
    calculateH, huffman, rendimientoCodigo, teoremaShannon
)

P = [0.4, 0.3, 0.2, 0.1]

# Entropía de la fuente
H = calculateH(P)
print(f"Entropía: {H:.4f} bits")

# Generar código de Huffman
C = huffman(P)
print(f"Código: {C}")

# Calcular rendimiento
eta = rendimientoCodigo(C, P)
print(f"Rendimiento: {eta*100:.2f}%")

# Verificar teorema
cumple = teoremaShannon(C, P, 1)
print(f"Cumple Teorema de Shannon: {cumple}")
```

### Ejemplo 2: Análisis de Canal

```python
from parcial2_template.total.utils_standalone import (
    calculateRuido, calculatePerdida, informacionMutuaABSimple,
    isCanalNoRuido, calcularCapacidad
)

# Definir canal
canal = [[0.9, 0.1], [0.1, 0.9]]
Pa = [0.5, 0.5]

# Métricas
ruido = calculateRuido(Pa, canal)
perdida = calculatePerdida(Pa, canal)
info_mutua = informacionMutuaABSimple(Pa, canal)

print(f"Ruido H(A|B): {ruido:.4f}")
print(f"Pérdida H(B|A): {perdida:.4f}")
print(f"Información Mutua I(A,B): {info_mutua:.4f}")
```

### Ejemplo 3: Control de Errores

```python
from parcial2_template.total.utils_standalone import (
    hamming, erroresDetectables, erroresCorregibles
)

codigo = ['000', '011', '101', '110']

d = hamming(codigo)
print(f"Distancia de Hamming: {d}")
print(f"Detecta hasta: {erroresDetectables(codigo)} errores")
print(f"Corrige hasta: {erroresCorregibles(codigo)} errores")
```

## 🔍 Búsqueda Rápida

Para encontrar una función específica, consulta `GUIA.md` que incluye:

1. **Búsqueda por concepto**: Mapeo de teoría a función
2. **Búsqueda por unidad**: Agrupación por unidades 4, 5 y 6
3. **Instrucciones de importación**: Para cada función

## 📝 Notas Importantes

1. **Solo funciones usadas en tp4, tp5, tp6**: Este archivo contiene únicamente las funciones que se importan y utilizan en los trabajos prácticos
2. **Sin dependencias internas**: Funciona de forma completamente independiente
3. **Compatible**: Python 3.6+
4. **Testeado**: Todas las funciones principales han sido probadas

## 📊 Estadísticas

- **Funciones totales**: 78 (incluyendo dependencias internas)
- **Líneas de código**: 976
- **Unidades cubiertas**: 3 (Unidades 4, 5 y 6)
- **Funciones directamente usadas en tp4/tp5/tp6**: 50
- **Funciones de soporte/dependencias**: 28

---

**Criterio de inclusión**: Solo funciones utilizadas en tp4, tp5 y tp6  
**Versión**: 2.0 (filtrada)  
**Última actualización**: 2025
