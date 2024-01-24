#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    nameslist = dir(hidden_4)
    for name in namesList:
        if "__" != name[:2]:
            print(name)
