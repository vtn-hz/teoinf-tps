exec(open("./utils/fuente_no_nula/fuente_markov/calculateHFuenteMarkoviana.py").read())
exec(open("./utils/fuente_no_nula/fuente_markov/calculateVEstacionario.py").read())

def main():
    matriz = [
        [1/2, 0, 0, 1/2],
        [1/2, 0, 0, 0],
        [0, 1/2, 0, 0],
        [0, 1/2, 1, 1/2],
    ]

    matriz2 = [
        [1/3, 0, 1, 1/2, 0],
        [1/3, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [1/3, 0, 0, 0, 1/2],
        [0, 0, 0, 1/2, 1/2]
    ]


    V = calculateVEstacionario(matriz)
    hmarkov = calculateHFuenteMarkoviana(matriz, V)

    print(V)
    print(hmarkov)

    V = calculateVEstacionario(matriz2)
    hmarkov = calculateHFuenteMarkoviana(matriz2, V)

    print(V)
    print(hmarkov)

    
if __name__ == "__main__":
    main()
