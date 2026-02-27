
def is_armstrong_number(number):
    nombre = str(number)
    s=0
    for i in range(0,len(nombre)):
        s+= int(nombre[i])**len(nombre)
    if s == int(number) : return True 
    else : return False    
