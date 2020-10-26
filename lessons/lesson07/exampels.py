# def foo(name):
#     print(f"my name: {name}")
#
#
# # print(dir())
# # print(type(foo))
# foo("Anna")
# t = foo("Vasa")
# print(t)

# def foo(name):
#     """ foo boo
#
#     :param name: str myName
#     :return:  str string
#     """
#     s = f"my name: {name}"
#     print(s)
#     return s
#
#
# t = foo("Vasa")
# print("t: ", t)
# print(foo.__doc__)
# print(help(foo))

# def my_sum(arg1, arg2):
#     total = arg1 + arg2
#     print("Inside the function : ", total)
#     return total
#     print("After operator the return ")
#
#
# s = my_sum(1, 2)
# print("sum:", s)

# def bol(i, j, k):
#     print(f"{i} + {j} > {k} == {i + j > k}")
#     return i + j > k
#
#
# def my_foo():
#     for i in range(3, 9):
#         for j in range(10, 14):
#             for k in range(17, 20):
#                 print(i, j, k)
#                 # if i + j > k :
#                 if bol(i, j, k):
#                     # return (i, j, k)
#                     pass
#     return
#
#
# s = my_foo()
# print("sum:", s)


# def f(a, b):
#     print(f"a:{a} b:{b}")
#
#
# f(1, 2)
# f(2, 1)
# f(b=2, a=1)


# def f(a, b, c=10):
#     print(f"a:{a} b:{b} c:{c}")
#
#
# # f()
# f(1, 2)
# f(2, 1)
# f(2, 1, 3)
# f(b=2, a=1)
# f(b=2, a=1, c=99)


# def f(a=[]):
#     a.append(1)
#     print(a)
# def f(a=None):
#     if a is None:
#         a = []
#     a.append(1)
#     print(a)
#
#
# f()
# f()
# f([1, 2, 3, 4, 5, 6])
# f()


# def f(a, b=1, c=1):
#     print(f"a:{a} b:{b} c:{c}")
#
#
# f(1)
# f(1, 2)
# f(2, 1)
# f(2, 1, 3)
# f(b=2, a=1)
# f(b=2, a=1, c=99)

# def f(a, *args, b=1, **qargs):
#     print(f"{a} {args} {b} {qargs}")
#
#
# f(1, 2, 3, b=22, k=77)
# f(1)
# f(1, 2, 3, k=77)


# def f(a, b=1, *args, **qargs):
#     print(f"{a} {args} {b} {qargs}")
# f(1, 2, 3, b=22, k=77)
# f(1)
# f(1, 2, 3, k=77)

# def f(*args, b=1,  **qargs):
#     print(f" {args} {b} {qargs}")
# f(1, 2, 3, b=22, k=77)
# f(1)
# f(1, 2, 3, k=77)

# def f(a, b, c):
#     print(f"a:{a} b:{b} c:{c}")
#
#
# t = (1, 2, 3)
# f(t[0], t[1], t[2])
# f(*t)
# d = {"b": 20, "a": 10, "c": 30}
# f(a=d['a'], b=d['b'], c=d['c'])
# f(**d)
# f(*d)
# print(dir())
# a = 1

# def f():
#     t = 1
#     print(dir())
#     def g():
#         print(t)
#     return  g
# print(dir())
# k = f()
# k()
# print(dir())


# a = 1
# def f():
#     a = 10
#     print(a)
# f()
# print(a)


# a = 1
# def f():
#     print(a)
#     a = 10
#     print(a)
# f()
# print(a)

# a = 1
# def f():
#     global a
#     a = 10
#     print(a)
# f()
# print(a)

# l = []
# def f():
#     l.append(10)
#     print(l)
# f()
# f()
# print(l)
def f(n):
    print(f"{n}*f({n - 1})")
    if n == 1:
        return 1
    return n * f(n - 1)


print(f(10))

print(dir())

a = lambda a, b, c, d: a + b + c + d
print(a(1, 2, 3, 4))
print(dir())
