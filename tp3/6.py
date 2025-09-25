exec(open("./utils/codigos/getPropiedadCodigo.py").read())

def main(val):
    print( getPropiedadCodigoStr(val) )

codigo1 = ["1", "01", "001", "0001"]


main(codigo1)

