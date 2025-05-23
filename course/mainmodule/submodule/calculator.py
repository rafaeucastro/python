def sum(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def pow(base, exponent):
    if(exponent == 0): return 1

    accumulator = 1
    for _ in range(exponent):
        accumulator = accumulator * base

    return accumulator