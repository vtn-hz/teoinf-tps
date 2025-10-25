exec(open("utils/canales/priori/entropy.py").read())
exec(open("utils/canales/posteriori/entropy.py").read())


def main(Pinit: list[float], channel: list[list[float]]):
    print(calculateHPriori(Pinit))   
    print(calculateHPosteriori(Pinit, channel))
    print('-------')
    

Pinit_C1 = [0.14, 0.52, 0.34]
channel_C1 = [
    [0.50, 0.30, 0.20],
    [0.00, 0.40, 0.60],
    [0.20, 0.80, 0.00]
]

Pinit_C2 = [0.25, 0.25, 0.50]
channel_C2 = [
    [0.25, 0.25, 0.25, 0.25],
    [0.25, 0.25, 0.00, 0.50],
    [0.50, 0.00, 0.50, 0.00]
]

Pinit_C3 = [0.12, 0.24, 0.14, 0.50]
channel_C3 = [
    [0.25, 0.15, 0.30, 0.30],
    [0.23, 0.27, 0.25, 0.25],
    [0.10, 0.40, 0.25, 0.25],
    [0.34, 0.26, 0.20, 0.20]
]

if __name__ == "__main__":
    main(Pinit_C1, channel_C1)
    main(Pinit_C2, channel_C2)
    main(Pinit_C3, channel_C3)