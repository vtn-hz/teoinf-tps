from utils.fuente_nula.fuenteNulaSimulation import simulateFuente, simulateSymbol

def main():
    S = {
        'A': 0.80, 
        'a': 0.05, 
        'b': 0.05, 
        'lorem': 0.10
    }

    fuente = simulateFuente(S, 30)
    print(fuente)

main()