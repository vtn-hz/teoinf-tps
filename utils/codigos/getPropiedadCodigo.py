import math

exec(open("./utils/codigos/calculateIr.py").read())
exec(open("./utils/codigos/metadataCodigo.py").read())

exec(open("./utils/codigos/sardinasPatterson.py").read())

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