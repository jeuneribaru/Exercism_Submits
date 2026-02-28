dic = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
    }

def label(colors):
    s = ""

    for i in range(2) :
        s += str(dic.get(colors[i]))
    for j in range(dic.get(colors[2])):
        s+= "0"
    s = s.lstrip("0") or "0"
        
    if s[-9 :] == "000000000":
        s = s.replace("0", "", 9)
        return s+ " gigaohms"
    elif s[-6 :] == "000000":
        s = s.replace("0","",6)
        return s+ " megaohms"
    elif s[ -3:] == "000":
        s = s.replace("0", "", 3)
        return s+ " kiloohms"
    
    else : return s+" ohms"

print(label(["orange", "orange", "orange"]))
print(label(["red", "black", "red"]))
print(label(["yellow", "violet", "yellow"]))
print(label(["black", "grey", "black"]))