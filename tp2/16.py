exec(open("./utils/fuente_no_nula/fuente_markov/generateMatrixTransicion.py").read())
exec(open("./utils/fuente_no_nula/fuente_markov/fuenteNulaDetection.py").read())


exec(open("./utils/fuente_no_nula/fuente_markov/calculateHFuenteMarkoviana.py").read())
exec(open("./utils/fuente_no_nula/fuente_markov/calculateVEstacionario.py").read())

exec(open("./utils/fuente_nula/calculateH.py").read())
exec(open("./utils/fuente_nula/alfabetoS.py").read())


def getHBytipoFuente( message:str, M: list[list], isNula: bool):
    

    if isNula:
        S = buildS(message)
        P = list(S.values())
        H = calculateH(P)
        tipo = "nula"
    else:
        V = calculateVEstacionario( M )
        H = calculateHFuenteMarkoviana(M, V)
        tipo = "markoviana"

    return H, tipo
    
def main():
    message = input("mensaje: ")
    tolerancia = 0.1

    M = generateMatrixTransicion(message)
    isNula = isFuenteNula(M, tolerancia)

    print( "Matriz de transición:" )
    for row in M:
        print(row)


    H, tipo = getHBytipoFuente(message, M, True)
    print(f"Fuente {tipo} con entropía H = {H}")


    H, tipo = getHBytipoFuente(message, M, False)
    print(f"Fuente {tipo} con entropía H = {H}")

main()