def divider(a, b):
    return a / b


try:
    divider(42, 0)
except ZeroDivisionError:
    print('Please do not divide by zero!')
