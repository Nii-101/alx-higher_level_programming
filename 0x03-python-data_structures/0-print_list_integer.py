#!/usr/bin/python3
def print_list_integer(my_list=[]):
    a = 0
    x = len(my_list)
    while a < x:
        print("{}".format(my_list[a]))
        a = a + 1
