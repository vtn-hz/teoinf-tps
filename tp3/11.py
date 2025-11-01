from utils.codigos.calculateHr import calculateHr
from utils.codigos.metadataCodigo import getAlfabetoCodigo, getLengthsCodigo, getLengthMedCodigo

def main(cods, pbs):

    lmed = getLengthMedCodigo( cods, pbs )

    print( 'h: ',  calculateHr( len(getAlfabetoCodigo(cods)), pbs) )
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

print( 'h: ',  calculateHr( 3, [0.5, 0.25, 0.125, 0.125]) )
print( 'h: ',  calculateHr( 3, [0.333]*2+[0.167]*2) )
