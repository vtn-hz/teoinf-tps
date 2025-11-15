from utils.canales.metricas import *

def main(matrix): 
    print( calculateCapacidadBinario(matrix) )


matrixes = [
    [[0.60, 0.40],
     [0.20, 0.80]],
    
    [[0.25, 0.75],
     [0.90, 0.10]],
    
    [[0.51, 0.49],
     [0.72, 0.28]],
    
    [[0.77, 0.23],
     [0.20, 0.80]]
]

main( matrixes[0] )
main( matrixes[1] )
main( matrixes[2] )
main( matrixes[3] )