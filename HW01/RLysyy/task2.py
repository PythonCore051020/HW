"""This is the Task2 module.
"""

__version__ = '1.0'

try:
    v_name = input('What is your name? ')
    v_age = input('How old are you? ')
    v_city = input('Where do you live? ')

    print(f'Hello, {v_name}, Your age is {v_age}, You live in {v_city}')
except Exception as e:
    print('Something bad happened. Error:', e)
