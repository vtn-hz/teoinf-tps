from utils.errores.hamming import hamming

def erroresDetectables( C: list[str] ) -> int:
    return hamming(C) - 1

def erroresCorregibles( C: list[str] ) -> float:
    return (hamming(C) - 1) // 2
