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

dic_tol = {
    "grey" : '±0.05%',
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%",
}

def resistor_label(colors):
    s = ""
    l = []
    for h in range(len(colors)-1):
        l.append(colors[h])
    print(l)
    for i in range(2) :
        s += str(dic.get(l[i]))
    for j in range(dic.get(l[2])):
        s+= "0"
    s = s.lstrip("0") or "0"
        
    if s[-9 :] == "000000000":
        s = s.replace("0", "", 9)
        return s+ " gigaohms " + str(dic_tol.get(colors[-1]))
    elif s[-6 :] == "000000":
        s = s.replace("0","",6)
        return s+ " megaohms " + str(dic_tol.get(colors[-1]))
    elif s[ -3:] == "000":
        s = s.replace("0", "", 3)
        return s+ " kiloohms " + str(dic_tol.get(colors[-1]))
    
    else : return s+" ohms " + str(dic_tol.get(colors[-1]))

print(resistor_label(["orange", "orange", "orange", "red"]))
print(resistor_label(["red", "black", "red", "yellow"]))
print(resistor_label(["yellow", "violet", "yellow", "blue"]))
print(resistor_label(["black", "grey", "black", "white"]))
