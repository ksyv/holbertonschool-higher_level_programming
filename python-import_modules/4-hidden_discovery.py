#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    nameslist = dir(hidden_4)
    for name in namesList:
        if "__" != name[:2]:
            print(name)
