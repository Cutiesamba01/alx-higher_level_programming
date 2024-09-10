#!/usr/bin/python3

def uppercase(str):

    uppercase = 0
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            uppercase = 32
        else:
            uppercase = 0

            print("{:c}".format(ord(char) - uppercase), end='')
        print()
