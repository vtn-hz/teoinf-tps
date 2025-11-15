import math 
from utils.canales.propiedades import * 
from utils.canales.informacion_mutua import informacionMutuaABSimple

def calculateCapacidadNoRuido( channel: list[list]) -> float:
    return math.log2( len(channel) )

def calculateCapacidadDeterminante( channel: list[list] ) -> float:
    return math.log2( len(channel[0]) )

def calculateCapacidadUniforme( channel: list[list] ) -> float:
    log2NroSalida = math.log2( len(channel[0]) )
    amount = 0 

    for pij in channel[0]:
        amount += pij * math.log2(1 / pij) if pij != 0 else 0

    return log2NroSalida - amount

def calcularCapacidad( channel: list[list] ) -> float: 

    if isCanalNoRuido( channel ):
        return calculateCapacidadNoRuido( channel )
    
    if isCanalDeterminante( channel ):
        return calculateCapacidadDeterminante( channel )

    if isCanalUniforme( channel ):
        return calculateCapacidadUniforme( channel )
    

    raise NotImplementedError("No se puede calcular la capacidad con el 'channel' dado")


def calculateCapacidadBinario( channel: list[list], step = 0.0001 ) -> list:
    cPrev = []
    C = -1

    p = 0
    pPrev = []

    while( p < 1 ):
        pPrev = [p, 1 - p]
        currentI = informacionMutuaABSimple(pPrev, channel)

        if currentI > C:
            C = currentI
            cPrev = list(pPrev)
        
        p += step

    return [cPrev[0], C]



def probabilidadError(channel: list[list], P: list[float]) -> float:
    """
    Probabilidad de error bajo la regla ML (máxima posibilidad condicional).
    - channel: matriz cuadrada n x n con P(b|a).
    - P: vector de a priori de tamaño n con P(a_i).
    Pasos:
      1) Para cada fila i, elegir la columna j con valor máximo sin repetir columnas.
      2) Pe = sum_i P[i] * sum_{b != j(i)} P(b|a_i) = sum_i P[i] * (fila_sum_i - channel[i][j(i)]).
         Si cada fila suma 1, Pe = sum_i P[i] * (1 - channel[i][j(i)]).
    """
    if not channel or len(channel) != len(channel[0]):
        raise ValueError("La matriz del canal debe ser cuadrada.")
    n = len(channel)
    if not isinstance(P, (list, tuple)) or len(P) != n:
        raise ValueError("P debe ser un vector de tamaño igual al número de filas del canal.")

    # Asignación ML con columnas únicas
    columnas_tomadas = set()
    asignacion = [-1] * n  # asignacion[i] = columna elegida para la fila i

    for i in range(n):
        # columnas ordenadas por valor descendente en la fila i
        cols_ordenadas = sorted(range(n), key=lambda j: channel[i][j], reverse=True)
        j_elegida = None
        for j in cols_ordenadas:
            if j not in columnas_tomadas:
                j_elegida = j
                break
        if j_elegida is None:
            # Fallback: si todas las columnas estuvieran tomadas (no debería pasar en n x n)
            j_elegida = max(range(n), key=lambda j: channel[i][j])

        asignacion[i] = j_elegida
        columnas_tomadas.add(j_elegida)

    # Pe = sum_i P[i] * (sum_b P(b|a_i) - P(b=j(i)|a_i))
    error = 0.0
    for i, j in enumerate(asignacion):
        fila_sum = sum(channel[i][k] for k in range(n))
        correcto = channel[i][j]
        error += P[i] * (fila_sum - correcto)

    return error
