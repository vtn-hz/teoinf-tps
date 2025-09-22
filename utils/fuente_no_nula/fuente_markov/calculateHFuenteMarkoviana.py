exec(open("./utils/fuente_nula/calculateI.py").read())
exec(open("./utils/matrix.py").read())

'''
@param: M: matriz de transición (lista de listas)
@param: V: vector estacionario (tupla)
@return: H fuente markoviana
'''
def calculateHFuenteMarkoviana(M :list[list], V: tuple) -> float:
    Mt = getMatrixTraspuesta(M)
    
    result = 0
    for vi, caseA in zip(V, Mt):
        result += vi*sum([
            caseB*calculateI( caseB ) 
            if caseB > 0
            else 0
            for caseB in caseA 
        ])

    return result

