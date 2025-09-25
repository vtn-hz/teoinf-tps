exec(open("./utils/codigos/sardinasPatterson.py").read())

def main():
    val = eval( input("S: ") )

    if (sardinasPatterson(val)):
        print("Es univoco")
    else:
        print("No es univoco")

main()