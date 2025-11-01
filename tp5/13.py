from utils.canales.priori.entropy import calculateHPriori
from utils.canales.posteriori.entropy import calculateHPosteriori, calculateHPosterioriTotal


def main(Pinit: list[float], channel: list[list[float]]):
    print(calculateHPriori(Pinit))   
    print(calculateHPosteriori(Pinit, channel))
    print('-------')

# --- Datos de la nueva imagen ---
Pinit_C1 = [2/5, 3/5]
channel_C1 = [
    [3/5, 2/5],
    [1/3, 2/3]
]

Pinit_C2 = [3/4, 1/4]
channel_C2 = [
    [2/3, 1/3],
    [1/10, 9/10]
]

# --- Datos que ya existían (renombrados) ---
Pinit_C3 = [0.14, 0.52, 0.34]
channel_C3 = [
    [0.50, 0.30, 0.20],
    [0.00, 0.40, 0.60],
    [0.20, 0.80, 0.00]
]

Pinit_C4 = [0.25, 0.25, 0.50]
channel_C4 = [
    [0.25, 0.25, 0.25, 0.25],
    [0.25, 0.25, 0.00, 0.50],
    [0.50, 0.00, 0.50, 0.00]
]

Pinit_C5 = [0.12, 0.24, 0.14, 0.50]
channel_C5 = [
    [0.25, 0.15, 0.30, 0.30],
    [0.23, 0.27, 0.25, 0.25],
    [0.10, 0.40, 0.25, 0.25],
    [0.34, 0.26, 0.20, 0.20]
]

if __name__ == "__main__":
    main(Pinit_C1, channel_C1)
    main(Pinit_C2, channel_C2)
    main(Pinit_C3, channel_C3)
    main(Pinit_C4, channel_C4)
    main(Pinit_C5, channel_C5)