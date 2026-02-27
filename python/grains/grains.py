
def square(number):
    s=0
    if number > 64 or number < 1 :
        raise ValueError("square must be between 1 and 64")
    else : 
        for x in range(1, number+1):
            if x == 1:
                s=1
            else : s=2**(number-1)
    return s

def total():
    s = 0
    for x in range(1,65):
        s+=square(x)
    return s
