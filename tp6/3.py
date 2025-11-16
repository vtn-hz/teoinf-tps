from utils.canales.canales_serie import generarComposedChannel
from utils.canales.entropy_media import *
from utils.canales.priori.probs import getProbabilidadPriori, getPrioriMatrixFull
from utils.canales.posteriori.probs import getProbsOutSymbols
from utils.canales.informacion_mutua import informacionMutuaABSimple

def printMatrix(title: str, matrix: list[list]) -> None:
    max_width = max(len(f"{elem:.2f}") for row in matrix for elem in row)
    print(title)
    for row in matrix:
        print(" ".join(f"{elem:>{max_width}.2f}" for elem in row))
    print("---------------------")

def main() -> None:

    P = [0.5, 0.5]

    print("Probabilidades de entrada: ", P)

    A = [
        [0.7, 0.0, 0.3, 0.0],
        [0.2, 0.6, 0.0, 0.2]
    ] 

    printMatrix("Matriz de canal A:", A)
    print("Equivocacion: ", calculateEquivocacion([0.5, 0.5], A))
    print("Informacion mutua I(A, B) : ", informacionMutuaABSimple(P, A))
    probsOutA = getProbsOutSymbols(P, A) 
    print("Probabilidades de salida A: ", probsOutA)

    print("---------------------")

    B = [
        [0.9, 0.0, 0.1],
        [0.0, 1.0, 0.0],
        [0.1, 0.1, 0.8],
        [0.0, 0.5, 0.5]
    ]
    
    printMatrix("Matriz de canal B:", B)
    print("Equivocacion: ", calculateEquivocacion(probsOutA, A))
    probsOutB = getProbsOutSymbols(probsOutA, B) 
    print("Probabilidades de salida B: ", probsOutB)
    print("Informacion mutua I(A, B) : ", informacionMutuaABSimple(probsOutA, B))
    

    print("=====================")

    C = generarComposedChannel(A, B)
    printMatrix("Matriz de canal C = A * B:", C)
    print("Equivocacion: ", calculateEquivocacion(P, C))
    probsOutC = getProbsOutSymbols(P, C) 
    print("Probabilidades de salida C: ", probsOutC)
    print("Informacion mutua I(A, B) : ", informacionMutuaABSimple(P, C))
    
main()
