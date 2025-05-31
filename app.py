def addition(a, b, c):
    return a + b + c

def subtraction(a, b, e):
    return a - b-e

def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
