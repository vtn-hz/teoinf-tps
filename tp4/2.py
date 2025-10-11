exec(open("./utils/codigos/teoremaShannon.py").read())
exec(open("./utils/fuente_nula/extensiones/extensionGenerator.py").read())

def main() -> None:
    P = [0.3, 0.1 , 0.4, 0.2]
    C = ['BA', 'CAB', 'A', 'CBA']
    n = 2

    print(
        "cumple primer teorema shannon" if teoremaShannonExtending(C, P, n-1)
        else "no cumple primer teorema shannon"
    )


    print(
        "cumple primer teorema shannon" if teoremaShannonExtending(C, P, n)
        else "no cumple primer teorema shannon"
    )



main()