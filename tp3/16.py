exec(open("./utils/fuente_nula/fuenteNulaSimulation.py").read())


def main():
    C = [ ci.strip()        for ci in input('C: ').split(',') ]
    P = [ float(pi.strip()) for pi in input('P: ').split(',') ]
    iterations = int( input("iterations: ") )

    code = simulateFuente( dict(zip(C, P)), iterations )
    
    print(code)
        
main()  