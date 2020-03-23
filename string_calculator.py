class NumberToHighError(Exception):
    pass

def get_num(number):
    """Gets the number from the string, and cuts the string"""
    len_of_number = len(number)
    int_num = ""
    new_number =""
    i = 0 # counter

    while i != len_of_number: # The while loop is used for if the numbers happens to be longer then one letter
        if number[i] == ",":
            break
        elif number[i] == "\n":
            break
        else:
            int_num += number[i]
            i += 1

    new_number = number[i:] # disposing the number that we collected from the string (number)
    return int_num,new_number # cuts the number (prev) away from the string (number)

def add_recur(number,prev= 0):
    """Recursive"""
    len_of_number = len(number)

    if len_of_number == 0:
        return 0 + prev
    elif number[0] == "\n":
        return add_recur(number[1:]) / prev
    elif number[0] == ",":
        return add_recur(number[1:]) + prev
    else:
        prev,number = get_num(number)
        prev = int(prev)

        if prev > 1000:
            prev = 0

        return add_recur(number,prev)

def add(number):
    """recieves a string and returns a value"""
    return_val = add_recur(number)
    return return_val