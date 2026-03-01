actions = {
    1 : "wink",
    2 : "double blink",
    3 : "close your eyes",
    4 : "jump",
}

def commands(binary_str):
    l = []
    for i in range(1, len(binary_str)+1):
        print("i : ", i)
        print(binary_str[-i])
        if i in actions :
            print(actions[i])
        if binary_str[-i] == "1":
            if i == 5 :
                l.reverse()
            else : 
                
                l.append(actions[i])
    return l

print(commands("10011"))

