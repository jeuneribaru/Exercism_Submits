def steps(number):
    count = 0
    print(number)
    if number <= 0: 
        raise ValueError('Only positive integers are allowed')
    elif number == 1 :
        return(0)
    while number != 1 :
        if number % 2 == 0 :
            number = number/2
            count+=1
            print(number,count)
        else : 
            number = (number*3)+1
            count += 1
            print(number,count)
    return(count)

print(steps(16))