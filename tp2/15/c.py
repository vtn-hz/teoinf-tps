from utils.fuente_no_nula.fuente_markov.fuenteNulaDetection import isFuenteNula

def main():
    M = [
        [0.43, 0.43, 0.43],
        [0.535, 0.53, 0.53],
        [0.6, 0.6, 0.6]
    ]

    T = 0.006

    print( isFuenteNula(M, T) )

main()