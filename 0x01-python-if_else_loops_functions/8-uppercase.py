#!/usr/bin/python3

def uppercase(str):
    for f in str:
        if ord(f) >= 97 and ord(f) <= 122:
            f = chr(ord(f) - 32)
        print("{}".format(f), end="")
    print()
