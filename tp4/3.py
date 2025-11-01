from utils.codigos.teoremaShannon import teoremaShannon, teoremaShannonExtending

def main() -> None:
    C1 = ["11", "010", "00"]
    C2 = ["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111"]
    P1 = [0.5, 0.2, 0.3]

    if(teoremaShannon(C1, P1, 1)):
        print("El código C1 cumple el primer teorema de Shannon")
    else:
        print("El código C1 no cumple el primer teorema de Shannon")

    if(teoremaShannon(C2, P1, 2)):
        print("El código C2 cumple el primer teorema de Shannon")
    else:
        print("El código C2 no cumple el primer teorema de Shannon")

    

main()
