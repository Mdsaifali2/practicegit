def addition(a, b, c):
    return a + b + c

def subtraction(a, b, d):
    return a - b-d

def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
