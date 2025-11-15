from utils.canales.metricas import *

def main ():
    channel = [
        [ 0.6, 0.4], 
        [ 0.2, 0.8]
    ]

    P = [0.5, 0.5]
    PE = probabilidadError(channel, P)
    print("Probabilidad de error ML: ", PE)    


main()