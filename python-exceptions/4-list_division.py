#!/usr/bin/python3
def list_division(my_list1, my_list_2, list_length):
    new_list = []
    for index in range(list_length):
        try:
            div = my_list1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
