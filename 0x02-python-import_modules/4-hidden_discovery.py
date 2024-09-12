#!/usr/bin/python3

import hidden_4
import sys

if __name__ == "__main__":
    names = dir(hidden_4)
    filter_names = [name for name in names if not name.stsratswith("__")]
    filter_names.sort()

    for name in filter_names:
        print(name)
