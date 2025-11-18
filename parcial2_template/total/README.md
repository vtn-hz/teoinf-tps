# Total - Utilidades Consolidadas

Este directorio contiene una versión **standalone** (independiente) de todas las funciones de utilidad del proyecto, consolidadas en un único archivo para facilitar su uso en exámenes parciales y trabajos prácticos.

## 📁 Contenido

### `utils_standalone.py`
Archivo Python que contiene **todas las funciones** de los módulos `utils/` consolidadas en un solo lugar:

- **1791 líneas** de código
- **134 funciones** implementadas
- **Sin dependencias internas** (no requiere imports de otros módulos del proyecto)
- Solo usa librerías estándar: `math`, `random`, `os`

### `GUIA.md`
Guía completa de referencia que incluye:

- Resumen conceptual de las Unidades 4, 5 y 6
- Mapeo de teoría a implementación
- Catálogo completo de funciones con números de línea
- Instrucciones de importación para cada función
- Ejemplos de uso prácticos
- Índice alfabético de funciones

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

## 📚 Organización por Unidades

### UNIDAD 4: Compresión y Control de Errores

**Compresión:**
- Entropía y cálculo de información (H, I, Hr, Ir)
- Algoritmos: Huffman, Shannon-Fano, RLC
- Propiedades de códigos (instantáneo, unívoco, compacto)
- Rendimiento y redundancia
- Teorema de Shannon

**Control de Errores:**
- Distancia de Hamming
- Códigos con paridad (simple y cruzada)
- Detección y corrección de errores

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
- Canal simétrico
- Canal uniforme

### UNIDAD 6: Capacidad y Probabilidad de Error

**Capacidad:**
- Capacidad de canal sin ruido
- Capacidad de canal determinante
- Capacidad de canal uniforme
- Capacidad de canal binario (búsqueda numérica)

**Canales Compuestos:**
- Canales en serie
- Reducción suficiente
- Canal reducido

**Probabilidad de Error:**
- Regla de decisión ML (máxima posibilidad)
- Cálculo de probabilidad de error PE

### Extras: Fuentes de Markov

- Generación de matriz de transición
- Vector estacionario
- Entropía de fuente markoviana
- Verificación de ergodicidad
- Simulación de fuentes con memoria

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
    isCanalUniforme, calcularCapacidad
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
3. **Índice alfabético**: Lista completa de funciones ordenadas
4. **Números de línea**: Ubicación exacta de cada función

## ✅ Verificación

Para verificar que todo funciona correctamente:

```python
from parcial2_template.total.utils_standalone import *

# Test básico
assert abs(calculateH([0.5, 0.5]) - 1.0) < 0.001
assert len(huffman([0.5, 0.3, 0.2])) == 3
assert hamming(['00', '11']) == 2

print("✓ Todo funcionando correctamente")
```

## 📝 Notas Importantes

1. **Archivo único**: No se requiere estructura de directorios de utils/
2. **Sin dependencias internas**: Funciona de forma completamente independiente
3. **Compatible**: Python 3.6+
4. **Testeado**: Todas las funciones principales han sido probadas

## 🎓 Para Exámenes

Este directorio está diseñado específicamente para:

- Tener **todas las funciones en un solo lugar**
- **Consultar rápidamente** números de línea en GUIA.md
- **Copiar/importar** fácilmente funciones necesarias
- **Referencia teórica** integrada con implementación

## 📊 Estadísticas

- **Funciones totales**: 134
- **Líneas de código**: 1,791
- **Líneas de documentación (GUIA.md)**: 533
- **Unidades cubiertas**: 3 (Unidades 4, 5 y 6)
- **Ejemplos de uso**: 7 completos en GUIA.md

---

**Autor**: Generado automáticamente desde utils/  
**Versión**: 1.0  
**Última actualización**: 2025
