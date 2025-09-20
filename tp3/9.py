
# a
def getAlfabetoCod (cods: list) -> list:
    alfCod = set()

    for cod in cods:
        alfCod.update(cod)

    return list(alfCod)

# b 
def getLengths (cods: list) -> list:
    return [ len(cod) for cod in cods ] 

# c 
def kraft( cods: list ):
    r = len( getAlfabetoCod(cods) )
    l = getLengths( cods )
    
    return sum([
        1/pow(r, li) for li in l
    ]) 

def main(cods):
    # cods = ['AA', 'C', 'B', 'AB', 'ACB']
    print( getAlfabetoCod(cods) )
    print( getLengths(cods) )
    print( kraft(cods) )
