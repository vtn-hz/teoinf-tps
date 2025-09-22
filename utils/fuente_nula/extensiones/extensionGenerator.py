'''
Se llama extensión de orden n de S o Sn, a una fuente de
memoria nula con un alfabeto de qn símbolos: {o1,o2 ,...,oqn}. Donde el símbolo oi se
corresponde con una secuencia determinada de n símbolos de la fuente S
'''

# extensión de orden n de S (alf: list, prob: list)
def generateExtensionsFromLL(alf: list, prob: list, n: int) -> list:
    if n == 1:
        return alf, prob
    
    P = []
    S = []

    prevS, prevP = generateExtensionsFromLL(alf, prob, n-1)
    
    for i, phrase  in enumerate(prevS):
        for j, symbol in enumerate(alf):
            S.append( phrase + symbol )
            P.append( prevP[i] * prob[j] )
    return S, P 

# extensión de orden n de S (dict)
def generateExtensionsFromD(S: dict, n: int) -> dict:
    Sq, Pq = generateExtensionsFromLL( list(S.keys()), list(S.values()), n )
    return dict(zip(Sq, Pq))