exec(open("./utils/fuente_no_nula/fuente_markov/calculateHFuenteMarkoviana.py").read())

def main():
    # Matriz de transición
    M = [
        [1/2, 1/3, 0],
        [1/2, 1/3, 1],
        [0,   1/3, 0]
    ]

    # Vector estacionario
    v = (1/3, 1/2, 1/6)

    result = calculateHFuenteMarkoviana(M, v)
    print(result)

main()