# Guía de Estudio: Teoría de la Información y la Comunicación

## Cuestionario de Repaso

1.  Describa los componentes clave del modelo de comunicación de Shannon y el papel que juega cada uno.
2.  ¿Cómo se relaciona la cantidad de información de un mensaje con la probabilidad de su ocurrencia según la teoría de la información?
3.  ¿Qué representa la entropía de una fuente de información sin memoria y cuáles son sus propiedades fundamentales?
4.  Explique la diferencia fundamental entre un código unívocamente decodificable y un código instantáneo, mencionando la propiedad clave que los distingue.
5.  ¿Cuál es el objetivo principal del algoritmo de Huffman y por qué su resultado se considera un código óptimo o compacto?
6.  Compare los métodos de compresión sin pérdida (lossless) y con pérdida (lossy) en cuanto a la integridad de los datos, sus tasas de compresión típicas y sus aplicaciones.
7.  ¿Cómo se utiliza la distancia de Hamming de un código para determinar su capacidad de detección y corrección de errores?
8.  ¿Qué mide la información mutua en un canal de comunicación y de qué dos factores principales depende?
9.  Defina el concepto de capacidad de un canal y explique su relación con la información mutua.
10. ¿Qué es una "regla de decisión" en el contexto de la recepción de mensajes y cómo se establece la regla óptima para minimizar la probabilidad de error?

---

## Clave de Respuestas

**1.** El modelo de Shannon consta de una fuente de información que genera el mensaje, un transmisor que lo convierte en una señal apta para la transmisión, un canal que es el medio por el cual viaja la señal, una fuente de ruido que puede introducir distorsiones y un receptor que decodifica la señal para entregar el mensaje al destino. Cada componente es esencial para posibilitar la transmisión desde el emisor hasta el receptor.

**2.** La cantidad de información es inversamente proporcional a la probabilidad de ocurrencia; los eventos menos probables o más inesperados son los que aportan mayor información. Matemáticamente, se calcula como el logaritmo de la inversa de la probabilidad del evento (I(E) = log(1/P(E))), lo que formaliza que a menor probabilidad, mayor es la incertidumbre resuelta y, por tanto, mayor la información recibida.

**3.** La entropía (H(S)) representa la cantidad media de información por símbolo que suministra una fuente sin memoria; también puede interpretarse como la incertidumbre promedio sobre el próximo símbolo que la fuente emitirá. Sus propiedades fundamentales son: siempre es mayor o igual a cero (0 ≤ H(S) ≤ log(n)), es nula solo si un evento tiene probabilidad 1, y alcanza su valor máximo cuando todos los símbolos son equiprobables.

**4.** Un código unívocamente decodificable garantiza que cualquier secuencia codificada tiene una única interpretación, aunque para decodificarla sea necesario analizar símbolos futuros. Un código instantáneo es un tipo especial de código unívocamente decodificable que además cumple la condición de prefijo: ninguna palabra de código es prefijo de otra, lo que permite decodificar cada símbolo tan pronto como se recibe su palabra de código completa.

**5.** El objetivo del algoritmo de Huffman es generar un código instantáneo que sea óptimo para una distribución de probabilidad dada. Se considera óptimo o compacto porque produce la mínima longitud media de código (L) posible, logrando la mayor eficiencia en la codificación al asignar sistemáticamente las palabras de código más cortas a los símbolos más frecuentes.

**6.** La compresión sin pérdida mantiene la integridad total de los datos, permitiendo que el archivo original sea reconstruido perfectamente; se usa para texto o código fuente y tiene tasas de compresión moderadas (ej. 2:1). La compresión con pérdida sacrifica parte de la información para lograr tasas de compresión mucho más altas (ej. 30:1), por lo que el archivo reconstruido es una aproximación; se usa para imágenes, video y sonido.

**7.** La distancia de Hamming de un código es la distancia mínima entre dos palabras de código cualesquiera. Un código con una distancia de Hamming *d* tiene la capacidad de detectar hasta *d-1* errores y de corregir hasta *(d-1)/2* errores. Por lo tanto, a mayor distancia de Hamming, mayor es la robustez del código frente a los errores.

**8.** La información mutua (I(A,B)) mide la reducción de la incertidumbre sobre la entrada del canal (A) que se logra al observar la salida (B); es decir, la cantidad de información sobre la entrada que atraviesa eficazmente el canal. Depende de dos factores: las probabilidades de los símbolos de la fuente de entrada y las propiedades del propio canal, expresadas en su matriz de probabilidades condicionales P(bj/ai).

**9.** La capacidad de un canal (C) es el máximo valor de la información mutua que puede transmitirse a través de él. Se obtiene al encontrar la distribución de probabilidad de entrada óptima que maximiza la función I(A,B), representando la máxima tasa de transmisión de información que el canal puede soportar con una probabilidad de error arbitrariamente pequeña.

**10.** Una regla de decisión es una función que asigna a cada símbolo de salida recibido un único símbolo de entrada que se presume fue el enviado. La regla óptima, denominada regla de máxima posibilidad condicional, es aquella que minimiza la probabilidad de error al asignar a cada salida *bj* el símbolo de entrada *ai* que tiene la mayor probabilidad a posteriori P(ai/bj).

---

## Preguntas de Ensayo

1.  Explique el Primer Teorema de Shannon y su importancia fundamental para la codificación de fuentes. Relacione los conceptos de entropía (H(S)), longitud media del código (L), rendimiento (η) y el uso de extensiones de fuente (Sn) para aproximar el límite teórico de compresión.
2.  Compare y contraste los algoritmos de codificación de Huffman y Shannon-Fano. Describa los pasos de cada algoritmo, discuta su optimalidad y explique por qué Huffman garantiza un código compacto mientras que Shannon-Fano es subóptimo.
3.  Describa el proceso de transmisión de información a través de un canal con ruido. Defina los conceptos de entropía a priori H(A), entropía a posteriori H(A/bj), equivocación H(A/B) e información mutua I(A,B), y explique cómo estas métricas cuantifican la incertidumbre y la información transmitida eficazmente.
4.  Analice los mecanismos para el tratamiento de errores en la transmisión de datos. Explique la diferencia entre códigos detectores y correctores, y detalle cómo la distancia de Hamming de un código determina su capacidad en ambos frentes. Ilustre con el ejemplo del código de paridad cruzada (VRC/LRC) su capacidad para detectar y corregir errores.
5.  Clasifique las fuentes de información según la dependencia estadística entre sus símbolos (con memoria y sin memoria). Describa cómo se modela una fuente de Markov de orden 1 utilizando un diagrama de estados y una matriz de transición, y explique el procedimiento para calcular su entropía en estado estacionario, contrastándola con la de una fuente de memoria nula.

---

## Glosario de Términos Clave

| Término | Definición |
| :--- | :--- |
| **Alfabeto Código** | El conjunto de símbolos {x1, x2, ..., xp} utilizado para construir las palabras de código. |
| **Alfabeto Fuente** | El conjunto de símbolos {s1, s2, ..., sq} emitidos por una fuente de información. |
| **Canal Binario Simétrico (BSC)** | Un canal con dos símbolos de entrada y dos de salida, donde la probabilidad de error (p) es la misma para ambos símbolos (P(1/0) = P(0/1) = p). |
| **Canal de Información** | El medio a través del cual se transmite la información. Se caracteriza por un alfabeto de entrada, un alfabeto de salida y un conjunto de probabilidades condicionales P(bj/ai) que definen la probabilidad de recibir bj cuando se envió ai. |
| **Canal Determinante** | Un canal cuya matriz de probabilidades tiene un único elemento no nulo (y por tanto, igual a 1) en cada fila. La entrada determina la salida con certeza. |
| **Canal sin Ruido** | Un canal cuya matriz de probabilidades tiene un único elemento no nulo en cada columna. La observación de la salida permite conocer la entrada con certeza. |
| **Capacidad del Canal (C)** | El máximo valor de la información mutua, max(I(A,B)), que se puede transmitir por un canal. Representa la máxima tasa de transmisión de información confiable. |
| **Código Bloque** | Un código que asigna a cada símbolo del alfabeto fuente una secuencia fija (palabra de código) de símbolos del alfabeto código. |
| **Código Compacto** | Un código unívoco cuya longitud media es igual o menor que la de cualquier otro código unívoco para la misma fuente y alfabeto. Los códigos de Huffman son compactos. |
| **Código de Huffman** | Un algoritmo que construye un código instantáneo óptimo (compacto) para una distribución de probabilidad dada, asignando palabras de código más cortas a los símbolos más probables. |
| **Código de Shannon-Fano** | Un algoritmo subóptimo para construir un código de prefijo dividiendo recursivamente el conjunto de símbolos en dos subconjuntos con probabilidades lo más cercanas posible. |
| **Código Instantáneo** | Un código unívocamente decodificable que cumple la propiedad de prefijo (ninguna palabra de código es prefijo de otra), permitiendo la decodificación inmediata de cada símbolo al recibir su palabra. |
| **Código no Singular** | Un código bloque donde todas las palabras de código asignadas a los símbolos de la fuente son distintas entre sí. |
| **Código Unívocamente Decodificable** | Un código que garantiza que cualquier secuencia de palabras de código puede ser decodificada de una sola manera, sin ambigüedad. |
| **Compresión con Pérdida (Lossy)** | Método de compresión que no mantiene la integridad de la información, resultando en datos descomprimidos que son una aproximación del original. Logra altas tasas de compresión. |
| **Compresión sin Pérdida (Lossless)** | Método de compresión que mantiene la integridad de la información, asegurando que los datos descomprimidos son idénticos a los originales. |
| **Distancia de Hamming** | El número de posiciones en las que dos palabras de código de igual longitud difieren. La distancia de un código es la mínima distancia de Hamming entre cualquier par de sus palabras. |
| **Entropía (H(S))** | La cantidad media de información por símbolo de una fuente. Mide la incertidumbre promedio sobre la salida de la fuente y establece el límite teórico para la compresión sin pérdida. |
| **Entropía Afín (H(A,B))** | Mide la incertidumbre promedio del suceso simultáneo de que ocurra una entrada ai y una salida bj. |
| **Equivocación (H(A/B))** | También llamado Ruido. Es la entropía media "a posteriori" de la entrada A, una vez conocida la salida B. Mide la incertidumbre que permanece sobre la entrada después de observar la salida. |
| **Estado Estacionario** | En una fuente de Markov ergódica, es la distribución de probabilidad única a la que converge la emisión de símbolos después de un tiempo suficientemente largo, independientemente del estado inicial. |
| **Extensión de una Fuente** | Una nueva fuente (Sn) cuyos símbolos son secuencias de n símbolos de la fuente original (S). Su entropía es H(Sn) = n * H(S). |
| **Fuente con Memoria (Markov)** | Una fuente donde la probabilidad de emisión de un símbolo depende de los m símbolos anteriores (orden m). |
| **Fuente sin Memoria** | Una fuente donde la emisión de cada símbolo es estadísticamente independiente de los símbolos anteriores. |
| **Información Mutua (I(A,B))** | La cantidad de información sobre la entrada A que se obtiene al observar la salida B. Se calcula como I(A,B) = H(A) - H(A/B) y mide la información que atraviesa eficazmente el canal. |
| **Inecuación de Kraft-McMillan** | Una condición necesaria y suficiente para la existencia de un código instantáneo (Kraft) o unívocamente decodificable (McMillan) con un conjunto dado de longitudes de palabras de código li. |
| **Longitud Media del Código (L)** | El promedio ponderado de las longitudes de las palabras de código, donde la ponderación es la probabilidad de cada símbolo de la fuente. L = Σ pi * li. |
| **Paridad** | Un método simple de detección de errores que consiste en añadir un bit extra a un bloque de datos para que el número total de "1"s sea par (paridad par) o impar (paridad impar). |
| **Pérdida (H(B/A))** | La entropía media de la salida B, una vez conocida la entrada A. Mide la incertidumbre sobre la salida que es introducida por el propio canal. |
| **Primer Teorema de Shannon** | Establece que la longitud media (L) de un código instantáneo está acotada por la entropía de la fuente (H(S)): H(S) ≤ L < H(S) + 1. Demuestra que no se puede comprimir una fuente más allá de su entropía. |
| **Probabilidad de Error (PE)** | La probabilidad de que el símbolo recibido y decodificado no sea el mismo que el símbolo transmitido. |
| **Redundancia** | La porción de un código que no aporta información nueva, calculada como 1 - η. Se introduce deliberadamente para la detección y corrección de errores. |
| **Regla de Decisión** | Una función que especifica el símbolo de entrada único que se asume fue enviado para cada símbolo de salida observado. |
| **Rendimiento (η)** | La eficiencia de un código, definida como la relación entre la entropía de la fuente y la longitud media del código: η = H(S) / L. |
| **Run Length Coding (RLC)** | Un método de compresión que codifica secuencias de símbolos idénticos y consecutivos mediante un par (símbolo, número de repeticiones). |
| **Segundo Teorema de Shannon** | Establece que si la entropía de una fuente (H) es menor que la capacidad de un canal (C), es posible transmitir información a través de ese canal con una probabilidad de error arbitrariamente pequeña. |