#!/usr/bin/python3
import calculator_1 as math
if __name__ == '__main__':
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, math.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, math.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, math.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, math.div(a, b)))
