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

def main():
    val = eval( input("S: ") )

    if (sardinasPatterson(val)):
        print("Es univoco")
    else:
        print("No es univoco")

main()