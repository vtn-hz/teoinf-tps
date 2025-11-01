exec(open('utils/canales/posteriori/entropy_media.py').read())
exec(open('utils/canales/priori/entropy.py').read())
exec(open('utils/canales/priori/probs.py').read())
exec(open('utils/canales/entropia_canal.py').read())
exec(open('utils/canales/informacion_mutua.py').read())

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