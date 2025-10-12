exec(open("./utils/codigos/algorithm/rlc.py").read())


def printRlc( C: list ):
    coded = ""
    for symbol, amount in C:
        coded += symbol+str(amount) 
    
    print(coded)

def main():
    message1 = "XXXYZZZZ"
    message2 = "AAAABBBCCDAA"
    message3 = "UUOOOOAAAIEUUUU"

    coded1 = rlc( message1 )
    coded2 = rlc( message2 )
    coded3 = rlc( message3 )

    printRlc( coded1 )
    printRlc( coded2 )
    printRlc( coded3 )

main()