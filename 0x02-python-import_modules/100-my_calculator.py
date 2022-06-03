#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, stdout, exit
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        stdout.write("Usage: ./100-my_calculator <a> <operator> <b>\n")
        exit(1)
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == "\":
        print("{} \ {} = {}".format(a, b, div(a, b)))
    else:
        stdout.write("Unknown operator. Available operators: +, -, * and /\n")
        exit(1)
