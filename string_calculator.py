class NegativeNumError(Exception):
    pass

def get_num(number,delimeter, def_type = None): # def_type is either negative or None (add)
    """Gets the number from the string, and cuts the string"""
    len_of_number = len(number)
    int_num = ""
    new_number =""
    i = 0 # counter

    while i != len_of_number: # The while loop is used for if the numbers happens to be longer then one letter
        if number[i] == delimeter:
            if def_type == "negative":
                i += 1 # remove the ","
            break

        elif number[i] == "\n":
            if def_type == "negative":
                i += 1 # remove the "\n"
            break

        else:
            int_num += number[i]
            i += 1

    new_number = number[i:] # disposing the number that we collected from the string (number)
    return int_num,new_number # cuts the number (prev) away from the string (number)

def negative_recur(negative_num_list,number,delimeter):
    len_of_number = len(number)
    if len_of_number == 0:
        negative_num_str = "Negatives not allowed: " #lists all the negative numbers

        for i in range(len(negative_num_list)):
            if i+1 == len(negative_num_list):
                negative_num_str += str(negative_num_list[i])
            else:
                negative_num_str += str(negative_num_list[i]) + ", "

        raise NegativeNumError(negative_num_str)

    # continuing unitl we have reached to the end of the number
    int_num, number = get_num(number,delimeter,"negative")
    if int(int_num) < 0:
        negative_num_list.append(int(int_num))

    negative_recur(negative_num_list,number,delimeter)

def negative(negative_num, number,delimeter):
    """Lists all the negative numbers from the string (number)"""
    negative_num_list = [negative_num]
    negative_recur(negative_num_list,number,delimeter)

def add_recur(number,delimeter,prev= 0):
    """Recursive"""
    len_of_number = len(number)

    if len_of_number == 0:
        return 0 + prev

    elif number[0] == "\n":
        return add_recur(number[1:],delimeter) / prev

    elif number[0] == delimeter:
        return add_recur(number[1:],delimeter) + prev

    else:
        prev,number = get_num(number,delimeter)
        prev = int(prev)

        if prev > 1000:
            prev = prev - 1000

        elif prev < 0:
            negative(prev,number[1:],delimeter) # when we try to find all of the negative numbers we want to skip "," and "\n"

        return add_recur(number,delimeter,prev)

def get_delimeter(number):
    """gets the delimeter and the number"""

    delimeter = ""

    i = 0 # location in the str
    while number[i] != "\n":
        delimeter += number[i]
        i += 1
    new_number = number[i+1:]

    return delimeter,new_number

def add(number):
    """recieves a string and returns a value"""
    if number[0:2] == "//":
        delimeter,number = get_delimeter(number[2:])
    else:
        delimeter = ","

    return_val = add_recur(number,delimeter)
    return return_val