from utils.matrix import *


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
que pasa si quiero reducir mas alla de una matriz cuadrada?
entrarian por ejemplo 3 simbolos y sadrian 2, como esto puede ser
rentable al momento de transmitir informacion?

el receptor no sabe que simbolo se envio si hay mas simbolos de entrada que de salida
entonces no tiene sentido reducir mas alla de una matriz cuadrada

preguntar!
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