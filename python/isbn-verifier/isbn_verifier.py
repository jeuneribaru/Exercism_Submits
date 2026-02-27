def is_valid(isbn):
    s = 0
    isbn_modif = ''
    for c in range(len(isbn)):
        if isbn[c] == "-":
            pass
        else : 
            isbn_modif += isbn[c]
    if len(isbn_modif) != 10: return False 
    for d in range(len(isbn_modif)):
        if isbn_modif[d] == 'X':
            if d != 9 :
                return False 
            else : s += ((len(isbn_modif)-d)*10)
        elif isbn_modif[d].isnumeric() :
            s += ((len(isbn_modif)-d)*int(isbn_modif[d]))
        else : return False
    if  s%11 == 0 :
        return True
    else: return False 
