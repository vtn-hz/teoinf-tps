import os
from utils.canales.canales_serie import combinateCols, getReducedChannel, isReduccionSuficiente, getCanalDeterminante
from utils.canales.informacion_mutua import informacionMutuaABSimple
from utils.canales.posteriori.entropy_media import calculateRuido, calculatePerdida
from utils.canales.propiedades import isCanalNoRuido, isCanalDeterminante
from utils.matrix import printMatrix as originalPrintMatrix

# Modificar la función printMatrix para mostrar solo 2 decimales
def printMatrix(matrix: list[list]) -> None:
    for row in matrix:
        print(" ".join(f"{val:.2f}" for val in row))

def main():
    # Definimos las matrices iniciales
    matrix1 = [
        [0.4, 0.6, 0.0, 0.0],
        [0.0, 0.0, 0.5, 0.5],
        [0.0, 0.0, 0.7, 0.3]
    ]

    matrix2 = [
        [0.2, 0.3, 0.5],
        [0.0, 0.0, 1.0],
        [0.0, 0.0, 1.0]
    ]

    matrix3 = [
        [0.4, 0.0, 0.2, 0.4],
        [0.4, 0.3, 0.2, 0.1],
        [0.0, 0.3, 0.0, 0.7]
    ]

    matrix4 = [
        [0.0, 0.5, 0.0, 0.5],
        [0.8, 0.0, 0.2, 0.0],
        [0.0, 0.5, 0.0, 0.5],
        [0.8, 0.0, 0.2, 0.0]
    ]

    # Diccionario para seleccionar matrices
    matrices = {
        1: matrix1,
        2: matrix2,
        3: matrix3,
        4: matrix4
    }

    # Probabilidades a priori asociadas a cada matriz
    priors = {
        1: [1 / len(matrix1)] * len(matrix1),
        2: [1 / len(matrix2)] * len(matrix2),
        3: [1 / len(matrix3)] * len(matrix3),
        4: [1 / len(matrix4)] * len(matrix4)
    }

    while True:
        os.system('clear')  # Limpiar la pantalla
        print("Estado actual de las matrices:")
        for key, matrix in matrices.items():
            print(f"\nMatriz {key}:")
            printMatrix(matrix)
            print(f"Probabilidades a priori: {[round(p, 2) for p in priors[key]]}")

        print("\nMenú de opciones:")
        print("1. Seleccionar una matriz para trabajar")
        print("0. Salir")

        try:
            option = int(input("\nSeleccione una opción: "))
            if option == 0:
                print("Saliendo del programa...")
                break

            elif option == 1:
                matrix_choice = int(input("\nSeleccione la matriz (1-4): "))
                if matrix_choice not in matrices:
                    print("Selección inválida. Presione Enter para continuar...")
                    input()
                    continue

                while True:
                    os.system('clear')  # Limpiar la pantalla
                    print(f"Trabajando con la Matriz {matrix_choice}:")
                    printMatrix(matrices[matrix_choice])
                    print(f"Probabilidades a priori: {[round(p, 2) for p in priors[matrix_choice]]}")

                    print("\nOpciones para la matriz seleccionada:")
                    print("1. Combinar dos columnas")
                    print("2. Obtener la matriz reducida")
                    print("3. Calcular la información mutua")
                    print("4. Verificar si dos columnas son combinables")
                    print("5. Calcular el determinante para dos columnas")
                    print("6. Mostrar el ruido (H(A|B))")
                    print("7. Mostrar la pérdida (H(B|A))")
                    print("8. Verificar si el canal es sin ruido")
                    print("9. Verificar si el canal es determinante")
                    print("0. Volver al menú principal")

                    try:
                        sub_option = int(input("\nSeleccione una opción: "))
                        if sub_option == 0:
                            break

                        selected_matrix = matrices[matrix_choice]

                        if sub_option == 1:  # Combinar dos columnas
                            col1 = int(input("Seleccione la primera columna (índice comienza en 0): "))
                            col2 = int(input("Seleccione la segunda columna (índice comienza en 0): "))
                            matrices[matrix_choice] = combinateCols(selected_matrix, col1, col2)
                            print(f"Las columnas {col1} y {col2} han sido combinadas.")

                        elif sub_option == 2:  # Obtener la matriz reducida
                            matrices[matrix_choice] = getReducedChannel(selected_matrix)
                            print("\nMatriz reducida:")
                            printMatrix(matrices[matrix_choice])

                        elif sub_option == 3:  # Calcular la información mutua
                            info_mutua = informacionMutuaABSimple(priors[matrix_choice], selected_matrix)
                            print(f"\nInformación mutua: {info_mutua:.2f}")

                        elif sub_option == 4:  # Verificar si dos columnas son combinables
                            col1 = int(input("Seleccione la primera columna (índice comienza en 0): "))
                            col2 = int(input("Seleccione la segunda columna (índice comienza en 0): "))
                            if isReduccionSuficiente(selected_matrix, col1, col2):
                                print(f"Las columnas {col1} y {col2} son combinables.")
                            else:
                                print(f"Las columnas {col1} y {col2} NO son combinables.")

                        elif sub_option == 5:  # Calcular el determinante para dos columnas
                            col1 = int(input("Seleccione la primera columna (índice comienza en 0): "))
                            col2 = int(input("Seleccione la segunda columna (índice comienza en 0): "))
                            determinante = getCanalDeterminante(selected_matrix, col1, col2)
                            print("\nDeterminante calculado:")
                            printMatrix(determinante)

                        elif sub_option == 6:  # Mostrar el ruido (H(A|B))
                            ruido = calculateRuido(priors[matrix_choice], selected_matrix)
                            print("\nFórmula del ruido: H(A|B)")
                            print(f"Ruido calculado: {ruido:.2f}")

                        elif sub_option == 7:  # Mostrar la pérdida (H(B|A))
                            perdida = calculatePerdida(priors[matrix_choice], selected_matrix)
                            print("\nFórmula de la pérdida: H(B|A)")
                            print(f"Pérdida calculada: {perdida:.2f}")

                        elif sub_option == 8:  # Verificar si el canal es sin ruido
                            if isCanalNoRuido(selected_matrix):
                                print("\nEl canal es SIN RUIDO.")
                            else:
                                print("\nEl canal TIENE RUIDO.")

                        elif sub_option == 9:  # Verificar si el canal es determinante
                            if isCanalDeterminante(selected_matrix):
                                print("\nEl canal es DETERMINANTE.")
                            else:
                                print("\nEl canal NO es DETERMINANTE.")

                        else:
                            print("Opción inválida. Presione Enter para continuar...")

                    except ValueError:
                        print("Entrada inválida. Presione Enter para continuar...")

                    input("\nPresione Enter para continuar...")

            else:
                print("Opción inválida. Presione Enter para continuar...")

        except ValueError:
            print("Entrada inválida. Presione Enter para continuar...")

        input("\nPresione Enter para continuar...")

# Llamada al main
if __name__ == "__main__":
    main()