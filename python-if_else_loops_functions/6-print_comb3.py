#!/usr/bin/python3
for number1 in range(10):
    for number2 in range(10):
        if number1 == number2:
            continue
        if number1 < number2:
            if number1 != 8 or number2 != 9:
                print("{:d}{:d}".format(number1, number2), end=", ")
            else:
                print("{:d}{:d}".format(number1, number2))
