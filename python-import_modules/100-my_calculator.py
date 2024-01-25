#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    match (argv[2]):
        case '+' | '-' | '*' | "/":
            a = int(argv[1])
            b = int(argv[3])
            if argv[2] == '+':
                result = add(a, b)
            elif argv[2] == '-':
                result = sub(a, b)
            elif argv[2] == '*':
                result = mul(a, b)
            elif argv[2] == '/':
                result = div(a, b)
            print("{} {} {} = {}".format(a, argv[2], b, result))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
