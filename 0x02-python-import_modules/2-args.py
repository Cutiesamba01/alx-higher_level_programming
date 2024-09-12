#!/usr/bin/python3

import sys


def main():
    num_args = len(sys.argv) - 1

    if num_args == 1:
        print("{} argument:".format(num_args))
    elif num_args == 0:
        print("{} arguments.".format(num_args))
    else:
        print("{} arguments:".format(num_args))

    for c in range(1, len(sys.argv)):
        print("{}: {}".format(c, sys.argv[c]))


if __name__ == "__main__":
    main()
