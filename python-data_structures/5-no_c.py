#!/user/bin/python3
def no_c(my_string):
    """remove all characters c and C from a string
        my_string is the traited string"""
    new_string = ""  # add new string and initialize
    for index in my_string:
        if index != 'c' and index != 'C':
            new_string += index  # if charac is not c or C, add at the string
    return new_string
