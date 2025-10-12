exec(open("./utils/codificacion/rlc/decode_encode.py").read())
exec(open("./utils/codificacion/metricas.py").read())


def main():
    message1 = "XXXYZZZZ"
    message2 = "AAAABBBCCDAA"
    message3 = "UUOOOOAAAIEUUUU"

    encode1 = codificar( message1 )
    encode2 = codificar( message2 )
    encode3 = codificar( message3 )

    print(tasaCompresion(message1, encode1))
    print(tasaCompresion(message2, encode2))
    print(tasaCompresion(message3, encode3))

main()