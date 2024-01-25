#!/usr/bin/python3
for lettre in range(ord('z'), ord('a') - 1, -1):
    if lettre % 2 != 0:
        upper = 32
    else:
        upper = 0
    print("{:c}".format(lettre - upper), end="")
