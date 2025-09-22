import math

# unidades de información: bits (base 2)
def calculateI(pi: float) -> float:
    if pi <= 0:
        raise ValueError("La probabilidad debe ser mayor que 0")

    return math.log2(1/pi); 