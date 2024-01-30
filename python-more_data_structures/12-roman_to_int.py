#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    value = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}
    total = 0
    for i in range(len(roman_string)):
        if i > 0 and value[roman_string[i]] > value[roman_string[i - 1]]:
            total += value[roman_string[i]] - 2 * value[roman_string[i - 1]]
        else:
            total += value[roman_string[i]]
    return total
