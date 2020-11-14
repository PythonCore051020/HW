# class A:
#     cm = []
#     ci = 123
#
#     def my_print(self, st=None):
#         print(st, self.cm, self.ci, self.im, self.ii)
#
#     def __init__(self):
#         self.im = [1, 2, 3]
#         self.ii = 123
#     def __del__(self):
#         print("deletefile")
#
# # a = A()
# # print(a)
# # print(type(a))
# # print(A.__doc__)
# # a.my_print("MY")
# # print(dir(a))
# # print(a.__dict__)
# # print(dir(A))
# # print(A.__dict__)
# a1 = A()
# a2 = A()
# a1.my_print()
# a2.my_print()
# a1.cm.append(10)
# a1.im.append(20)
# a1.my_print()
# a2.my_print()
# import pprint
# pprint.pprint(a1.__dict__)
# pprint.pprint(a2.__dict__)
# pprint.pprint(A.__dict__)
# del a2
#
# print()


# class Person:
#     # def __new__(cls, *args, **kwargs):
#     #     print("new")
#     #     return super().__new__(cls)
#
#     def __init__(self, name, age=18, sex="woman"):
#         self.age = age
#         self.sex = sex
#         self.name = name
#
#     def __str__(self):
#         return f"name:{self.name} age:{self.age} sex:{self.sex}"
#
#     def __repr__(self):
#         return f"<{self.name}, {self.age},{self.sex}>"
#
#     def __add__(self, other):
#         if isinstance(other, int):
#             self.age += other
#
#     def __add__(self, other):
#         if isinstance(other, int):
#             return Person(name=self.name,
#                           age=self.age + other,
#                           sex=self.sex)
#
#
# # p1 = Person("anri")
# # p2 = Person("oleh", 21, "man")
# # p3 = Person(age=21, name="kira", sex="man")
# # # print(p1, p1.name)
# # # print(p2, p2.name)
# # # print(p3, p3.name)
# # # s = str(p1)
# # # print(s)
# # # print([p1, p2, p3])
# # print(p1)
# # p4 = p1 + 20
# # p5 = p1.__add__(40)
# # print(p1)
# # p1 + "20"
# # print(p1)
# # print(p4)
# # print(p5)
#
# class Human(Person):
#     def __init__(self, name, age=21, sex="man", color="red"):
#         super(Human, self).__init__(name, age, sex)
#         self.color = color
#
# h1 = Human("ori")
# print(h1)


# class A:
#     cm = []
#     ci = 123
#
#     def my_print(self, st=None):
#         print(st, self.cm, self.ci, self.im, self.ii)
#
#     def __init__(self):
#         self.im = [1, 2, 3]
#         self.ii = 123
#     def __del__(self):
#         print("deletefile")
#

# class Encapsulation:
#     def __init__(self, a, b, c):
#         self.public = a
#         self._protected = b
#         self.__private = c
#
#
# e = Encapsulation(1, 2, 3)
# print(e.public)
# print(e._protected)
# # print(e.__private)
# print(e._Encapsulation__private)


# class P:
#
#     def __init__(self,x):
#         self.__set_x(x)
#
#     def __get_x(self):
#         print("get")
#         return self.__x
#
#     def __set_x(self, x):
#         print("set")
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x
#
#     x = property(__get_x, __set_x)
#
# p = P(100)
# print(p.x)
# p.x = 1000

class Test:
    def __init__(self):
        self.x = 10
        self.y = 10

    def p1(self):
        print(self, type(self), dir())

    @classmethod
    def p2(cls):
        print(cls, type(cls), dir())

    @staticmethod
    def p3():
        print(dir())

t = Test()
t.p1()
# Test.p1()
# Test.p1("bfjd")
t.p2()
Test.p2()
Test.p3()
t.p3()