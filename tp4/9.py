exec(open("./utils/codigos/algorithm/shannonfano.py").read())
exec(open("./utils/codigos/algorithm/huffman.py").read())

def main():
    P1 = [ 0.2, 0.2, 0.3, 0.3 ]
    P2 = [ 0.4, 0.25, 0.25, 0.1]

    C1 = shannonfano(P1) 
    L1 = [ len(ci) for ci in C1 ]
    C2 = shannonfano(P2)
    L2 = [ len(ci) for ci in C2 ]

    print('shannon: ')
    print(C1)
    print(L1)
    print(C2)
    print(L2)
    print('----------')

    C1 = shannonfano(P1) 
    L1 = [ len(ci) for ci in C1 ]
    C2 = shannonfano(P2)
    L2 = [ len(ci) for ci in C2 ]


    print('huffman: ')
    print(C1)
    print(L1)
    print(C2)
    print(L2)

main()