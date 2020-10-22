# # list
# l = []
# l = [1, "1", .01]
# l = list()
# l = list((1, "1", .01))
# l = list("test")
# print(type(l), l)
# print(dir(list))
# for i in [m for m in dir(list) if not m[0] == "_"]:
#     print(i)

# l = [1, 2, 4, 5, 6, 1, 2, 5, 2, 5, 7, 8]
# print(l)
# l.append("test")
# l.append(["1", "2"])
# l.append((1, 2, 3))
# print(l)
# print(l[10])
# print(l[13][1])
# print(l, id(l))
# l.clear()
# print(l, id(l))
# l = []
# print(l, id(l))


# l = [1, 2, 4, 5, 6, 1, 2, 5, 2, 5, 7, 8]
# _l = l
# t = [99, 100]
# l.append(t)
# l1 = l.copy()
# import copy
# l2 = copy.deepcopy(l)
# l[0] = "t"
# t.append(1001)
# print(l, id(l))
# print(_l, id(_l))
# print(l1, id(l1))
# print(l2, id(l2))

# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l)
# l.append([10,  11, 12, 13])
# print(l)
# l.extend([10,  11, 12, 13])
# l.extend("abc")
# print(l)

# l = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 00, 10, 20]
# print(l.index(20))
# print(l.index(20, 5))
# # print(l.index(20, 5, 10))
# # print(l.index(120))
# l.insert(3, ["1", "m"])
# l[2] =  ["1", "m"]
# print(l)

# l = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 00, 10, 20]
# k = l.pop()
# print(k, l)
# k = l.pop(2)
# print(k, l)

# l = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 00, 10, 20]
# l.remove(20)
# print(l)

# l = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 00, 10, 20]
# l.reverse()
# print(l)
# print(l[::-1])
# print(l)
# l.sort()
# print(l)
# l = ["11.10.10", "10.10.10", "12.10.09", "12.10.07", "12.11.07"]
# l.sort()
# print(l)
#
# def myS(element):
#     l = [int(e) for e in element.split(".")]
#     result = l[0]
#     result += l[1]*31
#     result += l[2]*100 * 365
#     print(result, element, l)
#     return result
# l.sort(key=myS)
# print(l)


# tuple
# for i in [m for m in dir(tuple) if not m[0] == "_"]:
#     print(i)
# t = ()
# t = (1, 2, 3)
# t = (1,)
# t = tuple()
# t = tuple((1, 2, 3))
# print(type(t))
# print(t)
# # t[1] = 10
# print(t[1])

# dict
# d = {}
# d = {10: [100], "sada": (1, 2, 3)}
# d = dict()
# d = dict(((1, 2), ))
#
# print(type(d), d)
# for i in [m for m in dir(dict) if not m[0] == "_"]:
#     print(i)
# d = {10: [100], "sada": (1, 2, 3)}
# d1 = d.fromkeys("saadasdasfsa", 10)
# print(d, d1)
# print(d[10])
# print(d["sada"])
# # print(d[11])
# print(d.get(11), d.get(10))
# p = d.pop("sada")
# # p = d.pop(111)
# print(p, d)
# d.update({1:10, 11: "ss"})
# print(d)
#
# print(d.items())
# print(d.keys())
# print(d.values())
#
# for key in d:
#     print(key, d[key])
#
# for key, value in d.items():
#     print(key, value)
#

# set

s = {1, 2, 3, 4, 1, 2, 3, 4}
s = set()
s = set("vdgsvfhdsvchgvdsgcsdgg653465256246532343652")

print(type(s), s)
for i in [m for m in dir(set) if not m[0] == "_"]:
    print(i)
s.add("asd")
s.add("asd")
s.add("asd")
print(s)
s.isdisjoint("aaaa")
print(s)
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1.difference(s2))
print(s2.difference(s1))
print(s2.isdisjoint(s1))
print(s2.isdisjoint({1, 2}))
