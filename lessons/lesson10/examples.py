# a = [5, 6, 7, 8]
# b = 20
# try:
#     print("Second element = {}".format(a[1]))
#     # Throws error since there are only 4 elements in array
#     b = 30
#     print("Fifth element = {}".format(a[4]))
# except LookupError as e:
#     print("e", e)
# print(b)


# # Program to handle multiple errors with one except statement
# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a / (a - 3)  # throws ZeroDivisionError for a = 3
#
#     if a >= 4:
#         print("Value of b = ", b)  # throws NameError
#     print(b)
#
# # note that braces () are necessary here for multiple exceptions
# except (ZeroDivisionError, NameError, ValueError):
#     print("Error Occurred and Handled")
# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a / (a - 3)  # throws ZeroDivisionError for a = 3
#
#     if a >= 4:
#         print("Value of b = ", b)  # throws NameError
#     print(b[1])
#
# except ValueError:
#     print("Value Error!")
# except NameError:
#     print("NameError!")
# except ZeroDivisionError:
#     print("ZeroDivisionError!")
# # except Exception as e:
# #     print(e)
# except :
#     print("Error!")


# a = [5, 6, 7, 8]
# b = 20
# try:
#     print("Second element = {}".format(a[1]))
#     # Throws error since there are only 4 elements in array
#     # print("Fifth element = {}".format(a[4]))
# except IndexError as e:
#     print("IndexError: ", e)
# except LookupError as e:
#     print("LookupError: ", type(e))
# else:
#     print("else")
# f = None
# try:
#     f = open("newfile.txt", 'w+')
#     f.write("Second element: ")
# except Exception as e:
#     print(e)
#     print("Something went wrong when writing to the file")
# else:
#     print("Nothing went wrong")
# finally:
#     f.close()
#     print("The 'try except' is finished")

# def parsPositive(element):
#     if element <= 0:
#         raise ValueError("That is not a positive number!")
#     return element
#
#
# try:
#     value = int(input("Enter a positive integer: "))
#     print(parsPositive(value))
# except ValueError as e:
#     print(e)


# class CustomError(ConnectionResetError):
#     def __init__(self, data):
#         self.data = data
#     def __str__(self):
#         return repr(self.data)
# class Custom2Error(CustomError):
#     def __init__(self, data):
#         self.data = data
#     def __str__(self):
#         return repr(self.data)
#
# total_score = int(input("Enter expert score: "))
# try:
#     num_of_group = int(input("Enter number of your group: "))
#     if num_of_group < 1:
#         raise Custom2Error("Number of your group can't be less than 1")
# except CustomError as e:
#     print("We obtain error:", e.data)

# import logging
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename='app.log',
#     filemode='w',
#     format='%(name)s - %(levelname)s - %(message)s %(module)s	%(created)f')
# # logging.warning('This will get logged to a file')
#
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

a = "aaaa10"
from exp2 import f2
try:
    print(f2(a))
except Exception as e:
    print(":(", e)