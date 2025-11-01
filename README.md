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
- `informacion_mutua`: Información mutua

### utils.errores
- `hamming`: Distancia de Hamming
- `multiparidad`: Códigos de paridad múltiple

## Cambios Recientes (Refactorización)

Este proyecto ha sido refactorizado para usar imports estándar de Python en lugar de `exec(open(...).read())`:

- ✓ Todos los módulos utils ahora son módulos Python apropiados
- ✓ Se agregaron archivos `__init__.py` en todos los paquetes
- ✓ Todos los scripts tp* usan imports estándar
- ✓ 44 scripts probados y funcionando correctamente

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
