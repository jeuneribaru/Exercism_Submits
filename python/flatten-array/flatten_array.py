null = "null"

def profondeur(lst): #inutile
    if not isinstance(lst, list):
        return 0
    if not lst:      
        return 1
    return 1 + max(profondeur(x) for x in lst)

def flatten(iterable):
    resultat = []
    for element in iterable:
        if isinstance(element, list):
            resultat.extend(flatten(element))  #recursivité, on appelle flatten pour lisser la liste qui nous embête
        elif ((element is not null) and (element is not None)):              
            resultat.append(element)
    return resultat
