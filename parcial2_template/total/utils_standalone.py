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


def buildS ( source: str ) -> dict:
    occurrences = dict( sorted(getOcurrences( source ).items()) )
    return { si:cant/len(source) for si, cant in occurrences.items() }


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


def calculateI(pi: float) -> float:
    if pi <= 0:
        raise ValueError("La probabilidad debe ser mayor que 0")

    return math.log2(1/pi); 

def calculateH(P: list) -> float:
    return sum([
        pi*calculateI(pi) 
        for pi in P
    ])


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

def generateExtensionsP(prob: list, n: int) -> list:
    if n == 1:
        return prob
    
    P = []
    prevP = generateExtensionsP(prob, n-1)
    
    for pi  in prob:
        for pj in prevP:
            P.append( pi * pj )
    return P 


def calculateIr( p: float, r: int ) -> float:
    return math.log(1/p, r)


def calculateHr( pbs:list, r: int ) -> float:
    return sum([
        pbi * calculateIr(pbi, r)
        for pbi in pbs
    ])


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


def rendimientoCodigo( C: list, P: list):
    H = calculateH(P)
    Lmed = getLengthMedCodigo(C, P)

    return H / Lmed



def redundanciaCodigo( C: list, P: list):
    return 1 - rendimientoCodigo(C, P)

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

def erroresDetectables( C: list[str] ) -> int:
    return hamming(C) - 1


def erroresCorregibles( C: list[str] ) -> float:
    return (hamming(C) - 1) // 2


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

def codificar(message: str) -> bytearray:
    C = rlc( message )
    return build_byteArray(C)


def decodificar(data: bytearray) -> str:
    C = solve_byteArray(data)
    message = ""

    for symb, amount in C:
        message += symb*amount

    return message


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


def tasaCompresion( message: str, compressed: bytearray) -> float:
    return len( message )/ len( compressed )
 

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



def calculateHPriori( Pa :list ) -> float:
    return calculateH(Pa)


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


def informacionMutuaABSimple(Pa: list, channel: list[list]) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    outProbs = getProbsOutSymbols(Pa, channel)

    result = 0.0
    for i in range(len(simulaneusEvent)):
        for j in range(len(simulaneusEvent[0])):
            if simulaneusEvent[i][j] > 0 and outProbs[j] > 0 and Pa[i] > 0:
                result += simulaneusEvent[i][j] * math.log2(simulaneusEvent[i][j] / (Pa[i] * outProbs[j]))

    return result


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


def calculateHCanal( Pa :list, channel: list[list] ) -> float:
    simulaneusEvent = getMatrixSimultaneusEvent(Pa, channel)
    result = 0.0

    for row in simulaneusEvent:
        for item in row:
            if item > 0:
                result += item*calculateI(item)

    return result


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



