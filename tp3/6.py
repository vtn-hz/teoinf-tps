def getSubfix(code: str, prefix: str):
    return code.replace(prefix, "", 1)


def hasAnyEqual(stack, S: set):
    return S in stack



def sardinasPatterson (S: set):
    stack = []
    stack.append( set (S))
    
    while (True):
        Si = set()
        for x in S:
            for y in stack[-1]:
                if x == y:
                    continue
                
                subfix = False
                if x.startswith(y):
                    subfix = getSubfix(x, y)
                elif y.startswith(x):
                    subfix = getSubfix(y, x)
                
                if (subfix):
                    if (subfix in S):
                        return False

                    Si.add(subfix)

        if ( hasAnyEqual(stack, Si) ):     
            return True
        
        stack.append( Si )

def hasRepeated(codes: list):
    return len(codes) != len( set(codes) )

def hasSubfixes(codes: list):
    for x in codes:
        for y in codes: 
            if x != y and y.startswith(x):
                return True

    return False

def main(val):

    if hasRepeated(val):
        print("Es bloque")
        return 

    if not hasSubfixes(val):
        print("Es instantaneo")
        return
    
    if sardinasPatterson(set(val)):
        print("Es univoco")
    else:
        print("Es no-singular")

codigo1 = ["1", "01", "001", "0001"]


main(codigo1)

