from utils.errores.metricas import erroresDetectables, erroresCorregibles

def main(): 
    C1 = ['00', '01', '10', '11']
    C2 = ['000', '100', '101', '111']
    C3 = ['0000', '0011', '1010', '0101']
    C4 = ['0100100', '0101000', '0010010', '0100000']
    C5 = ['0100100', '0010010', '0101000', '0100001']
    C6 = ['0110000', '0000011', '0101101', '0100110']


    print( "hamming:" + str(hamming(C1)) )
    print( "errores detectables:" + str(erroresDetectables( C1 )) )
    print( "errores corregibles:" + str(erroresCorregibles( C1 )) )

    print( "hamming:" + str(hamming(C2)))
    print( "errores detectables:" + str(erroresDetectables( C2 )) )
    print( "errores corregibles:" + str(erroresCorregibles( C2 )) )


    print( "hamming:" + str(hamming(C3)))
    print( "errores detectables:" + str(erroresDetectables( C3 )))
    print( "errores corregibles:" + str(erroresCorregibles( C3 )))
    
    print( "------------" )

    print( "hamming:" + str(hamming(C4)) )
    print( "errores detectables:" + str(erroresDetectables( C4 )) )
    print( "errores corregibles:" + str(erroresCorregibles( C4 )) )

    print( "hamming:" + str(hamming(C5)))
    print( "errores detectables:" + str(erroresDetectables( C5 )) )
    print( "errores corregibles:" + str(erroresCorregibles( C5 )) )


    print( "hamming:" + str(hamming(C6)))
    print( "errores detectables:" + str(erroresDetectables( C6 )))
    print( "errores corregibles:" + str(erroresCorregibles( C6 )))


 
main()

'''

Color Código 1 Código 2 Código 3
Rojo 00 000 0000
Amarillo 01 100 0011
Verde 10 101 1010
Azul 11 111 0101

Color Código 1 Código 2 Código 3
Rojo 0100100 0100100 0110000
Amarillo 0101000 0010010 0000011
Verde 0010010 0101000 0101101
Azul 0100000 0100001 0100110
'''