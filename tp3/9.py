exec(open("./utils/codigos/kraft.py").read())

def main(cods):
    # cods = ['AA', 'C', 'B', 'AB', 'ACB']
    print( cods )
    print( getAlfabetoCodigo(cods) )
    print( getLengthsCodigo(cods) )
    print( kraft(cods) )
    print( '---------' )

codigo1 = ["011", "000", "010", "101", "111", "100"]
codigo2 = ["110", "100", "101", "001", "110", "010"]
codigo3 = ["10", "1100", "0101", "1011", "0", "110"]
codigo4 = ["1101", "10", "1111", "1100", "11111", "0"]
codigo5 = ["011", "0111", "01", "0", "011111", "01111"]
codigo6 = ["1110", "0", "110", "1101", "1011", "10"]

codigo7 = ["==", "<", "]", ">", "=>", "<="]
codigo8 = [")", "[]", "|", "([", "([])", "([)]"]
codigo9 = ["/", "*", "-", "*", "++", "+-"]
codigo10 = [".,", ";", ",,", ":", "...", ",:;"]


main(codigo1)
main(codigo2)
main(codigo3)
main(codigo4)
main(codigo5)
main(codigo6)
main(codigo7)
main(codigo8)
main(codigo9)
main(codigo10)
