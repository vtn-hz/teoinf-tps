
def getMaxRowGap( row: list) -> float:
    _max = 0
    n = len(row)
    for i in range(n):
        for j in range(i+1, n):
            res = abs(row[i] - row[j])
            _max = res if res > _max else _max

    return _max

def isFuenteNula(M: list[list], T: float) -> bool:  
    result = True
    i = 0

    while result and i < len(M):
        result = getMaxRowGap(list(M[i])) < T
        i += 1

    return result

def main():
    M = [
        [0.43, 0.43, 0.43],
        [0.50, 0.53, 0.51],
        [0.6, 0.6, 0.6]
    ]

    T = 0.01

    print( isFuenteNula(M, T) )

main()