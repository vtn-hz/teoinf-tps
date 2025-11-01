from utils.matrix import getMatrixZeros
from utils.symbolFrequency import buildS

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


def getPrioriMatrixJust(_input: str, _output: str) -> list[list]:
    # original implementation to be copied from repo if needed
    raise NotImplementedError