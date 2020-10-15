# elements = [0, 0.1, -0.1, (), (1,), "", "a", None, {}, {1: 1}]
# for element in elements:
#
#     if element:
#         print(element, True)
#     else:
#         print(element, False)

# l = 1
# print(not l)

# a, b, c = True, True, False
# print(a or b and c)
#
# a, b, c = True, True, False
# print(a and b and c)
# print(c or b or a)

# def t():
#     print("t")
#     return True
# def f():
#     print("f")
#     return False
# print(t() and t() and t())
# print([1] and 0 and {"a"})
# print([1] and [] and 0 and {"a"})
# print([1] and "0" and {"a"} and 156)
# print([1] or 0 or {"a"})
# print([] or 0 or {})
# cond = 1
# if cond == 1:
#     print("2")
#     d = 1
# print(d)
# if cond == 1:
#     print("1")
# print("end")

# cond = 9
# if cond < 10:
#     print("cond < 10")
# else:
#     print("cond >= 10")
# print("end")
# cond = 11
# if cond < 10:
#     print("cond < 10")
# else:
#     print("cond >= 10")
# print("end")


# cond = 30
# if cond < 10:
#     print("cond < 10")
# elif cond >= 10 and cond < 15:
#     print("cond>=10 and cond < 15")
# elif cond >= 15 and cond < 20:
#     print("cond>=15 and cond < 20")
# else:
#     print("else")
#
# cond = 18
# if cond < 10:
#     print("cond < 10")
# elif 10 <= cond < 15:
#     print("cond>=10 and cond < 15")
# elif 15 <= cond < 20:
#     print("cond>=15 and cond < 20")
# else:
#     print("else")
#
# l = 10
# if l < 10:
#     print("1")
# elif l >= 10:
#     print("2")
# elif l > 5:
#     print("3")
# else:
#     print("else")


# cond = True
# # result = cond?true:false
# result = True if cond else False
# print(result)
# result = "True1" if not cond else "False1"
# print(result)
#
# a = 10
# b = 22
# a = a + b  # 32
# b = a - b  # 10
# a = a - b  # 22

# zen_python = ('Beautiful is better than ugly.'
#               'Explicit is better than implicit.'
#               'Simple is better than complex.'
#               'Complex is better than complicated.')
#
# print(zen_python)
# from this import d, s
#
# zen_python = "".join([d.get(c, c) for c in s])
# print(zen_python)
