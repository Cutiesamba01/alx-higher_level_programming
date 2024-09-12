#!/usr/bin/python3

import sys

if __name__ == "__main__":

    if len(sys.argv) > 1:
        total_sum = sum(int(arg) for arg in sys.argv[1:])
    else:
        total_sum = 0

    print(f"{total_sum}")
