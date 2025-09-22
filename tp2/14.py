exec(open("./utils/fuente_no_nula/fuente_markov/calculateHFuenteMarkoviana.py").read())
exec(open("./utils/fuente_no_nula/fuente_markov/calculateVEstacionario.py").read())

def main():
    M = [
        [0.58, 0.43, 0.3],
        [0.17, 0.43, 0.1],
        [0.25, 0.14, 0.6]
    ]

    V = calculateVEstacionario(M)

    print( V )
    print( calculateHFuenteMarkoviana(M, V) )
    
main()