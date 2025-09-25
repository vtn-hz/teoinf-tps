def getSubfix(code: str, prefix: str):
    return code.replace(prefix, "", 1)

def hasAnyEqual(stack, S: set):
    return S in stack

'''
Sardinas-Patterson algorithm to determine if a code is uniquely decodable.
Input: A set of strings S representing the code.
Output: True if the code is uniquely decodable, False otherwise.
'''
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