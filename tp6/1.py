from utils.canales.propiedades import *
from utils.canales.informacion_mutua import *
from utils.canales.entropy_media import *
    
def main(matrix: list) -> None:
    print("Contenido de la matriz recibida:")
    for fila in matrix:
        print(fila)

    if (not isCanalNoRuido(matrix)):
        print("- Tiene ruido")
    else:
        print("- No tiene ruido")

    if (isCanalDeterminante(matrix)):
        print("- Es determinante")
    else:
        print("- No es determinante")

    print( '[RUIDO]     H(A/B): ', calculateRuido([1/len(matrix)]*len(matrix), matrix) ) 
    print( '[PERDIDA]   H(B/A): ', calculatePerdida([1/len(matrix)]*len(matrix), matrix) ) 
    print( '[INFORMACION MUTUA] I(A, B): ', informacionMutuaAB([1/len(matrix)]*len(matrix), matrix))
    print("-------------------------")

if __name__ == "__main__":
    
    # Definición de las matrices fuera del main
    matriz_1 = [
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [0.0, 1.0, 0.0],
        [1.0, 0.0, 0.0]
    ]

    matriz_2 = [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 0.2, 0.0, 0.8],
        [0.0, 0.0, 1.0, 0.0]
    ]

    matriz_3 = [
        [0.3, 0.5, 0.2],
        [0.2, 0.3, 0.5],
        [0.5, 0.2, 0.3]
    ]

    matriz_4 = [
        [0.0, 0.0, 1.0, 0.0],
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ]
    
    # Llamadas individuales al main, inyectando cada matriz
    main(matriz_1)
    main(matriz_2)
    main(matriz_3) 
    main(matriz_4) 