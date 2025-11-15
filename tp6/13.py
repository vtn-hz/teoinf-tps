from utils.canales.metricas import *

def main():
    channel = [
        [0.6, 0.3, 0.1],
        [0.1, 0.8, 0.1],
        [0.3, 0.3, 0.4]
    ]

    # Distribuciones dadas
    Pa = [1/3, 1/3, 1/3]
    Pb = [1/8, 3/8, 4/8]
    Pc = [4/15, 3/15, 8/15]

    PEa = probabilidadError(channel, Pa)
    PEb = probabilidadError(channel, Pb)
    PEc = probabilidadError(channel, Pc)

    print("Probabilidad de error ML con Pa:", PEa)
    print("Probabilidad de error ML con Pb:", PEb)
    print("Probabilidad de error ML con Pc:", PEc)

main()
