#!/usr/bin/python3

def no_c(my_string):
    my_string = my_string.translate({ord(a): '' for a in 'Cc'})
    return (my_string)
