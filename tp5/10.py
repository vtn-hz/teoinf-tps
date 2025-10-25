exec(open("utils/canales/posteriori/probs.py").read())
exec(open("utils/canales/priori/entropy.py").read())
exec(open("utils/canales/posteriori/entropy.py").read())



def main():
    matrix = [
        [0.4, 0.4, 0.2],
        [0.3, 0.2, 0.5],
        [0.3, 0.4, 0.3]
    ]

    Pinitial = [0.3, 0.3, 0.4]

    # --- Identificación y llamado de funciones ---

    print("Llamando a: getProbsOutSymbols (de probs.py)")
    outsymb = getProbsOutSymbols(Pinitial, matrix)

    print("Llamando a: getPosterioriMatrix (de probs.py)")
    matrixPosteriori = getPosterioriMatrix(Pinitial, matrix)

    print("Llamando a: getMatrixSimultaneusEvent (de probs.py)")
    simultaneusEvent = getMatrixSimultaneusEvent(Pinitial, matrix)

    print("Llamando a: calculateHPriori (de priori/entropy.py)")
    h_priori = calculateHPriori(Pinitial) # Asumo que calcula H(X)

    print("Llamando a: calculateHPosteriori (de posteriori/entropy.py)")
    h_posteriori = calculateHPosteriori(Pinitial, matrix) # Asumo que calcula H(Y|X)

    print("\n--- RESULTADOS ---")

    print("Probabilidades de símbolos de salida:")
    print(outsymb)
    print()

    print("Matriz de probabilidades a posteriori:")
    for row in matrixPosteriori:
        print(row)
    print()

    print("Matriz de eventos simultáneos:")
    for row in simultaneusEvent:
        print(row)
    print()
    
    print("Entropía a priori H(X):")
    print(h_priori)
    print()

    print("Equivocación (Ruido) H(Y|X):")
    print(h_posteriori)
    print()


if __name__ == "__main__":
    main()