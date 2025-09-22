exec(open("./utils/fuente_no_nula/fuente_markov/generateMatrixTransicion.py").read())
exec(open("./utils/fuente_nula/alfabetoS.py").read())
exec(open("./utils/fuente_no_nula/fuente_markov/alfabetoS2.py").read())


def main():
    _str = "AABBAABACAACCCCAA"

    print(buildS(_str))
    print(buildS2(_str))
    print(generateMatrixTransicion(_str))

main()