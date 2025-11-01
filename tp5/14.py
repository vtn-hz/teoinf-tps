from utils.canales.posteriori.entropy_media import calculateHPosterioriMediaAB, calculateHPosterioriMediaBA, calculateRuido, calculatePerdida
from utils.canales.priori.entropy import calculateHPriori
from utils.canales.posteriori.entropy import calculateHPosterioriTotal
from utils.canales.priori.probs import getProbabilidadPriori, getPrioriMatrixFull
from utils.canales.entropia_canal import calculateHCanal
from utils.canales.informacion_mutua import informacionMutuaAB, informacionMutuaBA, informacionMutuaABSimple, informacionMutuaBASimple

def main():
    P = [0.7, 0.3]

    MC = [
        [0.7, 0.3],
        [0.4, 0.6]
    ]

    print( 'H(A): ',  calculateHPriori(P) )
    print( 'H(B): ', calculateHPosterioriTotal(P, MC) )
    print( 'H(A/B): ', calculateRuido(P, MC) ) 
    print( 'H(B/A): ', calculatePerdida(P, MC) ) 
    print( 'H(A, B): ', calculateHCanal(P, MC) ) 
    print( 'I(A, B): ', informacionMutuaABSimple(P, MC))
    print( 'I(B, A): ', informacionMutuaBASimple(P, MC))
main()