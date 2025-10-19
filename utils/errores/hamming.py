
def hamming (C: list[str]) -> int:
    
    if len(C) <= 1:
        raise Exception("No hay cantidad de codigos suficientes") 

    _min = []
    for i in range(0, len(C)):
        for j in range(i+1, len(C)):
            if i != j:
                dif_amount = 0 
                for k in range(0, len(C[i])):
                    dif_amount += int(C[i][k] != C[j][k]) 
                _min.append( dif_amount )

    return min( _min )