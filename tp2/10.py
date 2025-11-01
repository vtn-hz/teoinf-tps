from utils.fuente_nula.extensiones.extensionGenerator import generateExtensionsFromLL, generateExtensionsFromD

def main():
    S = ['1', '2', '3', '4', '5', '6']
    Sp = [1/6]*6
    n = int( input('n: ') )

    SQ = dict(zip(S, Sp))

    extensions = generateExtensionsFromLL(S, Sp, n)
    extensionsQ = generateExtensionsFromD(SQ, n)

    print(extensionsQ)
    print("\n")

main()