exec(open("./utils/fuente_no_nula/fuente_markov/fuenteMarkovSimulation.py").read())

def main():
    M = [ #A  #B  #C
        [0.333, 1, 1], 
        [0.333, 0, 0], 
        [0.333, 0, 0]
    ]

    S = ['A', 'B', 'C']

    print(simulateFuente(M, S, 30))

main()