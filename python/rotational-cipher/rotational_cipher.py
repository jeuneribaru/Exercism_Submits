def rotate(text, key):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    alphabet_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mot = ''
    for i in range(len(text)) : 
        if text[i] in alphabet :
            for j in range(len(alphabet)) : 
                if text[i] == alphabet[j]:
                    mot+=alphabet[(j+key)%26]
        elif text[i] in alphabet_maj :
            for j in range(len(alphabet_maj)) : 
                if text[i] == alphabet_maj[j]:
                    mot+=alphabet_maj[(j+key)%26]
        else : mot += text[i]
    return(mot)
