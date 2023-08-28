#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        division = None
    finally:
        print("Inside result: ", end="")
        print("{}".format(division))
        return division
