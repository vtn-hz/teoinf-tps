exec(open("utils/canales/priori/probs.py").read())
exec(open("utils/canales/posteriori/probs.py").read())

def showS( S: dict ):
    for symb, percent in S.items():
        print(f'P({symb}): {round(percent, 2)}')

def showMatrixCanal(S, C, mts: list[list]):
    # Determinar el ancho máximo necesario para alinear todo
    max_val_len = max(
        len(str(round(v, 2))) 
        for row in mts for v in row
    )
    max_label_len = max(max(map(len, S)), max(map(len, C)))
    cell_width = max(max_val_len, max_label_len) + 2  # +2 por margen visual

    # Encabezado de columnas
    print(" " * (max_label_len + 2), end="")
    for ci in C:
        print(f"{ci:>{cell_width}}", end="")
    print()

    # Filas
    for i, row in enumerate(mts):
        print(f"{S[i]:<{max_label_len + 2}}", end="")  # etiqueta fila
        for val in row:
            print(f"{round(val, 2):>{cell_width}}", end="")
        print()

def main(message, output):
    print('---------------------------------')
    print(message)
    print(output)

    print('- before channel -')
    priori = getProbabilidadPriori( message )
    showS( priori )
    matrixcanal = getPrioriMatrixJust( message, output ) 
    showMatrixCanal( sorted(set(message)), sorted(set(output)), matrixcanal )

    print('- after channel -')

    print(getProbsOutSymbols(list(priori.values()), matrixcanal))

    matrixPosteriori = getPosterioriMatrix( list(priori.values()), matrixcanal)
    showMatrixCanal( sorted(set(message)), sorted(set(output)), matrixPosteriori )

    matrixsimul = getMatrixSimultaneusEvent(list(priori.values()), matrixcanal)
    showMatrixCanal( sorted(set(message)), sorted(set(output)), matrixsimul )


main('1101011001101010010101010100011111', '1001111111100011101101010111110110')
main('110101100110101100110101100111110011', '110021102110022010220121122100112011')


    

    