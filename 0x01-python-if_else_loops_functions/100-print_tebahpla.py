#!/usr/bin/python3

for n in range(ord('z'), ord('a') - 1, -1):
    if n % 2 == 0:
        diff = 0
    else:
        diff = 32
    print("{}".format(chr(n - diff)), end='')
