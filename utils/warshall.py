exec(open("./utils/matrix.py").read())

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

