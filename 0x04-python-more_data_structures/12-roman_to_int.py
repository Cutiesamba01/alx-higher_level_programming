#!/usr/bin/python3


def roman_to_int(roman_string):

    if type(roman_string) is not str or roman_string is None:
        return 0
    result = 0
    zip_str = zip(roman_string, roman_string[1:])

    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for b, r in zip_str:
        if b not in dic.keys():
            return 0
        elif dic[b] >= dic[r]:
            result += dic[b]
        else:
            result -= dic[b]
    result += dic[roman_string[-1]]

    return (result)
