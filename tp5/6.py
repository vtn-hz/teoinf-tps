from utils.canales.posteriori.probs import getProbsOutSymbols, getPosterioriMatrix, getMatrixSimultaneusEvent

def main():
    matrix = [
        [0.4, 0.4, 0.2],
        [0.3, 0.2, 0.5],
        [0.3, 0.4, 0.3]
    ]

    Pinitial = [0.3, 0.3, 0.4]

    outsymb = getProbsOutSymbols(Pinitial, matrix)
    matrixPosteriori = getPosterioriMatrix(Pinitial, matrix)
    simultaneusEvent = getMatrixSimultaneusEvent(Pinitial, matrix)

    print("Probabilidades de símbolos de salida:")
    print(outsymb)
    print()

    print("Matriz de probabilidades a posteriori:")
    for row in matrixPosteriori:
        print(row)
    print()

    print("Matriz de eventos simultáneos:")
    for row in simultaneusEvent:
        print(row)


if __name__ == "__main__":
    main()
