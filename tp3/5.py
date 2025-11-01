from utils.codigos.sardinasPatterson import sardinasPatterson

def main():
    val = eval( input("S: ") )

    if (sardinasPatterson(val)):
        print("Es univoco")
    else:
        print("No es univoco")

main()