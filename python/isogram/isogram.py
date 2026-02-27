def is_isogram():
    string = string.lower()

    for i in range(len(string)):
        char = string[i]
        if char in " -":
            continue
        if char in string[i+1:]:
            return False
    
    return True
