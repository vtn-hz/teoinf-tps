exec(open("./utils/codigos/metadataCodigo.py").read())

def kraft( cods: list ):
    r = len( getAlfabetoCodigo(cods) )
    l = getLengthsCodigo( cods )
    
    return sum([
        1/pow(r, li) for li in l
    ]) 