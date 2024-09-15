#!/usr/bin/bash


def no_c(my_string):

    new_string = ""

    for o in my_string:
        if (o != 'c') and (o != 'C'):
            new_string += o

        return (new_string)
