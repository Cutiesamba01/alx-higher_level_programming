#!/usr/bin/python3

def uppercase(str):

    new_str = ""

    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        new_str += char

            print("{}".format(new_str))
