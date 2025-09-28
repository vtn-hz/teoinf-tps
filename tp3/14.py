exec(open("./utils/codigos/getPropiedadCodigo.py").read())
exec(open("./utils/codigos/calculateHr.py").read())

def main(cods, pbs):

    lmed = getLengthMedCodigo( cods, pbs )

    print( 'Codigo: ', cods )
    print( ' I(r=', len(getAlfabetoCodigo(cods)) ,') ', [ round(calculateIr( pb, len(getAlfabetoCodigo(cods)) ), 2) for pb in pbs ] )
    print( 'h: ',  calculateHr( pbs, len(getAlfabetoCodigo(cods))) )
    print( 'lmed: ', lmed)
    print( 'Es compacto: ', isCompacto(cods, pbs) )
    print( '--------------------------' )

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
