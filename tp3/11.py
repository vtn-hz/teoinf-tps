import math

#a 
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

#b
def getLengths (cods: list) -> list:
    return [ len(cod) for cod in cods ] 

def getLongitudMediaCodigo( pbs: list, cods: list ) -> float:
    l = getLengths( cods )

    return sum([
        pbi * li
        for pbi, li in zip(pbs, l)
    ])

def main(cods, pbs):

    lmed = getLongitudMediaCodigo( pbs, cods )

    print( 'h: ',  calcH( len(getAlfabetoCod(cods)), pbs) )
    print( 'lmed: ', lmed)

codigo7 = ["==", "<", "<=", ">", "=>", "<="]
codigo8 = [")", "[]", "]]", "([", "([])", "([)]"]
codigo9 = ["/", "*", "-", "*", "++", "+-"]
codigo10 = [".,", ";", ",,", ":", "...", ",:;"]

pbs = [0.1, 0.5, 0.1, 0.2, 0.05, 0.05]

main(codigo7, pbs)
main(codigo8, pbs)
main(codigo9, pbs)
main(codigo10, pbs)

print( 'h: ',  calcH( 3, [0.5, 0.25, 0.125, 0.125]) )
print( 'h: ',  calcH( 3, [0.333]*2+[0.167]*2) )
