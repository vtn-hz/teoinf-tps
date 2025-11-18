# Teoría de la Información - TPs

Este repositorio contiene las implementaciones de trabajos prácticos de Teoría de la Información.

## Estructura del Proyecto

```
teoinf-tps/
├── utils/              # Módulos de utilidades
│   ├── fuente_nula/    # Funciones para fuentes nulas
│   ├── fuente_no_nula/ # Funciones para fuentes no nulas (Markov)
│   ├── codigos/        # Funciones para códigos y codificación
│   ├── canales/        # Funciones para análisis de canales
│   ├── errores/        # Funciones para detección y corrección de errores
│   └── codificacion/   # Codificadores y decodificadores
├── tp2/                # Trabajos prácticos del TP2
├── tp3/                # Trabajos prácticos del TP3
├── tp4/                # Trabajos prácticos del TP4
└── tp5/                # Trabajos prácticos del TP5
```

## Uso

### Configuración del Entorno

Para ejecutar los scripts, debes configurar el PYTHONPATH al directorio raíz del repositorio:

```bash
# Opción 1: Configurar para la sesión actual
export PYTHONPATH=/ruta/al/teoinf-tps

# Opción 2: Configurar para cada comando
PYTHONPATH=/ruta/al/teoinf-tps python3 tp2/1.py
```

### Ejemplos de Ejecución

```bash
# Calcular entropía
python3 tp2/1.py

# Probar teorema de Shannon
python3 tp4/2.py

# Analizar canal
python3 tp5/14.py
```

## Módulos Principales

### utils.fuente_nula
- `calculateH`: Cálculo de entropía H(X)
- `calculateI`: Cálculo de información I(x)
- `fuenteNulaSimulation`: Simulación de fuente nula

### utils.codigos
- `teoremaShannon`: Verificación del teorema de Shannon
- `sardinasPatterson`: Algoritmo de Sardinas-Patterson
- `kraft`: Desigualdad de Kraft
- `algorithm.huffman`: Algoritmo de Huffman
- `algorithm.shannonfano`: Algoritmo de Shannon-Fano

### utils.canales
- `priori.entropy`: Entropía a priori
- `posteriori.entropy`: Entropía a posteriori
- `entropy_media`: Entropías medias (ruido y pérdida)
- `informacion_mutua`: Información mutua

### utils.errores
- `hamming`: Distancia de Hamming
- `multiparidad`: Códigos de paridad múltiple

## Guías Detalladas

### 📚 Guía de Utils

El directorio `utils/` contiene módulos reutilizables organizados por tema:

#### **utils/fuente_nula/** - Fuentes de Memoria Nula
- **`calculateH.py`** - Cálculo de entropía H(X)
- **`calculateI.py`** - Cálculo de información I(x)
- **`alfabetoS.py`** - Construcción del alfabeto
- **`fuenteNulaSimulation.py`** - Simulación de fuentes
- **`extensiones/`** - Extensiones de fuente de orden n
  - `extensionP.py` - Probabilidades de extensión
  - `extensionGenerator.py` - Generador de extensiones
  - `calculateHn.py` - Entropía de extensión

#### **utils/fuente_no_nula/** - Fuentes con Memoria (Markov)
- **`calculateH.py`** - Entropía de fuentes Markov
- **`transitionMatrix.py`** - Matrices de transición
- **`markovSimulation.py`** - Simulación de cadenas de Markov

#### **utils/codigos/** - Códigos y Codificación
- **`teoremaShannon.py`** - Verificación del teorema de Shannon
- **`kraft.py`** - Desigualdad de Kraft
- **`sardinasPatterson.py`** - Algoritmo de Sardinas-Patterson (códigos únicamente decodificables)
- **`getPropiedadCodigo.py`** - Propiedades de códigos
- **`metadataCodigo.py`** - Metadata (longitudes, alfabeto, etc.)
- **`calculateHr.py`** / **`calculateIr.py`** - Entropía/información en base r
- **`algorithm/`** - Algoritmos de codificación
  - `huffman.py` - Algoritmo de Huffman
  - `shannonfano.py` - Algoritmo de Shannon-Fano
  - `rlc.py` - Run-Length Coding
- **`metricas/`** - Métricas de códigos
  - `rendRend.py` - Rendimiento y redundancia

#### **utils/codificacion/** - Codificadores y Decodificadores
- **`huffman_shannon/decode_encode.py`** - Codificación/decodificación Huffman y Shannon-Fano
- **`rlc/decode_encode.py`** - Codificación/decodificación RLC
- **`memory_decode_encode.py`** - Codificación con memoria
- **`default.py`** - Funciones por defecto
- **`metricas.py`** - Métricas de compresión

#### **utils/canales/** - Análisis de Canales
- **`priori/`** - Análisis a priori
  - `probs.py` - Probabilidades a priori P(A)
  - `entropy.py` - Entropía a priori H(A)
- **`posteriori/`** - Análisis a posteriori
  - `probs.py` - Probabilidades a posteriori P(A|B), P(A,B)
  - `entropy.py` - Entropía a posteriori H(A|B)
- **`entropy_media.py`** - Entropías medias (ruido y pérdida)
- **`informacion_mutua.py`** - Información mutua I(A;B)
- **`entropia_canal.py`** - Entropía conjunta H(A,B)
- **`propiedades.py`** - Propiedades de canales (sin ruido, determinístico, simétrico, uniforme)
- **`canales_serie.py`** - Composición de canales y reducción
- **`metricas.py`** - Capacidad del canal

#### **utils/errores/** - Detección y Corrección de Errores
- **`hamming.py`** - Distancia de Hamming
- **`multiparidad.py`** - Códigos de paridad múltiple
- **`checksum.py`** - Funciones de checksum

#### **utils/matrix.py** - Operaciones Matriciales
Funciones para manipulación de matrices (transpuesta, producto, impresión, etc.)

#### **utils/symbolFrequency.py** - Análisis de Frecuencias
Funciones para análisis de frecuencias de símbolos

### 📝 Guía de TPs (Trabajos Prácticos)

Los directorios `tp2/` a `tp6/` contienen ejercicios específicos:

#### **tp2/** - Fuentes de Información
Ejercicios sobre:
- Cálculo de entropía
- Información de símbolos
- Análisis de fuentes
- Extensiones de fuente

**Ejemplos:**
- `1.py` - Entropía básica
- `10.py` - Extensión de fuente orden 2
- `11.py` - Simulación de fuente
- `16.py` - Análisis completo de fuente

#### **tp3/** - Fuentes con Memoria (Markov)
Ejercicios sobre:
- Cadenas de Markov
- Matrices de transición
- Entropía de fuentes Markov
- Simulaciones

**Ejemplos:**
- `5.py` - Matriz de transición
- `9.py` - Entropía de Markov
- `11.py` - Simulación de cadena

#### **tp4/** - Códigos y Codificación
Ejercicios sobre:
- Algoritmos de Huffman y Shannon-Fano
- Teorema de Shannon
- Desigualdad de Kraft
- Sardinas-Patterson
- Codificación y decodificación
- RLC

**Ejemplos:**
- `2.py` - Teorema de Shannon
- `7.py` / `8.py` / `9.py` - Huffman
- `10.py` - Shannon-Fano
- `12.py` / `13.py` - Codificación/decodificación
- `17.py` - Análisis completo
- `20.py` - RLC
- `25.py` - Comparación de algoritmos

#### **tp5/** - Teoría de Canales
Ejercicios sobre:
- Matrices de canal P(B|A)
- Probabilidades a priori y a posteriori
- Entropías de canal
- Información mutua
- Ruido y pérdida

**Ejemplos:**
- `1.py` / `3.py` - Construcción de canal desde datos
- `6.py` - Probabilidades a posteriori
- `8_9.py` - Análisis completo de canal
- `10.py` - Entropías de canal
- `14.py` - Información mutua y métricas completas

#### **tp6/** - Propiedades y Capacidad de Canales
Ejercicios sobre:
- Propiedades de canales (sin ruido, determinístico, uniforme, simétrico)
- Capacidad del canal
- Canales en serie (composición)
- Reducción de canales
- Probabilidad de error

**Ejemplos:**
- `1.py` - Propiedades básicas de canal
- `3.py` - Canales en serie
- `5.py` - Reducción de canales (interactivo)
- `8.py` - Capacidad del canal
- `11.py` - Capacidad de canal binario
- `12.py` - Probabilidad de error ML
- `13.py` - Análisis de prob. error

### 🎓 Parcial 2 Template

El directorio `parcial2_template/` contiene **archivos autocontenidos** para las Unidades 4, 5 y 6:

#### Versión Documentada
- **`unidad4.py`** (1,147 líneas) - Códigos y codificación con documentación completa
- **`unidad5.py`** (893 líneas) - Teoría de canales con documentación completa
- **`unidad6.py`** (1,019 líneas) - Propiedades de canales con documentación completa

#### Versión Sin Comentarios (no_comments_template/)
- **`unidad4.py`** (380 líneas) - Solo código
- **`unidad5.py`** (313 líneas) - Solo código
- **`unidad6.py`** (397 líneas) - Solo código

**Características:**
- ✅ Sin dependencias externas (solo `math` y `typing`)
- ✅ Ejecutables con `python unidad{4,5,6}.py`
- ✅ Entrada única por `input()`
- ✅ Demostración completa de todas las funcionalidades
- ✅ Documentación teórica exhaustiva (versión documentada)

Ver **[GUIA_FUNCIONALIDADES.md](parcial2_template/GUIA_FUNCIONALIDADES.md)** para índice completo de funciones.

## Cambios Recientes (Refactorización)

Este proyecto ha sido refactorizado para usar imports estándar de Python en lugar de `exec(open(...).read())`:

- ✓ Todos los módulos utils ahora son módulos Python apropiados
- ✓ Se agregaron archivos `__init__.py` en todos los paquetes
- ✓ Todos los scripts tp* usan imports estándar
- ✓ 44 scripts probados y funcionando correctamente
- ✓ Agregados archivos autocontenidos para Unidades 4, 5 y 6

Para más detalles sobre los tests, ver [TEST_EVIDENCE.md](TEST_EVIDENCE.md).

## Requisitos

- Python 3.7+
- No se requieren dependencias externas

## Contribuir

Al agregar nuevos módulos o scripts:
1. Use imports estándar de Python (`from utils.modulo import funcion`)
2. No use `exec(open(...).read())`
3. Asegúrese de que los módulos no tengan efectos secundarios al importarse
4. Agregue `__init__.py` a nuevos paquetes
