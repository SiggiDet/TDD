def add(number):
    """recieves a string and returns a value"""
    len_of_number = len(number)
    if len_of_number == 0:
        return 0

    else:
        number_list = number.split(",")
        for i in range (len(number_list)):
            number_list[i] = int(number_list[i])
        return sum(number_list)