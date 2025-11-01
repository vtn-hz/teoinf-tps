from utils.codigos.calculateIr import calculateIr

def calculateHr( pbs:list, r: int ) -> float:
    return sum([
        pbi * calculateIr(pbi, r)
        for pbi in pbs
    ])
