import math

def hasSubfixes(codes: list):
    for i, x in enumerate(codes):
        for j, y in enumerate(codes): 
            if i != j and y.startswith(x):
                return True

    return False

def getLengths (cods: list) -> list:
    return [ len(cod) for cod in cods ] 

def getLongitudMediaCodigo( pbs: list, cods: list ) -> float:
    l = getLengths( cods )

    return sum([
        pbi * li
        for pbi, li in zip(pbs, l)
    ])

def getAlfabetoCod (cods: list) -> list:
    alfCod = set()

    for cod in cods:
        alfCod.update(cod)

    return list(alfCod)


def calcH( r: int, pbs:list ) -> float:
    return sum([
        pbi * math.log(1/pbi, r)
        for pbi in pbs
    ])

def calculateI( p:list, r: int ) -> float:
    return math.log(1/p, r)

def isCompacto(C:list, P:list) -> bool:
    if hasSubfixes(C):
        return False

    r = len(getAlfabetoCod(C))
    for ci, pi in zip(C, P):
        if len(ci) > math.ceil(calculateI(pi, r)):
            return False

    return True

def main(cods, pbs):

    lmed = getLongitudMediaCodigo( pbs, cods )

    print( 'h: ',  calcH( len(getAlfabetoCod(cods)), pbs) )
    print( 'lmed: ', lmed)
    print( 'Es compacto: ', isCompacto(cods, pbs) )

codigo7 = ["==", "<", "<=", ">", "=>", "<="]
codigo8 = [")", "[]", "]]", "([", "([])", "([)]"]
codigo9 = ["/", "*", "-", "*", "++", "+-"]
codigo10 = [".,", ";", ",,", ":", "...", ",:;"]

pbs = [0.1, 0.5, 0.1, 0.2, 0.05, 0.05]

main(codigo7, pbs)
main(codigo8, pbs)
main(codigo9, pbs)
main(codigo10, pbs)

pbs = [ 0.13, 0.34, 0.37, 0.12, 0.04 ]
codigoX2 = ['B', 'CB', 'A', 'CC', 'CA']
codigoX3 = ['AA', 'C', 'B', 'AB', 'ACB']

main(codigoX2, pbs)
main(codigoX3, pbs)
