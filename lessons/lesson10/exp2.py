from exp3 import f3

def f2(value):
    try:

        value = value/2
    except:
        raise IndexError("MyError")
    return f3(value)