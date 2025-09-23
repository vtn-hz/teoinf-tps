
def getMatrixTraspuesta(M: list[list]) -> list[list]:
    result = []
    for i in range(len(M[0])):
        result.append([])  
        for j in range(len(M)):
            result[i].append(M[j][i])  
    return result

def getMatrixZeros(filas: int, columnas: int) -> list[list[int]]:
    return [[0 for _ in range(columnas)] for _ in range(filas)]

