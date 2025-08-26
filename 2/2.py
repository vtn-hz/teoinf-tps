
fuente = [
    'A', 'a', 'a', 'b', 'c', 'z', 'az', 
    'A', 'a', 'a', 'b', 'c', 'z', 'az', 'b', 'lorem'
]

def getSDistribution( fuente ):
    dictionary = {}
    for key in fuente:
        if not (key in dictionary):
            dictionary[key] = 0
         
        dictionary[key] += 1
    
    return [
        list(dictionary.keys()),
        [ item / len(fuente) for item in dictionary.values() ]
    ]
    
print (getSDistribution( fuente ))

         
