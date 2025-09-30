exec(open("./utils/warshall.py").read())
exec(open("./utils/matrix.py").read())

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
