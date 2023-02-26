#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return = a / b
    except:
        result = None
    finally:
        print("Inside return: {}'.format(result))
        return (result)
