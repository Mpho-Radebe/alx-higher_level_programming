#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0

    num = 0
    if "IV" in roman_string:
        num += 4
        roman_string = roman_string.replace("IV", "")

    if "XL" in roman_string:
        num += 40
        roman_string = roman_string.replace("XL", "")

    if "CD" in roman_string:
        num += 400
        roman_string = roman_string.replace("CD", "")

    if "IX" in roman_string:
        num += 9
        roman_string = roman_string.replace("IX", "")

    if "XC" in roman_string:
        num += 90
        roman_string = roman_string.replace("XC", "")

    if "CM" in roman_string:
        rum += 900
        roman_string = roman_string.replace("CM", "")

    if "V" in roman_string:
        num += 5
        roman_string = roman_string.replace("V", "")

    if "L" in roman_string:
        num += 50
        roman_string = roman_string.replace("L", "")

    if "D" in roman_string:
        num += 500
        roman_string = roman_string.replace("D", "")

    num += roman_string.count("I")
    num += roman_string.count("X") * 10
    num += roman_string.count("C") * 100
    num += roman_string.count("M") * 1000

    return num
