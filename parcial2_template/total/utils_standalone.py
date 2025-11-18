"""
Archivo Standalone de Utilidades - Teoría de la Información
============================================================
Este archivo consolida todas las funciones de las unidades 4, 5 y 6
del curso de Teoría de la Información y la Comunicación.

UNIDAD 4: Compresión y Control de Errores
UNIDAD 5: Caracterización de Canales  
UNIDAD 6: Capacidad y Probabilidad de Error

Generado automáticamente consolidando todos los módulos de utils/
"""

import math
import random
import os



# ============================================================================
# MATRIZ - Operaciones con matrices
# ============================================================================


def getMatrixTraspuesta(M: list[list]) -> list[list]:
    result = []
    for i in range(len(M[0])):
        result.append([])  
        for j in range(len(M)):
            result[i].append(M[j][i])  
    return result

def getMatrixZeros(filas: int, columnas: int) -> list[list[int]]:
    return [[0 for _ in range(columnas)] for _ in range(filas)]

def printMatrix(matrix: list[list]) -> None:
    max_width = max(len(f"{elem:.2f}") for row in matrix for elem in row)
    for row in matrix:
        print(" ".join(f"{elem:>{max_width}.2f}" for elem in row))

def getBinMatrixFromStr(message: str) -> list:
    binary_matrix = []
    for char in message:
        binary_row = list(map(int, format(ord(char), '07b')))
        binary_matrix.append(binary_row)
    return binary_matrix
    
def getIntMatrixFromByteArray( byte_array: bytearray ) -> list:
    matrix = []
    for byte in byte_array:
        row = []
        for i in range(0, 8):
            row.append( (byte >> (7 - i)) & 1 )
        matrix.append(row)
    return matrix

def getMatrixProduct(A: list[list], B: list[list]) -> list:

    # A:{ixj}*B:{jxk} = C{ixk}
    if (len(A[0]) != len(B)):
        raise Exception("Las matrices no son compatibles para la multiplicacion matricial")

    result = getMatrixZeros(len(A), len(B[0]))

    for i in range(len(A)):
        for k in range(len(B[0])):
            amount = 0
            for j in range(len(B)):
                amount += A[i][j] * B[j][k]
            
            result[i][k] = amount
    
    return result


def getDeterminanteRowDuplicated(matrix: list[list], col: int, row: int) -> float:
    result = getMatrixZeros(len(matrix[0]), len(matrix[0]) - 1)
    j = 0
    for i in range(len(matrix[0])):
        if i != row:
            result[i][j] = 1
            j += 1
    
    result[row][col] = 1
    return result

    # ...existing code...

def printMatrixVerbose(matrix: list[list], row_labels: list[str], col_labels: list[str]) -> None:
    """
    Imprime la matriz con etiquetas de filas y columnas.
    - matrix: matriz numérica (list of lists)
    - row_labels: etiquetas para cada fila (len == filas)
    - col_labels: etiquetas para cada columna (len == columnas)
    """
    if not matrix:
        print("(matriz vacía)")
        return
    filas = len(matrix)
    columnas = len(matrix[0])

    if len(row_labels) != filas:
        raise ValueError("row_labels debe tener la misma cantidad de elementos que filas de la matriz.")
    if len(col_labels) != columnas:
        raise ValueError("col_labels debe tener la misma cantidad de elementos que columnas de la matriz.")

    # Ancho para números
    num_width = max(len(f"{elem:.2f}") for row in matrix for elem in row)
    # Ancho para etiquetas de fila
    row_label_width = max(len(lbl) for lbl in row_labels)
    # Anchos por columna (el máximo entre etiqueta y número)
    col_widths = []
    for j in range(columnas):
        max_val_width = max(len(f"{matrix[i][j]:.2f}") for i in range(filas))
        col_widths.append(max(max_val_width, len(col_labels[j]), num_width))

    # Encabezado
    header = " " * (row_label_width) + "  " + " ".join(f"{col_labels[j]:>{col_widths[j]}}" for j in range(columnas))
    print(header)
    # Separador
    print(" " * (row_label_width) + "  " + " ".join("-" * col_widths[j] for j in range(columnas)))

    # Filas
    for i in range(filas):
        fila_str = f"{row_labels[i]:>{row_label_width}}  " + " ".join(f"{matrix[i][j]:>{col_widths[j]}.2f}" for j in range(columnas))
        print(fila_str)


# ============================================================================
# SYMBOL FREQUENCY - Frecuencias de símbolos
# ============================================================================



def getOcurrences( phrase: str ) -> dict:
    occurrences = {}

    for si in phrase:
        if not (si in occurrences):
            occurrences[si] = 0
        occurrences[si] += 1
    
    return occurrences

'''
@return dictionary: { letra: porcentaje aparicion } 
'''
def buildS ( source: str ) -> dict:
    occurrences = dict( sorted(getOcurrences( source ).items()) )
    return { si:cant/len(source) for si, cant in occurrences.items() }


# ============================================================================
# MONTECARLO - Simulación Monte Carlo
# ============================================================================


def getMontecarloIntervals( P: list ) -> list:
    last = 0
    result = []

    for pi in P:
        result.append((last, last+pi))
        last = last+pi
        
    return result

def getRandomIndexByInterval(montecarloIntervals: list[tuple]):
    rdm = random.uniform(0, 1)
    i = 0
    while i < len(montecarloIntervals) and not (montecarloIntervals[i][0] <= rdm and rdm <= montecarloIntervals[i][1]):
        i += 1

    return min(i, len(montecarloIntervals)-1)


# ============================================================================
# WARSHALL - Algoritmo de Warshall
# ============================================================================


def initWarshall( matrix: list[list] ) -> list[list[bool]]:
    n = len(matrix)
    reach = getMatrixZeros(n, n)

    for i in range(n):
        for j in range(n):
            reach[i][j] = matrix[i][j] != 0

    return reach

def warshall( matrix: list[list]) -> list[list[bool]]: 
    reach = initWarshall(matrix)
    n = len(matrix)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    
    return reach



# ============================================================================
# FUENTE NULA - Alfabeto y símbolos
# ============================================================================



def getSymbolOcurrences( phrase: str ) -> dict:
    occurrences = {}

    for si in phrase:
        if not (si in occurrences):
            occurrences[si] = 0
        occurrences[si] += 1
    
    return occurrences


# @return dictionary: { letra: porcentaje aparicion } 
def buildS(source: str) -> dict:
    occurrences = getSymbolOcurrences(source)
    frequencies = {symbol: count / len(source) for symbol, count in occurrences.items()}
    
    return dict(sorted(frequencies.items(), key=lambda item: item[0]))


# ============================================================================
# FUENTE NULA - Información
# ============================================================================


# unidades de información: bits (base 2)
def calculateI(pi: float) -> float:
    if pi <= 0:
        raise ValueError("La probabilidad debe ser mayor que 0")

    return math.log2(1/pi); 

# ============================================================================
# FUENTE NULA - Entropía
# ============================================================================


# entropía: H = Σ pi * I(pi)
def calculateH(P: list) -> float:
    return sum([
        pi*calculateI(pi) 
        for pi in P
    ])


# ============================================================================
# FUENTE NULA - Generador de extensiones
# ============================================================================

'''
Se llama extensión de orden n de S o Sn, a una fuente de
memoria nula con un alfabeto de qn símbolos: {o1,o2 ,...,oqn}. Donde el símbolo oi se
corresponde con una secuencia determinada de n símbolos de la fuente S
'''

# extensión de orden n de S (alf: list, prob: list)
def generateExtensionsFromLL(alf: list, prob: list, n: int) -> list:
    if n == 1:
        return alf, prob
    
    P = []
    S = []

    prevS, prevP = generateExtensionsFromLL(alf, prob, n-1)
    
    for i, phrase  in enumerate(prevS):
        for j, symbol in enumerate(alf):
            S.append( phrase + symbol )
            P.append( prevP[i] * prob[j] )
    return S, P 

# extensión de orden n de S (dict)
def generateExtensionsFromD(S: dict, n: int) -> dict:
    Sq, Pq = generateExtensionsFromLL( list(S.keys()), list(S.values()), n )
    return dict(zip(Sq, Pq))

# ============================================================================
# FUENTE NULA - Extensiones de probabilidades
# ============================================================================


def generateExtensionsP(prob: list, n: int) -> list:
    if n == 1:
        return prob
    
    P = []
    prevP = generateExtensionsP(prob, n-1)
    
    for pi  in prob:
        for pj in prevP:
            P.append( pi * pj )
    return P 


# ============================================================================
# FUENTE NULA - Entropía de extensiones
# ============================================================================



def calculateHn(P: list, n: int) -> float:
    return n*calculateH(P)

# ============================================================================
# FUENTE NULA - Simulación
# ============================================================================


def simulateSymbol( symbols: str, intervals: list[tuple] ) -> str:        
    return symbols[ getRandomIndexByInterval(intervals) ]

def simulateFuente( S: dict, iteration: int) -> str:
    intervals = getMontecarloIntervals( list(S.values()) )
    fuente = []

    while (iteration):
        fuente.append( simulateSymbol( list(S.keys()), intervals ) )
        iteration -= 1
    
    return ''.join(fuente)



# ============================================================================
# CÓDIGOS - Información en base r
# ============================================================================


def calculateIr( p: float, r: int ) -> float:
    return math.log(1/p, r)


# ============================================================================
# CÓDIGOS - Entropía en base r
# ============================================================================


def calculateHr( pbs:list, r: int ) -> float:
    return sum([
        pbi * calculateIr(pbi, r)
        for pbi in pbs
    ])


# ============================================================================
# CÓDIGOS - Metadata de códigos
# ============================================================================


def getAlfabetoCodigo (cods: list) -> list:
    alfCod = set()

    for cod in cods:
        alfCod.update(cod)

    return list(alfCod)

def getLengthsCodigo (cods: list) -> list:
    return [ len(cod) for cod in cods ] 

def getLengthMedCodigo(cods: list, pbs: float) -> float:
    l = getLengthsCodigo( cods )

    return sum([
        li * pbi
        for li, pbi in zip(l, pbs)
    ])


# ============================================================================
# CÓDIGOS - Desigualdad de Kraft
# ============================================================================


def kraft( cods: list ):
    r = len( getAlfabetoCodigo(cods) )
    l = getLengthsCodigo( cods )
    
    return sum([
        1/pow(r, li) for li in l
    ]) 

# ============================================================================
# CÓDIGOS - Algoritmo Sardinas-Patterson
# ============================================================================

def getSubfix(code: str, prefix: str):
    return code.replace(prefix, "", 1)

def hasAnyEqual(stack, S: set):
    return S in stack

'''
Sardinas-Patterson algorithm to determine if a code is uniquely decodable.
Input: A set of strings S representing the code.
Output: True if the code is uniquely decodable, False otherwise.
'''
def sardinasPatterson (S: set):
    stack = []
    stack.append( set (S))
    
    while (True):
        Si = set()
        for x in S:
            for y in stack[-1]:
                if x == y:
                    continue
                
                subfix = False
                if x.startswith(y):
                    subfix = getSubfix(x, y)
                elif y.startswith(x):
                    subfix = getSubfix(y, x)
                
                if (subfix):
                    if (subfix in S):
                        return False

                    Si.add(subfix)

        if ( hasAnyEqual(stack, Si) ):     
            return True
        
        stack.append( Si )

# ============================================================================
# CÓDIGOS - Teorema de Shannon
# ============================================================================


def teoremaShannon( C: list, P: list, n: int) -> bool:
    r = len( getAlfabetoCodigo(C) )

    if len(P) < len(C):
        P = generateExtensionsP(P, n)
        if len(P) != len(C):
            RaiseError("La cantidad de probabilidades no coincide con la cantidad de palabras del código")
 
    Lmed = getLengthMedCodigo(C, P)
    nHr = calculateHr(P, r)

    return nHr/n <= Lmed/n and Lmed/n <= nHr/n + 1/n


def teoremaShannonExtending( C: list, P: list, n: int) -> bool:
    r = len( getAlfabetoCodigo(C) )
    Hr = calculateHr(P, r) 

    C, P = generateExtensionsFromLL(C, P, n)

    Lmed = getLengthMedCodigo(C, P)
    

    return Hr <= Lmed/n and Lmed/n <= Hr + 1/n


# ============================================================================
# CÓDIGOS - Propiedades de códigos
# ============================================================================



def hasRepeated(codes: list):
    return len(codes) != len( set(codes) )

def hasSubfixes(codes: list):
    for i, x  in enumerate(codes):
        for j, y  in enumerate(codes): 
            if i != j and y.startswith(x):
                return True

    return False

def isBlock(codes: list):
    return hasRepeated(codes)

def isUniquelyDecodable(codes: list):
    return sardinasPatterson(set(codes))

def isInstantaneous(codes: list):
    return not hasSubfixes(codes)

def isCompacto(C:list, P:list) -> bool:
    if not isInstantaneous(C):
        return False

    r = len(getAlfabetoCodigo(C))
    for ci, pi in zip(C, P):
        if len(ci) > math.ceil(calculateIr(pi, r)):
            return False

    return True

'''
 Si tiene repetidos -> bloque
    Si no tiene prefijos -> instantaneo
        Si es univoco -> univoco
            Si no es univoco -> no-singular
'''
def getPropiedadCodigoStr(codes: list):
    if isBlock(codes):
        return "bloque"
    
    if isInstantaneous(codes):
        return "instantaneo"
    
    if isUniquelyDecodable(codes):
        return "univoco"
    
    return "no-singular"

'''
 Si tiene repetidos -> bloque
     Si no tiene prefijos ^ ∀li <= Ir(pi, r) -> compacto
        Si no tiene prefijos -> instantaneo
            Si es univoco -> univoco
                Si no es univoco -> no-singular
'''
def getFullPropiedadCodigoStr(codes: list, pbs: list):
    if isBlock(codes):
        return "bloque"
    
    if isCompacto(codes, pbs):
        return "compacto"

    if isInstantaneous(codes):
        return "instantaneo"
    
    if isUniquelyDecodable(codes):
        return "univoco"
    
    return "no-singular"

# ============================================================================
# CÓDIGOS - Rendimiento y redundancia
# ============================================================================


def rendimientoCodigo( C: list, P: list):
    H = calculateH(P)
    Lmed = getLengthMedCodigo(C, P)

    return H / Lmed


def redundanciaCodigo( C: list, P: list):
    return 1 - rendimientoCodigo(C, P)

# ============================================================================
# ALGORITMOS - Huffman
# ============================================================================


def initializeHuffman(P: list) -> list:
    result = []
    for i, p in enumerate(P):
        result.append( (p, [i]) )
    return result


def huffmanAlgorithm(result: list, P: list) -> list:

    huffman = initializeHuffman(P)
    huffman.sort(key=lambda x: x[0], reverse=True)

    while len(huffman) > 1:
        (p1, c1) = huffman.pop()
        (p2, c2) = huffman.pop()

        for i in c1:
            result[i] = '0' + result[i]
        for i in c2:
            result[i] = '1' + result[i]

        huffman.append( (p1 + p2, c1 + c2) )
        huffman.sort(key=lambda x: x[0], reverse=True)

    return result

# def huffman(S: list, P: list) -> list:
#     result = [''] * len(S)
#     return huffmanAlgorithm(result, P)

def huffman(P: list) -> list:
    result = [''] * len(P)
    return huffmanAlgorithm(result, P)
    

# ============================================================================
# ALGORITMOS - Shannon-Fano
# ============================================================================

def initializeShannonFano ( P: list ) -> list:
    return sorted([ [pi, i] for i, pi in enumerate(P) ], key=lambda item: item[0], reverse=True)


def propagateSubfix( result: list, P: list[list], fix: str ) -> list:
    for pi, i in P:
        result[i] +=  fix 

def shannonfanoAlgorithm ( result: list, Pindex: list  ):
    if len(Pindex) <= 1:
        return

    # calculate split
    total = sum( [ pi for pi, i in Pindex ]) / 2 

    acum = 0
    lastDif = 1 
    splitLocation = -1


    for i, pi in enumerate(Pindex):
        acum += pi[0]

        if acum >= total:
            if min(lastDif, abs(total - acum)) == lastDif:
                splitLocation = i
            else:
                splitLocation = i + 1
            
            firstPart = Pindex[:splitLocation]
            secondPart = Pindex[splitLocation:]

            propagateSubfix( result, firstPart, '1' )
            propagateSubfix( result, secondPart, '0' )

            shannonfanoAlgorithm( result, firstPart)
            shannonfanoAlgorithm( result, secondPart)

            return
                
        lastDif = total - acum

# def shannonfano( S: list, P: list ) -> list:
#     result = [''] * len(S)
#     Pindex = initializeShannonFano(P)
#     shannonfanoAlgorithm(result, Pindex)
#     return result

def shannonfano(P: list) -> list:
    result = [''] * len(P)
    Pindex = initializeShannonFano(P)
    shannonfanoAlgorithm(result, Pindex)
    return result

# ============================================================================
# ALGORITMOS - RLC (Run Length Coding)
# ============================================================================


def rlc(message: str) -> list[tuple]:
    if not message:
        return []

    result = []
    symbol = message[0]
    amount = 1

    for ch in message[1:]:
        if ch == symbol:
            amount += 1
        else:
            result.append((symbol, amount))
            symbol = ch
            amount = 1

    result.append((symbol, amount))
    return result


# ============================================================================
# ERRORES - Distancia de Hamming
# ============================================================================


def hamming (C: list[str]) -> int:
    
    if len(C) <= 1:
        raise Exception("No hay cantidad de codigos suficientes") 

    _min = []
    for i in range(0, len(C)):
        for j in range(i+1, len(C)):
            if i != j:
                dif_amount = 0 
                for k in range(0, len(C[i])):
                    dif_amount += int(C[i][k] != C[j][k]) 
                _min.append( dif_amount )

    return min( _min )

# ============================================================================
# ERRORES - Métricas de detección/corrección
# ============================================================================


def erroresDetectables( C: list[str] ) -> int:
    return hamming(C) - 1

def erroresCorregibles( C: list[str] ) -> float:
    return (hamming(C) - 1) // 2


# ============================================================================
# ERRORES - Paridad simple
# ============================================================================


def encodeParidad( char: str, par = True ) -> int:
    byte = ord(char)
    print( char + ': ' +  bin(byte) )
    bitAmount = 0
    for i in range(0,8):
        bitAmount += (byte >> i) & 1

    if not par:
        bitAmount += 1

    return (byte << 1) | (bitAmount % 2)

def detectarError( byte: int, par = True ) -> bool:
    bitAmount = 0
    for i in range(0,8):
        bitAmount += (byte >> i) & 1

    if not par:
        bitAmount += 1
        
    return (bitAmount % 2) == 0

# ============================================================================
# ERRORES - Codificación multiparidad
# ============================================================================


def addHorizontalParity(matrix: list, par = True) -> list:
    for i in range(len(matrix)):
        bitAmount = 0 if par else 1
        for j in range(len(matrix[i])):
            bitAmount += matrix[i][j]
        matrix[i].append(bitAmount % 2 )

    return matrix

def addVerticalParity(matrix: list, par = True) -> list:
    parityRow = [-1] * len(matrix[0])

    for j in range(len(matrix[0])):
        bitAmount = 0 if par else 1
        for i in range(len(matrix)):
            bitAmount += matrix[i][j]
        parityRow[j] = bitAmount % 2
    matrix.insert(0, parityRow)

    return matrix

def getMatrixMultiparidad(message: str, par = True ) -> list:
    matrix = getBinMatrixFromStr(message)
    matrix = addHorizontalParity(matrix, par)
    matrix = addVerticalParity(matrix, par)
    return matrix

def encodeMultiparidad( message: str, par = True ) -> bytearray:
    matrix = getMatrixMultiparidad(message, par)
    
    byte_array = bytearray()
    for row in matrix:
        byte = 0
        for bit in row:
            byte = (byte << 1) | bit
        byte_array.append(byte)
    
    return byte_array

# ============================================================================
# ERRORES - Decodificación multiparidad
# ============================================================================




def decodeMultiparidad( byte_array: bytearray, par = True ) -> str:
    matrix = getIntMatrixFromByteArray(byte_array)
    
    print('Matriz recibida:')
    print('rows :', len(matrix))
    print('cols :', len(matrix[0]))
    for row in matrix:
        for bit in row:
            print(bit, end='')
        print()

    if detectarErrorMultiparidad(matrix, par):
        trySolveErrorMultiparidad(matrix, par)


    message = ''
    for i in range(1, len(matrix)):
        char_bits = matrix[i][:-1]  
        char_code = 0
        for bit in char_bits:
            char_code = (char_code << 1) | bit
        message += chr(char_code)
    
    return message


# ============================================================================
# ERRORES - Detección/corrección multiparidad
# ============================================================================


def trackErrorMultiparidad( matrix: list, par = True ) -> list:
    errHorizontal = []
    errVertical = []

    detectCruzada = sum( matrix[0] ) % 2
    paridadGap = 0 if par else 1

    # Verificar paridad horizontal    
    for i in range( len(matrix) ):
        bitAmount = 0
        for j in range( len(matrix[i]) ):
            bitAmount += matrix[i][j]

        if i == len(matrix) and  ((bitAmount + detectCruzada) % 2 == 0):
            errHorizontal.append(i)
        elif ((bitAmount + paridadGap) % 2) != 0:
            errHorizontal.append(i)

    # Verificar paridad vertical
    for j in range(len(matrix[0])):
        bitAmount = 0
        for i in range(len(matrix)):
            bitAmount += matrix[i][j]
   
        if j == len(matrix[0]) and  ((bitAmount + detectCruzada) % 2 == 0):
            errVertical.append(j)
        elif ((bitAmount + paridadGap) % 2) != 0:
            errVertical.append(j)

    return errHorizontal, errVertical  

def detectarErrorMultiparidad( matrix: list, par = True ) -> bool:
    errHorizontal, errVertical = trackErrorMultiparidad(matrix, par)
    return len(errHorizontal) > 0 or len(errVertical) > 0

def trySolveErrorMultiparidad( matrix: list, par = True ) -> bool:
    errHorizontal, errVertical = trackErrorMultiparidad(matrix, par)

    print('[DEBUG] errHorizontal: ', end='')
    print(errHorizontal)
    print('[DEBUG] errVertical: ', end='')
    print(errVertical)

    if len(errHorizontal) != 1 or len(errVertical) != 1:
        raise Exception("No se puede corregir el error")  
    
    row = errHorizontal[0]
    col = errVertical[0]

    if row == 0 and col == len(matrix[0]) - 1:
        raise Exception("No se puede corregir, error en paridad cruzada")  

    if row == 0:
        raise Exception("No se puede corregir, error en paridad horizontal")    

    if col == len(matrix[0]) - 1:
        raise Exception("No se puede corregir, error en paridad vertical")

    matrix[row][col] ^= 1  


# ============================================================================
# CODIFICACIÓN - Huffman/Shannon-Fano
# ============================================================================

def build_C(alf, C):
    """Construye el diccionario símbolo -> código"""
    return dict(zip(alf, C))

def build_byteArray(bits: list) -> bytearray:
    padding = (8 - (len(bits) % 8)) % 8
    bits += [0] * padding

    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for bit in bits[i:i+8]:
            byte = (byte << 1) | bit
        byte_array.append(byte)

    
    byte_array.append(padding)
    return byte_array

def solve_byteArray(bytes: bytearray) -> list:
    if not bytes:
        return []

    padding = bytes[-1]
    data_bytes = bytes[:-1]

    bits = []
    for byte in data_bytes:
        bits.extend([(byte >> i) & 1 for i in range(7, -1, -1)])

    return bits[:-padding]

# ==============================================================
# CODIFICADORES
# ==============================================================

def codificar_dict(message: str, C: dict) -> bytearray:
    """Codifica un mensaje en un bytearray usando un mapa símbolo->código.
    El último byte almacena la cantidad de bits de padding agregados.
    """
    bits = ''.join(C[ch] for ch in message)
    bits = [int(b) for b in bits]

    # print("Códigos posibles:")
    # for simbolo, codigo in C.items():
    #    print(f"  {simbolo!r}: {codigo}")

    # print("\nBits del mensaje:")
    # print(bits)

    return build_byteArray(bits)




def codificar(message: str, alf: list, C: list) -> bytearray:
    """Codifica usando listas paralelas alf y C"""
    C = build_C(alf, C)
    return codificar_dict(message, C)


# ==============================================================
# DECODIFICADORES
# ==============================================================

def decodificar_dict(data: bytearray, C: dict) -> str:
    """Decodifica un bytearray a texto usando un mapa código->simbolo"""

    bits = solve_byteArray( data )
    message = ""
    buffer = ""

    for bit in bits:
        buffer += str(bit)
        if buffer in C:
            message += C[ buffer ]
            buffer = ""

    return message


def decodificar(data: bytearray, C: list, alf: list) -> str:
    """Decodifica usando listas paralelas alf y C"""
    C = build_C(C, alf)
    return decodificar_dict(data, C)


# ============================================================================
# CODIFICACIÓN - RLC
# ============================================================================



def build_byteArray(C: list) -> bytearray:
    byte_array = bytearray()
    for symbol, amount in C:
        byte_array.append(ord(symbol))
        byte_array.append(amount)

    return byte_array

def solve_byteArray(bytes: bytearray) -> list:
    C = []
    for i in range(0, range( bytes ), 2):
        C.append((chr(bytes[i]), bytes[i+1]))
    return C

# ==============================================================
# CODIFICADORES
# ==============================================================

def codificar(message: str) -> bytearray:
    C = rlc( message )
    return build_byteArray(C)


# ==============================================================
# DECODIFICADORES
# ==============================================================

def decodificar(data: bytearray) -> str:
    C = solve_byteArray(data)
    message = ""

    for symb, amount in C:
        message += symb*amount

    return message


# ============================================================================
# CODIFICACIÓN - Guardar/recuperar comprimidos
# ============================================================================


def saveComprimido(bits: bytearray, filename: str, path="compressed_messages/"):
    os.makedirs(path, exist_ok=True)

    fullpath = os.path.join(path, filename)

    with open(fullpath, "wb") as f:
        f.write(bits)

def recoverComprimido(filename: str, path="compressed_messages/") -> bytearray:
    """Recupera un archivo comprimido y lo devuelve como bytearray.
    Lanza FileNotFoundError si el archivo no existe.
    """
    fullpath = os.path.join(path, filename)

    if not os.path.exists(fullpath):
        raise FileNotFoundError(f"No se encontró el archivo comprimido: '{fullpath}'")

    with open(fullpath, "rb") as f:
        data = f.read()

    return bytearray(data)


# ============================================================================
# CODIFICACIÓN - Métricas de compresión
# ============================================================================


def tasaCompresion( message: str, compressed: bytearray) -> float:
    return len( message )/ len( compressed )
 

# ============================================================================
# CANALES - Probabilidades a priori
# ============================================================================


def getProbabilidadPriori( message: str ) -> dict:
    return buildS( message )

def getPrioriMatrixFull(fnt: list, cds: list, _input: str, _output: str) -> list[list]:
    
    result = getMatrixZeros( len(fnt), len(cds) )
    i = 0
    while i < len(_input) and i < len(_output):
        row = fnt.index( _input[i] )
        col = cds.index( _output[i] )

        result[row][col] += 1
        i += 1
        
    for item in result:
        s = sum(item)
        if s > 0:
            for j in range(len(item)):
                item[j] /= s

    return result


def getPrioriMatrixByInputOutput(_input: str, _output: str) -> list[list]:
    inalf = sorted(set(_input))
    outalf = sorted(set(_output))

    return getPrioriMatrixFull(inalf, outalf, _input, _output)

# ============================================================================
# CANALES - Entropía a priori
# ============================================================================


def calculateHPriori( Pa :list ) -> float:
    return calculateH(Pa)


# ============================================================================
# CANALES - Probabilidades a posteriori
# ============================================================================


def getProbsOutSymbols(Pinitial: list, channel: list[list]) -> list:
    result = [0.0] * len(channel[0])
    for j in range(len(channel[0])):
        for i in range(len(channel)):
            result[j] += channel[i][j] * Pinitial[i]
    return result

def getPosterioriMatrix(Pinitial: list, channel: list[list]):
    result = getMatrixZeros(len(channel), len(channel[0]))
    outsSymbProbs = getProbsOutSymbols(Pinitial, channel)
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            result[i][j] = channel[i][j]
            if outsSymbProbs[j] != 0:
                result[i][j] *= Pinitial[i] / outsSymbProbs[j]
    return result

def getMatrixSimultaneusEvent(Pinitial: list, channel: list[list]):
    rows = len(channel)
    cols = len(channel[0])
    result = getMatrixZeros(rows, cols)
    for i in range(rows):
        for j in range(cols):
            result[i][j] = Pinitial[i] * channel[i][j]
    return result

# ============================================================================
# CANALES - Entropía a posteriori
# ============================================================================



def calculateHPosteriori( Pa :list, channel: list[list] ) -> list:
    afterchannel = getPosterioriMatrix(Pa, channel)
    result = []
    for j in range( len(afterchannel[0]) ):
        collectedPbs = []
        for i in range( len(afterchannel) ):
            if afterchannel[i][j] > 0:  
                collectedPbs.append( afterchannel[i][j] )
        result.append( calculateH( collectedPbs ) )
    
    return result



def calculateHPosterioriTotal( Pa :list, channel: list[list] ) -> list:
    return calculateH( getProbsOutSymbols(Pa, channel) )



# ============================================================================
# CANALES - Entropías medias (ruido y pérdida)
# ============================================================================




def calculateHPosterioriMediaAB( Pa :list, channel: list[list] ) -> float:
    Hpost = calculateHPosteriori(Pa, channel)
    Pout = getProbsOutSymbols(Pa,channel)

    result = 0
    for pi, hb in zip(Pout, Hpost):
        result += pi * hb
    
    return result

def calculateHPosterioriMediaABSimple( Pa :list, channel: list[list] ) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    antiChannel = getPosterioriMatrix(Pa, channel)


    result = 0
    for i in range( len(channel) ):
        for j in range( len(channel[0]) ):
            if antiChannel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1/antiChannel[i][j])
    
    return result

def calculateRuido(Pa :list, channel: list[list] ) -> float:
    return calculateHPosterioriMediaABSimple(Pa, channel)

def calculateEquivocacion(Pa :list, channel: list[list] ) -> float:
    return calculateHPosterioriMediaABSimple(Pa, channel)

def calculateHPosterioriMediaBA( Pa :list, channel: list[list] ) -> float:
    antiChannel = getPosterioriMatrix(Pa, channel)
    Pout = getProbsOutSymbols(Pa,channel)

    Hpost = calculateHPosteriori(Pout, getMatrixTraspuesta(antiChannel))
    
    result = 0
    for pi, hb in zip(Pa, Hpost):
        result += pi * hb
    
    return result

def calculateHPosterioriMediaBASimple( Pa :list, channel: list[list] ) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)

    result = 0
    for i in range( len(channel) ):
        for j in range( len(channel[0]) ):
            if channel[i][j] > 0:
                result += simulaneusEvent[i][j] * math.log2(1/channel[i][j])
    
    return result

def calculatePerdida(Pa: list, channel: list[list]):
    return calculateHPosterioriMediaBASimple(Pa, channel)


# ============================================================================
# CANALES - Información mutua
# ============================================================================



def informacionMutuaAB( Pa :list, channel: list[list] ) -> float:
    return calculateHPriori(Pa) -  calculateHPosterioriMediaAB(Pa, channel)

def informacionMutuaABSimple(Pa: list, channel: list[list]) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    outProbs = getProbsOutSymbols(Pa, channel)

    result = 0.0
    for i in range(len(simulaneusEvent)):
        for j in range(len(simulaneusEvent[0])):
            if simulaneusEvent[i][j] > 0 and outProbs[j] > 0 and Pa[i] > 0:
                result += simulaneusEvent[i][j] * math.log2(simulaneusEvent[i][j] / (Pa[i] * outProbs[j]))

    return result

def informacionMutuaBA( Pa :list, channel: list[list] ) -> float:
    outP = getProbsOutSymbols(Pa, channel)
    outChannel = getMatrixTraspuesta(getPosterioriMatrix(Pa, channel))

    Hb = calculateH( outP )
    return Hb - calculateHPosterioriMediaAB(outP, outChannel)
    

def informacionMutuaBASimple(Pa: list, channel: list[list]) -> float:
    # Calcular P(B) y P(A|B)
    antiChannel = getPosterioriMatrix(Pa, channel)  # P(A|B)
    outProbs = getProbsOutSymbols(Pa, channel)      # P(bj)

    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)

    result = 0.0
    for i in range(len(simulaneusEvent)):
        for j in range(len(simulaneusEvent[0])):
            if simulaneusEvent[i][j] > 0 and outProbs[j] > 0 and Pa[i] > 0:
                result += simulaneusEvent[i][j] * math.log2(simulaneusEvent[i][j] / (outProbs[j] * Pa[i]))

    return result

# ============================================================================
# CANALES - Propiedades de canales
# ============================================================================


def isCanalNoRuido (channel : list[list]) -> bool:
    
    for j in range(len(channel[0])):
        amount = 0
        for i in  range(len(channel)):
            amount += int(channel[i][j] != 0)

            if amount > 1:
                return False
    
    return True

def isCanalDeterminante (channel : list[list]) -> bool:
    
    for i in range(len(channel)):
        amount = 0
        for j in  range(len(channel[0])):
            amount += int(channel[i][j] != 0)

            if amount > 1:
                return False
        
        if amount == 0:
            return False
    
    return True

def isCanalSimetricoMariAesteticCoding(channel : list[list]) -> bool:
    acums = {}

    if len(channel) != len(channel[0]):
        return False

    # initialize acums
    for i in range( len(channel[0]) ):
        acums[ channel[0][i] ] = [i]

    if len(acums) != len( channel[0] ):
        return False
    
    for i in range(1, len(channel) ):
        for j in range( len(channel[0]) ):
            pij = channel[i][j]

            if pij not in acums:
                return False
            
            if j not in acums[ pij ]:
                acums[ pij ].append(j)
            else:
                return False
    
    return True


def isCanalSimetrico(channel : list[list]) -> bool:

    if len(channel) != len(channel[0]):
        return False

    for i in range(len(channel)):
        probs       = list(channel[0])
        probsanti   = list(channel[0]) 
        
        for j in range(len(channel[0])):
            if channel[i][j] in probs:
                probs.remove( channel[i][j] )

            if channel[j][i] in probsanti:
                probsanti.remove( channel[j][i] )
        
        if probs or probsanti:
            return False
            
    return True

def isCanalUniforme(channel : list[list]) -> bool:

    for i in range(1, len(channel) ):
        probs = list( channel[0] )

        for j in range( len(channel[0]) ):
            pij = channel[i][j]

            if(pij in probs ):
                probs.remove( pij )

        if probs:
            return False
    
    return True


# ============================================================================
# CANALES - Entropía afín
# ============================================================================



def calculateHCanal( Pa :list, channel: list[list] ) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    result = 0.0

    for row in simulaneusEvent:
        for item in row:
            if item > 0:
                result += item*calculateI(item)

    return result

def calculateHAfinCanal( Pa :list, channel: list[list] ) -> float:
    return calculateHCanal(Pa, channel)

# ============================================================================
# CANALES - Canales en serie y reducción
# ============================================================================



def generarComposedChannel( channelA: list[list], channelB: list[list] ):
    return getMatrixProduct( channelA, channelB )

def isReduccionSuficiente( channel: list[list], col1: int, col2: int ) -> bool:
    const = 0
    tolerance = 1e-5
    isCalculated = False

    # calculate the constant
    i = 0
    while i < len(channel) and not isCalculated:
        if channel[i][col1] == 0 and channel[i][col2] == 0:
            i += 1
            continue
        
        if channel[i][col2] == 0:
            isCalculated = True
            const = 0
        else:
            isCalculated = True
            const = channel[i][col1] / channel[i][col2]
        i += 1
    
    # check const for every row
    for j in range(len(channel)):
        if abs(channel[j][col1] - const*channel[j][col2]) > tolerance:
            return False
    
    return True

def combinateCols(channel: list[list], col1: int, col2: int) -> list[list]:
    for i in range(len(channel)):
        channel[i][col1] += channel[i][col2]
        del channel[i][col2]
    
    return channel

def getCanalDeterminante(channel: list[list], col1: int, col2: int) -> list[list]:
    return getDeterminanteRowDuplicated(channel, col1, col2)

# no tiene limite al momento de reducir ? 
'''
No, lo unico que hago al reducir al canal, es simplificar la cantidad de salidas,
sin embargo, el canal sigue siendo el mismo. 
'''
def getReducedChannel(channel: list[list], squareLimit = False) -> list[list]:
    isReductable = True
    while isReductable and (not squareLimit or len(channel) < len(channel[0])):
        col1 = -1
        col2 = -1

        for i in range(len(channel[0])):
            for j in range(i + 1, len(channel[0])):
                if isReduccionSuficiente(channel, i, j):
                    col1 = i
                    col2 = j
                    break

        if col1 != -1 and col2 != -1:
            determinante = getCanalDeterminante(channel, col1, col2)
            channel = generarComposedChannel(channel, determinante)
        else:
            isReductable = False    

    return channel


# ============================================================================
# CANALES - Capacidad y probabilidad de error
# ============================================================================


def calculateCapacidadNoRuido( channel: list[list]) -> float:
    return math.log2( len(channel) )

def calculateCapacidadDeterminante( channel: list[list] ) -> float:
    return math.log2( len(channel[0]) )

def calculateCapacidadUniforme( channel: list[list] ) -> float:
    log2NroSalida = math.log2( len(channel[0]) )
    amount = 0 

    for pij in channel[0]:
        amount += pij * math.log2(1 / pij) if pij != 0 else 0

    return log2NroSalida - amount

def calcularCapacidad( channel: list[list] ) -> float: 

    if isCanalNoRuido( channel ):
        return calculateCapacidadNoRuido( channel )
    
    if isCanalDeterminante( channel ):
        return calculateCapacidadDeterminante( channel )

    if isCanalUniforme( channel ):
        return calculateCapacidadUniforme( channel )
    

    raise NotImplementedError("No se puede calcular la capacidad con el 'channel' dado")


def calculateCapacidadBinario( channel: list[list], step = 0.0001 ) -> list:
    cPrev = []
    C = -1

    p = 0
    pPrev = []

    while( p < 1 ):
        pPrev = [p, 1 - p]
        currentI = informacionMutuaABSimple(pPrev, channel)

        if currentI > C:
            C = currentI
            cPrev = list(pPrev)
        
        p += step

    return [cPrev[0], C]



def probabilidadError(channel: list[list], P: list[float]) -> float:
    """
    Probabilidad de error bajo la regla ML (máxima posibilidad condicional).
    - channel: matriz cuadrada n x n con P(b|a).
    - P: vector de a priori de tamaño n con P(a_i).
    Pasos:
      1) Para cada fila i, elegir la columna j con valor máximo sin repetir columnas.
      2) Pe = sum_i P[i] * sum_{b != j(i)} P(b|a_i) = sum_i P[i] * (fila_sum_i - channel[i][j(i)]).
         Si cada fila suma 1, Pe = sum_i P[i] * (1 - channel[i][j(i)]).
    """
    if not channel or len(channel) != len(channel[0]):
        raise ValueError("La matriz del canal debe ser cuadrada.")
    n = len(channel)
    if not isinstance(P, (list, tuple)) or len(P) != n:
        raise ValueError("P debe ser un vector de tamaño igual al número de filas del canal.")

    # Asignación ML con columnas únicas
    columnas_tomadas = set()
    asignacion = [-1] * n  # asignacion[i] = columna elegida para la fila i

    for i in range(n):
        # columnas ordenadas por valor descendente en la fila i
        cols_ordenadas = sorted(range(n), key=lambda j: channel[i][j], reverse=True)
        j_elegida = None
        for j in cols_ordenadas:
            if j not in columnas_tomadas:
                j_elegida = j
                break
        if j_elegida is None:
            # Fallback: si todas las columnas estuvieran tomadas (no debería pasar en n x n)
            j_elegida = max(range(n), key=lambda j: channel[i][j])

        asignacion[i] = j_elegida
        columnas_tomadas.add(j_elegida)

    # Pe = sum_i P[i] * (sum_b P(b|a_i) - P(b=j(i)|a_i))
    error = 0.0
    for i, j in enumerate(asignacion):
        fila_sum = sum(channel[i][k] for k in range(n))
        correcto = channel[i][j]
        error += P[i] * (fila_sum - correcto)

    return error


# ============================================================================
# MARKOV - Alfabeto S2
# ============================================================================


def buildS2( source: str ) -> str:
    symbols = sorted(set( source ))
    S = []
    P = []

    for s1 in symbols:
        currentP = []
        for s2 in symbols:
            S.append( s1 + s2 )
            currentP.append( source.count(s1 + s2) )
        
        for pi in currentP:
            P.append( pi/sum(currentP) if sum(currentP) != 0 else 0 )
    
    return dict(zip(S, P))
    

# ============================================================================
# MARKOV - Entropía de fuente markoviana
# ============================================================================


'''
@param: M: matriz de transición (lista de listas)
@param: V: vector estacionario (tupla)
@return: H fuente markoviana
'''
def calculateHFuenteMarkoviana(M :list[list], V: tuple) -> float:
    Mt = getMatrixTraspuesta(M)
    
    result = 0
    for vi, caseA in zip(V, Mt):
        result += vi*sum([
            caseB*calculateI( caseB ) 
            if caseB > 0
            else 0
            for caseB in caseA 
        ])

    return result



# ============================================================================
# MARKOV - Vector estacionario
# ============================================================================

def getErrorTolerancia() -> float:
    return 0.001

def getVEstacionarioInit( n: int ) -> tuple:
    return [1/n] * n 

'''
@param: M: matriz de transición (lista de listas)
@param: V: vector estacionario a calcular (tupla)
'''
def getOperatedVEstacionario(M: list[list], V: tuple) -> tuple:
    return tuple([
        sum([ vi*mij for vi, mij in zip(mi, V)])
        for mi in M       
    ])

def getNormalizedVEstacionario(V: tuple) -> tuple: 
    return tuple( vi /sum(V) for vi in V)


'''
@param: V1: vector estacionario inicial (tupla)
@param: V2: vector estacionario operado (tupla)
@return: máximo delta entre ambos vectores
'''
def getMaxVEstacionarioDelta(V1: tuple, V2: tuple) -> float:
    return max([
        abs(vi - vii)
        for vi, vii in zip(V1, V2)
    ])


'''
@param: M: matriz de transición (lista de listas)
@return: vector estacionario (tupla)
'''
def calculateVEstacionario(M: list[list]) -> tuple:
    V = getVEstacionarioInit( len(M) )

    lastV = V
    V = getOperatedVEstacionario(M, V)

    while getMaxVEstacionarioDelta(V, lastV) > getErrorTolerancia():
        lastV = V
        V = getNormalizedVEstacionario(
            getOperatedVEstacionario(M, V)
        )
    
    return V

# ============================================================================
# MARKOV - Simulación de fuente markoviana
# ============================================================================


'''
Para iniciar, se elige el simbolo con mayor probabilidad de ocurrencia
y luego se elige el siguiente simbolo segun la fila de la matriz de
transicion correspondiente al simbolo anterior.

@param M: Matriz de transicion
@return: Indice de la fila con mayor promedio
'''
def getHighestAvgIndex(M: list[list]) -> int:
    maxAvg = [
        sum(m_row) / len(m_row)
        for m_row in M
    ]

    return maxAvg.index( max(maxAvg) )

def getMontecarlosByColumns(M: list[list]) -> list[list[tuple]]:
    return [
        getMontecarloIntervals(row) 
        for row in getMatrixTraspuesta(M)
    ]

def simulateFuente( M: list[list], S: list , n:int) -> str:
    if n <= 0:
        return ''

    prevIndex = getHighestAvgIndex(M)
    montercarlosByColumn = getMontecarlosByColumns(M)

    fuente = S[prevIndex]
    for _ in range(n-1):
        currentIndex = getRandomIndexByInterval( montercarlosByColumn[prevIndex] )
        fuente += S[currentIndex]
        prevIndex = currentIndex
    
    return fuente


# ============================================================================
# MARKOV - Detección de fuente nula
# ============================================================================


def getMaxProbabilityDelta( P: list ) -> float:
    maxProbabilityDelta = 0

    for pi in P:
        for pj in P:
            probDelta = abs(pi - pj)
            maxProbabilityDelta = max(probDelta, maxProbabilityDelta)

    return maxProbabilityDelta

'''
@param M: Matriz de transicion
@param tolerancia: Tolerancia para considerar fuente nula
'''
def isFuenteNula(M: list[list], tolerancia: float) -> bool:
    
    for P in M:
        if getMaxProbabilityDelta( P ) >= tolerancia:
            return False

    return True


# ============================================================================
# MARKOV - Generación de matriz de transición
# ============================================================================



def generateMatrixTransicion(message: str) -> list[list]:
    symbols = sorted(set( message ))
    n = len(symbols)
    M = getMatrixZeros(n, n)

    sumCols = [0 for _ in range(n)]

    for i in range( len(message) - 1 ):
        col = symbols.index( message[i] )
        row = symbols.index( message[i + 1] )

        M[row][col] += 1
        sumCols[col] += 1

    for j in range(n):
        for i in range(n):
            M[i][j] /= sumCols[j] if sumCols[j] > 0 else 1
    
    return M

# ============================================================================
# MARKOV - Verificación de ergodicidad
# ============================================================================


def isErgodica( M: list[list[float]] ) -> bool:
    reacheable = warshall( getMatrixTraspuesta( M ) )

    for i in range(len(reacheable)):
        for j in range(len(reacheable)):
            if not reacheable[i][j]:
                return False
    return True

def test() -> None:
    matriz = [
        [1/2, 0, 0, 1/2],
        [1/2, 0, 0, 0],
        [0, 1/2, 0, 0],
        [0, 1/2, 1, 1/2],
    ]

    matriz2 = [
        [1/3, 0, 1, 1/2, 0],
        [1/3, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [1/3, 0, 0, 0, 1/2],
        [0, 0, 0, 1/2, 1/2]
    ]

    matriz3 = [
        [1/3, 0, 1, 0], 
        [2/3, 0, 0, 0],
        [0, 4/5, 0, 0],
        [0, 1/5, 0, 1]
    ]

    print(isErgodica(getMatrixTraspuesta(matriz)))
    print(isErgodica(getMatrixTraspuesta(matriz2)))
    print(isErgodica(getMatrixTraspuesta(matriz3)))
