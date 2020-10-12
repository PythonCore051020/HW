"""This is the Task1 module.
"""

__version__ = '1.0'

try:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))

    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
except ValueError as e:
    print("Incorrect data entered, please enter a number. Error:", e)
