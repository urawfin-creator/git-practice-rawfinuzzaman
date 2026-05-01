def multiply(a,b):
    return a*b
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error : Cannot be divided by zero."