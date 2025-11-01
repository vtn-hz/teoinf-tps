from utils.codigos.getPropiedadCodigo import getPropiedadCodigoStr, getFullPropiedadCodigoStr, isInstantaneous, isUniquelyDecodable, isBlock, isCompacto

def main(val):
    print( getPropiedadCodigoStr(val) )

codigo1 = ["1", "01", "001", "0001"]


main(codigo1)

