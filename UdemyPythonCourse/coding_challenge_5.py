def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

result = divide(20, 0)
print result