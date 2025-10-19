exec(open("./utils/errores/hamming.py").read())

def erroresDetectables( C: list[str] ) -> int:
    return hamming(C) - 1

def erroresCorregibles( C: list[str] ) -> float:
    return (hamming(C) - 1) // 2
