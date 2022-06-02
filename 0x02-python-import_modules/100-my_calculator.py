#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, stdout, exit
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        stdout.write("Usage: ./100-my_calculator <a> <operator> <b>\n")
        exit(1)
    operator = argv[2]
    operand1 = int(argv[1])
    operand2 = int(argv[3])
    if operator == "+":
        print("{} + {} = {}".format(operand1, operand2, add(operand1, operand2)))
    elif operator == "-":
        print("{} - {} = {}".format(operand1, operand2, sub(operand1, operand2)))
    elif operator == "*":
        print("{} * {} = {}".format(operand1, operand2, mul(operand1, operand2)))
    elif operator == "/":
        print("{} / {} = {}".format(operand1, operand2, div(operand1, operand2)))
    else:
        stdout.write("Unknown operator. Available operators: +, -, * and /\n")
        exit(1)
