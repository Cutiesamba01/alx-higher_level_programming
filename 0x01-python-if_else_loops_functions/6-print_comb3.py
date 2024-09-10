#!/usr/bin/python3

for o in range(9):
    for d in range(o + 1, 10):
        if o < 8:
            print("{}{}".format(o % 10, d % 10), end=", ")
        else:
            print("{}{}".format(o % 10, d % 10), end="\n")
