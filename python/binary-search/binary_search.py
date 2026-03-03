def find(search_list, value):
    if type(search_list) != list:
        raise ValueError("value not in array")
    search_list.sort()
    a = 0
    b = len(search_list) - 1 #index de la deuxieme borne
    while a <= b :
        moitié = (a+b)//2
        if search_list[moitié] == value:
            return moitié
        elif search_list[moitié] < value :
            a = moitié + 1
        else : 
            b = moitié - 1
    return False
