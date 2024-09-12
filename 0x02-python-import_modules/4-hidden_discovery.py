#!/usr/bin/python3

import hidden_4
import sys

if __name__ == "__main__":
    # Get all names defined in the module
    names = dir(hidden_4)
    # Filter out names that starts with __
    filter_names = [name for name in names if not name.startswith("__")]
    # Sorts names alphabetically
    filter_names.sort()
    # Prints each name on a new line
    for name in filter_names:
        print(name)
