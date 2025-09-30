
import math

def calculateIr( p: float, r: int ) -> float:
    return math.log(1/p, r)

def calculateHr( pbs:list, r: int ) -> float:
    return sum([
        pbi * calculateIr(pbi, r)
        for pbi in pbs
    ])



def getAlfabetoCodigo (cods: list) -> list:
    alfCod = set()

    for cod in cods:
        alfCod.update(cod)

    return list(alfCod)

def getLengthsCodigo (cods: list) -> list:
    return [ len(cod) for cod in cods ] 

def getLengthMedCodigo(cods: list, pbs: float) -> float:
    l = getLengthsCodigo( cods )

    return sum([
        li * pbi
        for li, pbi in zip(l, pbs)
    ])


def hasRepeated(codes: list):
    return len(codes) != len( set(codes) )

def hasSubfixes(codes: list):
    for i, x  in enumerate(codes):
        for j, y  in enumerate(codes): 
            if i != j and y.startswith(x):
                return True

    return False

def isBlock(codes: list):
    return hasRepeated(codes)

def isUniquelyDecodable(codes: list):
    return sardinasPatterson(set(codes))

def isInstantaneous(codes: list):
    return not hasSubfixes(codes)

def isCompacto(C:list, P:list) -> bool:
    if not isInstantaneous(C):
        return False

    r = len(getAlfabetoCodigo(C))
    for ci, pi in zip(C, P):
        if len(ci) > math.ceil(calculateIr(pi, r)):
            return False

    return True

'''
 Si tiene repetidos -> bloque
    Si no tiene prefijos -> instantaneo
        Si es univoco -> univoco
            Si no es univoco -> no-singular
'''
def getPropiedadCodigoStr(codes: list):
    if isBlock(codes):
        return "bloque"
    
    if isInstantaneous(codes):
        return "instantaneo"
    
    if isUniquelyDecodable(codes):
        return "univoco"
    
    return "no-singular"

'''
 Si tiene repetidos -> bloque
     Si no tiene prefijos ^ ∀li <= Ir(pi, r) -> compacto
        Si no tiene prefijos -> instantaneo
            Si es univoco -> univoco
                Si no es univoco -> no-singular
'''
def getFullPropiedadCodigoStr(codes: list, pbs: list):
    if isBlock(codes):
        return "bloque"
    
    if isCompacto(codes, pbs):
        return "compacto"

    if isInstantaneous(codes):
        return "instantaneo"
    
    if isUniquelyDecodable(codes):
        return "univoco"
    
    return "no-singular"

def kraft( cods: list ):
    r = len( getAlfabetoCodigo(cods) )
    l = getLengthsCodigo( cods )
    
    return sum([
        1/pow(r, li) for li in l
    ])


def getSubfix(code: str, prefix: str):
    return code.replace(prefix, "", 1)

def hasAnyEqual(stack, S: set):
    return S in stack

'''
Sardinas-Patterson algorithm to determine if a code is uniquely decodable.
Input: A set of strings S representing the code.
Output: True if the code is uniquely decodable, False otherwise.
'''
def sardinasPatterson (S: set):
    stack = []
    stack.append( set (S))
    
    while (True):
        Si = set()
        for x in S:
            for y in stack[-1]:
                if x == y:
                    continue
                
                subfix = False
                if x.startswith(y):
                    subfix = getSubfix(x, y)
                elif y.startswith(x):
                    subfix = getSubfix(y, x)
                
                if (subfix):
                    if (subfix in S):
                        return False

                    Si.add(subfix)

        if ( hasAnyEqual(stack, Si) ):     
            return True
        
        stack.append( Si )

def main():

    pbs = [ 0.15, 0.25, 0.05, 0.45, 0.1 ]
    cods = ['])', '(', ')[', '[', '(]']

    lmed = getLengthMedCodigo( cods, pbs )

    

    print( 'h: ',  calculateHr( pbs, len(getAlfabetoCodigo(cods))) )    
    print( 'lmed: ', lmed)
    print('kraft: ', kraft(cods))
    print( getFullPropiedadCodigoStr(cods, pbs) )


    pbs = [ 0.15, 0.25, 0.05, 0.45, 0.1 ]
    cods = ['(]', ']', '[)', ')', '([']

    lmed = getLengthMedCodigo( cods, pbs )

    

    print( 'h: ',  calculateHr( pbs, len(getAlfabetoCodigo(cods))) )    
    print( 'lmed: ', lmed)
    print('kraft: ', kraft(cods))
    print( getFullPropiedadCodigoStr(cods, pbs) )
    
main()

# Fuente 	Probs 	Código
# S1 	0.15 	])
# S2 	0.25 	(
# S3 	0.05 	)[
# S4 	0.45 	[
# S5 	0.10 	(]

# Fuente 	Probs 	Código
# S1 	0.15 	(]
# S2 	0.25 	]
# S3 	0.05 	[)
# S4 	0.45 	)
# S5 	0.10 	([