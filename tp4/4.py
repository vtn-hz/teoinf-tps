exec(open("./utils/fuente_nula/extensiones/extensionGenerator.py").read())
exec(open("./utils/codigos/teoremaShannon.py").read())

def main():
    S = ['1', '0']
    P = [0.8, 0.2]
    n = 3
    Sn, Pn = generateExtensionsFromLL( S, P, n)

    C = ['1', '01', '001', '00001', '000001', '0001', '0000001', '0000000']
    for pn, sn, ci in zip(Pn, Sn, C):
        print(f"{sn}: {round(pn,2)} | {ci}")

   
    if(teoremaShannon(C, P, 3)):
        print("El código C cumple el primer teorema de Shannon")
    else:
        print("El código C no cumple el primer teorema de Shannon")

main()