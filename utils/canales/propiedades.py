
def isCanalNoRuido (channel : list[list]) -> bool:
    
    for j in range(len(channel[0])):
        amount = 0
        for i in  range(len(channel)):
            amount += int(channel[i][j] != 0)

            if amount > 1:
                return False
    
    return True

def isCanalDeterminante (channel : list[list]) -> bool:
    
    for i in range(len(channel)):
        amount = 0
        for j in  range(len(channel[0])):
            amount += int(channel[i][j] != 0)

            if amount > 1:
                return False
        
        if amount == 0:
            return False
    
    return True