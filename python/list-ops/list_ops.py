def append(list1, list2):
        return (list1 + list2)


def concat(lists):
    resultat = []
    for liste in lists:
              resultat = append(resultat, liste)
    return(resultat)

def filter(function, list):
    resultat = []
    for element in list:
         if function(element) :
              resultat = append(resultat, [element])
    return(resultat)

print(filter(lambda x: x % 2 == 1, [1, 2, 3, 5]))

def length(list):
    count = 0
    for element in list :
        count += 1
    return count

def map(function, list):
    resultat = []
    for element in list :
         resultat = append(resultat, [function(element)])
    return(resultat)

def foldl(function, list, initial):
    resultat = initial
    for element in list :
        resultat = function(resultat, element)
    return resultat

def foldr(function, list, initial):
    resultat = initial
    for element in list [::-1]:
         resultat = function(resultat,element)
    return resultat

def reverse(list):
    resultat = []
    for element in list[::-1]:
        resultat = append(resultat,[element])
    return resultat
         
