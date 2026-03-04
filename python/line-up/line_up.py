dic = {
        1 : "st",
        2 : "nd",
        3 : "rd",
    }

def line_up(name, number):
    number = str(number)
    if (len(number)>= 2)  and (number[-2:] in ("11","12","13")):
        suffixe = 'th'
    elif int(number[-1]) in dic :
        suffixe = str(dic[int(number[-1])])
    else : 
        suffixe = "th"
    return(f"{name}, you are the {number}{suffixe} customer we serve today. Thank you!")

print(line_up("Gianna", "4"))
print(line_up("Dahir", "162"))
print(dic)