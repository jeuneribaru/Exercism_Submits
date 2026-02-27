def equilateral(sides):
    a,b,c = sides[0], sides[1], sides[2]
    if a == 0 or b == 0 or c == 0 : return False
    if a + b <= c or a + c <= b or b + c <= a: return False
    if a == b and b == c and a == c : return True 
    else : return False

def isosceles(sides):
    a,b,c = sides[0], sides[1], sides[2]
    if a == 0 or b == 0 or c == 0 : return False
    if max(a,b,c) == a :
        if a == b or a == c : return True 
        else : return False 
    if max(a,b,c) == b :
        if b == a or b == c : return True 
        else : return False 
    if max(a,b,c) == c :
        if c == a or c == b : return True 
        else : return False 


def scalene(sides):
    a,b,c = sides[0], sides[1], sides[2]
    if a == 0 or b == 0 or c == 0 : return False
    if equilateral(sides) : return False
    if max(a,b,c) == a :
        if a**2 == b**2 + c**2 : return True
        else : return False 
    if max(a,b,c) == b :
        if b**2 == a**2 + c**2 : return True 
        else : return False 
    if max(a,b,c) == c :
        if c**2 == b**2 + a**2 : return True 
        else : return False 
