from utils.codigos.metadataCodigo import getAlfabetoCodigo, getLengthsCodigo

def kraft( cods: list ):
    r = len( getAlfabetoCodigo(cods) )
    l = getLengthsCodigo( cods )
    
    return sum([
        1/pow(r, li) for li in l
    ]) 