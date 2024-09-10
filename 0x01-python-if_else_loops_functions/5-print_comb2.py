#!/usr/bin/python3

for h in range(0, 100):
    if h != 99:
        print("{:02d}".format(h), end=", ")
    else:
        print("{:02d}".format(h), end="\n")
