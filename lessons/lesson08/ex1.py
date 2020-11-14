# import ex2
# print(__name__)
#
# # import sys
# # import pprint
# # pprint.pprint(sys.path)
#
# print(ex2.CONSTS)
# print(ex2.CONST)
# ex2.f()
#
# print()
# ex2.CONST = 20
# ex2.CONSTS.append(99)
# print(ex2.CONSTS)
# print(ex2.CONST)
# ex2.f()
#
# print()
# from ex2 import CONSTS
# from ex2 import CONST
# from ex2 import f
# print(CONSTS)
# print(CONST)
# f()
#
# print()
# CONST = 20
# CONSTS.append(99)
# print(CONSTS)
# print(CONST)
# ex2.f()
# print(ex2.CONSTS)
# print(ex2.CONST)
# ex2.f()
# from ex2 import CONST

# from ex2 import CONST as c
# CONST = "safsd"
# print(c)
# print(CONST)
# print(dir())
# from ex2 import CONSTS , CONST, f
# print(CONST, CONSTS)
# f()
# from ex2 import CONSTS as cs, CONST, f as g
# print(CONST, cs)
# g()
# # from ex2 import CONSTS as cs,\
# #     CONST,\
# #     f as g
# from ex2 import (CONSTS as cs,
#                  CONST,
#                  f as g)
# print(CONST, cs)
# g()
#
# print(__name__)
# if __name__ == "__main__":
#     print("temp")
# import ex2
# print(__name__)
# if __name__ == "__main__":
#     print("temp")

# from ex2 import *
# from ex2 import CONSTS, CONST, f
# print(dir())
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "Hello, World!"
#
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)

b = "cfch gchf cf                ghchfh"
print(' '.join(b.split()))