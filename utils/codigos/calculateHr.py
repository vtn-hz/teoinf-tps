exec(open("./utils/codigos/calculateIr.py").read())

def calculateHr( pbs:list, r: int ) -> float:
    return sum([
        pbi * calculateIr(pbi, r)
        for pbi in pbs
    ])
