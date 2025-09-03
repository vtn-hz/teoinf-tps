
def generateExtensions(alf: list, prob: list, n: int):
    if n == 1:
        return alf, prob
    
    P = []
    S = []

    prevS, prevP = generateExtensions(alf, prob, n-1)
    
    for i, phrase  in enumerate(prevS):
        for j, symbol in enumerate(alf):
            S.append( phrase + symbol )
            P.append( prevP[i] * prob[j] )
    return S, P 

def main():
    S = ['1', '2', '3', '4', '5', '6']
    Sp = [1/6]*6
    n = int( input('n: ') )

    extensions = generateExtensions(S, Sp, n)

    print(dict(zip(extensions[0], extensions[1])))
    print("\n")

main()