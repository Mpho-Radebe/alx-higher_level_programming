#!/usr/bin/python3
for ascci_code in range(97, 123):
    if chr(ascci_code) != 'q' and chr(ascci_code) != 'e':
        print(f"{chr(ascci_code)}", end="")
