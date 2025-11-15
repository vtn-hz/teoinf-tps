from utils.canales.propiedades import *

def main():
    print("Matrix: ")
    matrix = [
        [1/3, 1/6, 1/2],
        [1/3, 1/6, 1/2]
    ]

    print( isCanalSimetrico(matrix) )
    print( isCanalUniforme(matrix) )

main()