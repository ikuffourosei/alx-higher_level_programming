#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    decimal = [roman_num[x] for x in roman_string]
    dec_len = len(decimal)
    result = 0
    for i in range(dec_len):
        result += decimal[i]
        if decimal[i - 1] < decimal[i] and i != 0:
            result -= (decimal[i - 1] + decimal[i - 1])
    return result
